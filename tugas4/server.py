import socket
import threading
import logging
import time
import sys
import json

from file import File

f = File()

class ProcessTheClient(threading.Thread):
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address
        threading.Thread.__init__(self)

    def run(self):
        raw_data = b''
        msg = ""
        while True:
            data = self.connection.recv(16)
            if data:
                msg = msg + data.decode()

                # Melakukan cek apakah data yang diterima sudah berupa json
                if(self.is_json_instance(msg)):
                    req = json.loads(msg)
                    if req['status'] == 'OK':
                        resp = f.execute_command(header=req['header'], content=req['content'])

                        resp = resp + b'\r\n'
                        self.connection.sendall(resp)
                        if resp == b'upl\r\n':
                            recv_data = self.connection.recv(1024)
                            while(recv_data):
                                raw_data += recv_data
                                recv_data = self.connection.recv(1024)

                            f.upload_file(req['content'], raw_data)
                            raw_data = b''
                        msg = ""
            else:
                msg = ""
                break
        self.connection.close()
    
    def is_json_instance(self, data):
        try:
            json_object = json.loads(data)
            del json_object
        except ValueError as e:
            return False
        return True


class Server(threading.Thread):
    def __init__(self):
        self.the_clients = []
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        threading.Thread.__init__(self)

    def run(self):
        self.my_socket.bind(('0.0.0.0', 5555))
        self.my_socket.listen(1)
        while True:
            self.connection, self.client_address = self.my_socket.accept()
            logging.warning(f"connection from {self.client_address}")

            clt = ProcessTheClient(self.connection, self.client_address)
            clt.start()
            self.the_clients.append(clt)


def main():
    svr = Server()
    svr.start()


if __name__ == "__main__":
    main()
