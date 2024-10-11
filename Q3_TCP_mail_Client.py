import socket
import base64
from email.mime.text import MIMEText
import os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# SMTP server settings
smtp_server = 'mmtp.iitk.ac.in'
smtp_port = 25

# Your email credentials
sender_email = input('Please enter your email id: ')
password = input('Enter your password: ')

# Recipient email addresses
recipient_email = input('Enter the recipient email id: ')
bcc_email = input('Enter bcc email id: ')

# Email details
subject = input('Please enter the subject of the mail: ')
message = input('Please input the message to be sent: ')

# Path to the file you want to attach
attachment_path = "D:\IIT-K_Courses\Semester-5\EE-673\image.png"

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((smtp_server, smtp_port))
server_response = client_socket.recv(1024).decode()

# Observing server status
print(server_response)

# Send HELO command for initial communication in SMTP
client_socket.send(b'HELO ' + socket.gethostname().encode() + b'\r\n')
server_response = client_socket.recv(1024).decode()
print(server_response)

# Login using your credentials in SMTP
client_socket.send(b'AUTH LOGIN\r\n')
server_response = client_socket.recv(1024).decode()
print(server_response)

# Send your email and password in base64 encoding
client_socket.send(base64.b64encode(sender_email.encode()) + b'\r\n')
client_socket.send(base64.b64encode(password.encode()) + b'\r\n')

# Compose and send the email
email_data = """\
MAIL FROM: <{}>\r\n""".format(sender_email)
client_socket.send(email_data.encode())

email_data = """\
RCPT TO: <{}>\r\n""".format(recipient_email)
client_socket.send(email_data.encode())

email_data = """\
RCPT TO: <{}>\r\n""".format(bcc_email)
client_socket.send(email_data.encode())

email_data = 'DATA\r\n'
client_socket.send(email_data.encode())

# Compose the email message with attachment using MIME
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Bcc'] = bcc_email
msg['Subject'] = subject

msg.attach(MIMEText(message, 'html'))

# Attach the file
attachment = open(attachment_path, "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % os.path.basename(attachment_path))
msg.attach(part)

email_message = msg.as_string()

# Send the email message
client_socket.send(email_message.encode())

# Send the terminating dot
client_socket.send(b'\r\n.\r\n')

# Quit the session
client_socket.send(b'QUIT\r\n')
server_response = client_socket.recv(1024).decode()
print(server_response)

# Close the socket
client_socket.close()

