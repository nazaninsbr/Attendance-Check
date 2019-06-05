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
    
    def authenticate_with_answer(self, username, answer):
        if self.username == username and self.secret_answer == answer:
            return True
        return False
    
    def get_username(self):
        return self.username
    
    def change_password(self, password):
        self.password = password

    def get_info(self):
        return [self.username, self.password, self.secret_answer]
