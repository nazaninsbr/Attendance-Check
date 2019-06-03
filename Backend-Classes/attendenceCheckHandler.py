from db_handler import DBHandler

class AttendenceCheckHandler:
    def __init__(self):
        self.db_handler = DBHandler()
        self.current_user = None
        self.create_instances()
    
    def create_instances(self):
        self.db_handler.create_instances()

    def login_to_account(self, username, password):
        if self.db_handler.login(username, password):
            self.current_user = self.db_handler.get_curr_user()
            return True
        return False
    
    def check_secter_answer(self, answer):
        return True
    
    def change_password(self, new_password):
        pass
    
    def get_exam_list(self):
        pass
    
    def submit_results(self):
        pass