from db_handler import DBHandler

class AttendenceCheckHandler:
    def __init__(self):
        self.db_handler = DBHandler()
        self.current_user = None
        self.semester = None
        self.curr_offering = None 
        self.create_instances()
    
    def create_instances(self):
        self.db_handler.create_instances()

    def login_to_account(self, username, password):
        if self.db_handler.login(username, password):
            self.current_user = self.db_handler.get_curr_user()
            return True
        return False
    
    def check_secter_answer(self, username, answer):
        return self.db_handler.check_secter_answer(username, answer)
    
    def change_password(self, username, new_password):
        self.db_handler.change_password(username, new_password)
    
    def get_data_from_db(self):
        self.semester = self.db_handler.get_data_from_db()
    
    def set_curr_exam(self, exam_id):
        status, self.curr_offering = self.semester.get_curr_exam(exam_id)
        return status
    
    def get_student_ids(self):
        return self.curr_offering.get_student_ids()
    
    def get_exam_list(self):
        return self.semester.get_exam_list()
    
    def is_student_available(self, student_id):
        return self.curr_offering.is_student_available(student_id)
    
    def confirm_attendance(self, student_id):
        return self.curr_offering.confirm_attendance(student_id)
    
    def submit_results(self):
        pass