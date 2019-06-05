# TODO : add back/return to options on every page
class UserProfilePage:
    def __init__(self, backend_api):
        self.backend_api = backend_api
    
    def show_exam_list(self):
        print('^^ Available Exams ^^')
        ex_li = self.backend_api.get_exam_list()
        for ex_l in ex_li:
            print(ex_l)
        exam_id = input('Please Enter Your Choice (Exam ID): ')
        if self.backend_api.set_curr_exam(exam_id):
            self.print_all_students()
            self.exam_attendance_check_options()
        else:
            print('Invalid exam number.')
            self.show_exam_list()

    def print_all_students(self):
        print('^^ Available Students ^^')
        ids = self.backend_api.get_student_ids()
        for i in ids:
            print(i)
        
    def exam_attendance_check_options(self):
        print('(1) Search for Student')
        print('(2) Home')
        c = input('Please Enter Your Choice (1/2): ')
        if c=='1':
            self.show_search_for_students_page()
        elif c=='2':
            # TODO: should we make curr_offering null again?
            self.show_choices()
    
    def show_search_for_students_page(self):
        student_id = input('Please Enter Your Choice (Student ID): ')
        if self.backend_api.is_student_available(student_id):
            answer = input('Confirm attendance? (y/n)')
            if answer=='y':
                self.backend_api.confirm_attendance(student_id)
            elif answer == 'n':
                pass
            else: 
                print('Invalid choice.')
            self.exam_attendance_check_options()
        else:
            print('Invalid student id.')
            self.exam_attendance_check_options()

    def show_choices(self):
        print('^^ User Profile ^^')
        print('(1) Get Data From Database')
        print('(2) Perform Attendance Check')
        print('(3) Confirm Attendance Check')
        print('(4) Submit Attendance Results')
        print('(5) Logout')
        c = input('Please Enter Your Choice (1/2/3/4/5): ')
        if c=='1':
            self.backend_api.get_data_from_db()
            self.show_choices()
        elif c=='2':
            self.show_exam_list()
        elif c=='3':
            self.confirm_list_page()
        elif c=='4':
            self.backend_api.submit_results()
            self.show_choices()
        elif c=='5':
            print('^^ Bye ^^')
            return
        else:
            self.show_choices()

    def search_for_student_page(self):
        print('^^ Search For Student ^^')

    def confirm_list_page(self):
        print('^^ Confirm List ^^')
