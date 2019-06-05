import csv
from personel import Personel

class LocalDB:
    def __init__(self):
        self.personel_file = 'personel.csv'

        self.users = []
        self.curr_user = None
    
    def read_from_db(self, path, has_header = True):
        rows = []
        count = 0
        with open(path, newline='\n') as myFile:  
            reader = csv.reader(myFile)
            for row in reader:
                if count ==0 and has_header:
                    count += 1
                else:
                    rows.append(row)
        return rows

    def create_instances(self):
        personel = self.read_from_db(self.personel_file)
        for p in personel:
            self.users.append(Personel(p[0], p[1], p[2]))

    def get_curr_user(self):
        return self.curr_user

    def login(self, username, password):
        for p in self.users:
            if p.authenticate(username, password):
                self.curr_user = p
                return True
        return False
    
    def check_secter_answer(self, username, answer):
        for p in self.users:
            if p.authenticate_with_answer(username, answer):
                self.curr_user = p
                return True
        return False
    
    def change_password(self, username, new_password):
        if self.curr_user.get_username() == username:
            self.curr_user.change_password(new_password)
            self.write_to_db(self.personel_file, self.curr_user.get_info())
        else:
            print('ERROR IN CHANGE PASSWORD!!')
    
    def write_to_db(self, path, write_data):
        with open(path, newline='\n') as myFile: 
            writer = csv.writer(myFile)
            reader = csv.reader(myFile)
            # TODO : Write the password change to the DB

