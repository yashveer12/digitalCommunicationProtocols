import socket
import cv2
import pickle
import struct

servername = 'localhost'
serverPort = 20000

# Create a socket for the client using TCP
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Now we do a 3 Way Handshake
clientsocket.connect((servername, serverPort))

# Open the CLIENT window
cv2.namedWindow("CLIENT")

while True:
    try:
        # Receive the frame size as a packed struct
        frame_size_data = clientsocket.recv(struct.calcsize("!L"))
        if not frame_size_data:
            break
        frame_size = struct.unpack("!L", frame_size_data)[0]

        # Receive the serialized frame data
        frame_data = b""
        while len(frame_data) < frame_size:
            packet = clientsocket.recv(frame_size - len(frame_data))
            if not packet:
                break
            frame_data += packet

        # Deserialize the frame
        frame = pickle.loads(frame_data)

        # Display the received frame
        cv2.imshow("CLIENT", frame)

        # Check for the 'p' key press to exit the CLIENT window
        key = cv2.waitKey(1) & 0xFF
        if key == ord('p'):
            break

    except Exception as e:
        print(f"Error: {str(e)}")
        break

# Clean up and close the OpenCV window
cv2.destroyWindow("CLIENT")
clientsocket.close()
