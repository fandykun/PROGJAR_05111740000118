import sys
import socket

HOST = '192.168.100.25'
PORT = 31003
BUFSIZE = 4096 # max buff size
FILENAME = 'client.py' #isi nama file disini

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (HOST, PORT)
print('connecting to ', server_address)
sock.connect(server_address)

try:
    # Open file
    sendfile = open(FILENAME, 'rb')
    bytes = sendfile.read()

    print('sending file: ', FILENAME)
    sock.sendall(FILENAME.encode())

    # Look for the response
    response = sock.recv(BUFSIZE)
    print('response:', response.decode())
    if response.decode() == FILENAME:
        sock.sendall(bytes)
        # print(bytes)
        # Check what server send
        answer = sock.recv(BUFSIZE)
        # print('answer: ', answer)
        if answer == b'GOT FILE':
            print('file successfully send to server..')

    sendfile.close()

finally:
    print('closing socket')
    sock.close()
