from person import Person

class Student(Person):
    def __init__(self, first, last, id_number):
        super().__init__(first, last, id_number)
    
    def get_id(self):
        return super().get_id()
    
    def __str__(self):
        return super().__str__()