import shelve
import uuid
import os
import json

class Database:
    def __init__(self):
        self.data = shelve.open('database.dat')
        self.dir = 'uploads/'
        self.generate_data()

    def create_data(self, filename: str):
        if self.dir + filename is None:
            return False

        if self.is_data_exist(filename):
            return False

        data_id = str(uuid.uuid4())
        data_name = filename
        _, data_extension = os.path.splitext(self.dir + filename)
        data_size = os.path.getsize(self.dir + filename)
        data_all = {
            'id': data_id,
            'name': data_name,
            'extension': data_extension,
            'size': data_size
        }

        self.data[data_id] = data_all

    def list_data(self):
        result = [self.data[i] for i in self.data.keys()]
        return result

    def is_data_exist(self, filename: str):
        for i in self.data.keys():
            if self.data[i]['name'] == filename:
                return True
        
        return False

    '''
    generate_data() : generate all data(file) from uploads directory
                      and save it metadata to database
    '''
    def generate_data(self):
        datas = os.listdir(self.dir)
        for data in datas:
            self.create_data(data)

if __name__ == "__main__":
    DB = Database()
    DB.generate_data()
    print(json.dumps(DB.list_data()))