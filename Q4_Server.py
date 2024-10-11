import socket
import struct
import cv2
import pickle

serverPort = 20000

# Create a socket for the server using TCP
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', serverPort))
# The welcoming socket should be open to receive requests from any client.
serversocket.listen(1)
print("The server is ready to receive")

# Open the SERVER window
cv2.namedWindow("SERVER")

# Initialize the video capture
video = cv2.VideoCapture(0)

while True:
    connectionsocket, clientaddress = serversocket.accept()
    print('GOT CONNECTION FROM:', clientaddress)

    while True:
        ret, frame = video.read()

        if not ret:
            break

        # Display the streaming video in the SERVER window
        cv2.imshow("SERVER", frame)

        # Serialize the frame using pickle
        serialdata = pickle.dumps(frame)

        # Send the frame size as a struct.pack to help the client know when the frame ends
        frame_size = struct.pack("!L", len(serialdata))
        connectionsocket.sendall(frame_size)

        # Send the serialized frame data
        connectionsocket.sendall(serialdata)

        # Check for the 'p' key press to exit the SERVER window
        key = cv2.waitKey(1) & 0xFF
        if key == ord('p'):
            break

    connectionsocket.close()

# Release the video capture and close the SERVER window when the server exits
video.release()
cv2.destroyWindow("SERVER")
