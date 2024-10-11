import socket

# Define the server's port as 12000
serverPort = 12000

# Create a server socket using IPv4 and UDP (User Datagram Protocol)
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the server socket to the specified port
# The socket can receive data from all network addresses on this port
serverSocket.bind(("", serverPort))

# Print a message to indicate that the server is ready to receive messages
print("The server is ready to receive messages.")

while True:
    # Receive a message and the client's address using the recvfrom function
    message, clientAddress = serverSocket.recvfrom(2048)

    # Print the received message and the client's address
    print("Received message from client:", message)
    print("Client's address:", clientAddress)

    # Convert the received message to uppercase
    modifiedMessage = message.upper()

    # Send the modified message back to the client using the server's socket
    serverSocket.sendto(modifiedMessage, clientAddress)
