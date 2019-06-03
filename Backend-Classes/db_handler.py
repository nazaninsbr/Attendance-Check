from local_db import LocalDB

class DBHandler:
    def __init__(self):
        self.get_address = ''
        self.post_address = ''
        self.local = LocalDB()
    
    def write_to_db(self, write_data):
        pass
    
    def read_from_db(self):
        pass