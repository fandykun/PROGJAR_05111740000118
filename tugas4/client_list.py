import socket
import json
import pandas as pd

HOST = '127.0.0.1'
PORT = 5555

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (HOST, PORT)
print('connecting to ', server_address)
sock.connect(server_address)

# Input
scan = input()

try:
    message = json.dumps(dict(header=scan, content='empty', status='OK'))
    print('JSON Data: ')
    print(message)

    sock.sendall(message.encode())

    outputs = ""
    while True:
        response = sock.recv(16)
        outputs += response.decode()
        if outputs[-2:] == '\r\n':
            break

    outputs = outputs[:-2]
    outputs = json.loads(outputs)
    print(pd.DataFrame.from_dict(outputs))

finally:
    print('upload finished...')
    print('closing socket')
    sock.close()
