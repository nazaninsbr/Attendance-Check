from local_db import LocalDB

class DBHandler:
    def __init__(self):
        self.db_address = 'http://142.93.134.194:8088/api/attendance'
        self.local = LocalDB()

    def create_instances(self):
        self.local.create_instances()

    def login(self, username, password):
        return self.local.login(username, password)
    
    def get_curr_user(self):
        return self.local.get_curr_user()
    
    def write_to_db(self, write_data):
        pass
    
    def read_from_db(self):
        pass