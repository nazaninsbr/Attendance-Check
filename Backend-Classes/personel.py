from person import Person

class Personel(Person):
    def __init__(self, username, password, secret_answer):
        self.username = username
        self.password = password
        self.secret_answer = secret_answer
    
    def authenticate(self, username, password):
        if self.username == username and self.password == password:
            return True
        return False
    
    def set_user_pass(self, username, password):
        self.username = username
        self.password = password
    
    def change_password(self, password):
        self.password = password
