import csv
from personel import Personel
from professor import Professor

class LocalDB:
    def __init__(self):
        self.personel_file = 'personel.csv'
        self.professors_file = 'professors.csv'

        self.users = []
        self.professors = []
        self.curr_user = None
    
    def read_csv(self, path, has_header = True):
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
        personel = self.read_csv(self.personel_file)
        for p in personel:
            self.users.append(Personel(p[0], p[1], p[2]))

        profs = self.read_csv(self.professors_file)
        for p in profs:
            self.professors.append(Professor(p[0], p[1]))
    
    def get_curr_user(self):
        return self.curr_user

    def login(self, username, password):
        for p in self.users:
            if p.authenticate(username, password):
                self.curr_user = p
                return True
        return False
    
    def write_to_db(self, write_data):
        pass
    
    def read_from_db(self):
        pass