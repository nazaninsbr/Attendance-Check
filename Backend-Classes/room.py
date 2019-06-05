class Room:
    def __init__(self, number):
        self.room_number = number

    def get_room_number(self):
        return self.room_number
    
    def __str__(self):
        return str(self.room_number)