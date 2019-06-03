from person import Person

class Professor(Person):
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def set_user_pass(self, username, password):
        self.username = username
        self.password = password
