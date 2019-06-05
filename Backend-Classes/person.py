class Person:
    def __init__(self, first_name, last_name, id_number):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number
    
    def __str__(self):
        return 'Name: '+self.first_name+' '+self.last_name+' ID: '+str(self.id_number)

    def get_id(self):
        return self.id_number