class Person:
    def __init__(self):
        self.first_name = ''
        self.last_name = ''
        self.picture = ''
        self.id_number = ''
    
    def set_info(self, f_name, l_name, id_number, picture = None):
        self.first_name = f_name
        self.last_name = l_name
        self.picture = picture
        self.id_number = id_number
    
    def print_info(self):
        print('Name: '+self.first_name+' '+self.last_name)
        print('ID: ', self.id_number)