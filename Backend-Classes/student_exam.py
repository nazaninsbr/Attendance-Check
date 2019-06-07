class StudentExamInfo:
    def __init__(self, student, chair_no):
        self.student = student
        self.chair_no = chair_no
        self.present = False
        self.status = False
    
    def __str__(self):
        return '* Chair Number: '+str(self.chair_no)+' '+str(self.student)+' Attendance Checked? '+str(self.status)+' Present? '+str(self.present)
    
    def get_id(self):
        return self.student.get_id()
    
    def confirm_attendance(self):
        self.status = True
    
    def set_present(self):
        self.present = True

    def is_confirmed(self):
        return self.status
    
    def is_present(self):
        return self.present