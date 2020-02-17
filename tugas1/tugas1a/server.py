import sys
import socket


HOST = '127.0.0.1'
PORT = 31000
BUFSIZE = 4096

filename_recv = None
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
    while True:
        if not filename_recv:
            filename_recv = connection.recv(BUFSIZE)
            print('received :', filename_recv)
            print('sending data filename to the client')
            connection.sendall(filename_recv)
        else:
            data = connection.recv(BUFSIZE)
            recv_file = open( 'receive_'+ filename_recv.decode(), 'wb')
            if not data:
                recv_file.close()
                break
            recv_file.write(data)
            recv_file.close()

            connection.sendall(b'GOT FILE')
            status_file = True
            break
    # Clean up the connection
    connection.close()