from person import Person

class Professor(Person):
    def __init__(self, first, last, id_number):
        super().__init__(first, last, id_number)
    
    def get_id(self):
        return super().get_id()