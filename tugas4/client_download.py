import socket
import json

from file import File

HOST = '127.0.0.1'
PORT = 5555

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (HOST, PORT)
print('connecting to ', server_address)
sock.connect(server_address)

f = File()

# Input
scan = input()
cstring = scan.split(" ")
try:
    header = cstring[0].strip()
    content = cstring[1].strip()
    message = json.dumps(dict(header=header, content=content, status='OK'))
    print('JSON Data: ')
    print(message)

    sock.sendall(message.encode())

    outputs = b""
    while True:
        response = sock.recv(16)
        outputs += response
        if outputs[-2:] == b'\r\n':
            break

    outputs = outputs[:-2]
    f.save_file(content, 'downloads', outputs)

finally:
    print('Download finished...')
    print('closing socket')
    sock.close()
