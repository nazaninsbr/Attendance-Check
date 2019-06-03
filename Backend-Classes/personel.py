from person import Person

class Personel(Person):
    def __init__(self):
        self.username = ''
        self.password = ''
    
    def set_user_pass(self, username, password):
        self.username = username
        self.password = password
    
    def change_password(self, password):
        self.password = password
