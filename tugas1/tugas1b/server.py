import sys
import socket
import os

HOST = '127.0.0.1'
PORT = 31000
BUFSIZE = 4096

status_file = False
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = (HOST, PORT)
print('starting up on ', server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while not status_file:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    print('connection from ', client_address)

    # Receive the data in small chunks and retransmit it
    data = connection.recv(BUFSIZE)
    print('received :', data)

    connection.sendall(data)
    filename_recv = data.decode()

    if os.path.exists(filename_recv):
        send_file = open(filename_recv, 'rb')
        bytes = send_file.read()

        send_file.close()
        connection.sendall(bytes)

    # Clean up the connection
    connection.close()