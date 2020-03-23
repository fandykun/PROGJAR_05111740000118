from database import Database
import os
import json

class File:
    def __init__(self):
        self.up_dir = 'uploads/'
        self.down_dir = 'downloads/'

    '''
    upload_file: client mengirim file ke server untuk diupload
                hasil file upload disimpan di direktori uploads
    '''
    def upload_file(self, filename: str, raw_data:bytes):
        path = open(self.up_dir + filename, 'wb')

        DB = Database()
        DB.create_data(filename)

        path.write(raw_data)
        path.close()

    '''
    request: client meminta file dari server untuk didownload
                hasil file yang telah didownload disimpan di direktori downloads
    @return: bytes (raw data)
    '''
    def request_file(self, filename: str, dir:str):
        path = open(dir + '/' + filename, 'rb')
        raw_data = path.read()
        path.close()
        return raw_data

    def save_file(self, filename: str, dir:str, raw_data):
        path = open(dir + '/' + filename, 'wb')
        if isinstance(raw_data, bytes):
            path.write(raw_data)
        else:
            path.write(raw_data.encode())
        path.close()

    '''
    execute_command: server mengeksekusi command menyesuaikan perintah dari client
    '''
    def execute_command(self, header:str, content:None):
        try:
            command = header
            print(command)
            if command == 'list':
                result = Database().list_data()
                result = json.dumps(result)
                return result.encode()
            elif command == 'download':
                filename = content
                return self.request_file(filename, 'uploads')
            elif command == 'upload':
                return b"upl"
            else:
                return b"ERRORCMD"
        except:
            return b"ERROR"

if __name__ == "__main__":
    f = File()
    # f.save_file('coba.txt', 'downloads', '12333333'.encode())
    # f.upload_file('loh.txt', 'hi syg'.encode())
    # print(len(f.request_file('dummy.pdf', 'assets')))
    f.execute_command('list', 'test')