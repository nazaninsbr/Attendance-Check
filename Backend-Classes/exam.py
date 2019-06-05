class Exam:
    def __init__(self, id, start_at, end_at, room):
        self.id = id
        self.start_at = start_at
        self.end_at = end_at
        self.room = room

    def get_id(self):
        return self.id

    def __str__(self):
        return '-------'+'ID:'+str(self.id)+'-------\n'+' Start:'+self.start_at+' End:'+self.end_at+' Room:'+str(self.room)+'\n--------------------------'