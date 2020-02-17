import sys
import socket

HOST = '127.0.0.1'
PORT = 31000
BUFSIZE = 4096 # max buff size
FILENAME = '' #isi nama file disini

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (HOST, PORT)
print('connecting to ', server_address)
sock.connect(server_address)

try:
    print('sending file: ', FILENAME)
    sock.sendall(FILENAME.encode())

    # Look for the response
    response = sock.recv(BUFSIZE)
    print('response:', response.decode())
    if response.decode() == FILENAME:
        recvfile = open('client_' + FILENAME, 'wb')
        data = sock.recv(BUFSIZE)
        recvfile.write(data)
        recvfile.close()

        print('file successfully received from server..')

finally:
    print('closing socket')
    sock.close()
