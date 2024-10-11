import socket
import threading

# Define the phone's IP address (visible in UDP monitor) and port number
phonename = "172.23.16.118"
phonePort = 4000

# Define the PC's IP address (can be seen by typing 'ipconfig' in cmd) and server port
myname = '172.23.6.178'
myPort = 13000

# Create a socket for IPv4 and UDP connection
ChatSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the server port
ChatSocket.bind(('', myPort))

# Print a message to confirm that the system is ready
print("System is ready to send and receive messages.")

# Function for receiving messages from the phone
def recvmessage():
    while True:
        message, sender_address = ChatSocket.recvfrom(2048)
        print("Message received from phone:", message.decode())

# Function for sending messages to the phone
def sendmessage():
    while True:
        message = input("Please type your message: ")
        ChatSocket.sendto(message.encode(), (phonename, phonePort))

# Create a thread for receiving messages
recv_thread = threading.Thread(target=recvmessage)

# Create a thread for sending messages
sendmsg_thread = threading.Thread(target=sendmessage)

# Start the send message thread
sendmsg_thread.start()

# Start the receive message thread
recv_thread.start()

# Wait for both threads to finish
recv_thread.join()
sendmsg_thread.join()
