import socket

# Define the server's hostname or IP address
serverName = 'localhost'  # Example: 'localhost' or '173.17.54.213'

# Define the server's port number
serverPort = 12000

# Create a client socket with IPv4 and UDP (User Datagram Protocol)
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Prompt the user to input a lowercase sentence
message = input('Please enter a lowercase sentence:\n')

# Encode the string message into a stream of bytes using message.encode()
# Send it to the destination server by specifying its address and port number
clientSocket.sendto(message.encode(), (serverName, serverPort))

# Receive the response message, up to 2048 bytes, from the client socket
# The received message is stored in the modifiedMessage variable
# The serverAddress tuple stores two pieces of information: serverName and serverPort
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

# Print the modified message received from the server
print(modifiedMessage)

# Close the clientSocket
clientSocket.close()
