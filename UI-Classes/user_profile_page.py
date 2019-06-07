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
        self.exam_attendance_check_options()
        
    def exam_attendance_check_options(self):
        print('(1) Search for Student')
        print('(2) Show Student List')
        print('(3) Confirm Attendance Check')
        print('(4) Home')
        c = input('Please Enter Your Choice (1/2/3/4): ')
        if c=='1':
            self.show_search_for_students_page()
        elif c=='2':
            self.print_all_students()
        elif c=='3':
            self.confirm_list_page()
        elif c=='4':
            self.backend_api.remove_curr_offering()
            self.show_choices()

    def show_prof_info(self):
        print(self.backend_api.get_offering_prof_info())
    
    def confirm_list_page(self):
        self.show_prof_info()
        if self.backend_api.are_all_studence_checked():
            c = input('Enter Proffesor ID to Confirm: ')
            self.backend_api.prof_confirm()
            self.backend_api.remove_curr_offering()
            self.show_choices()
            print('Successful:)')
        else:
            print('ERROR: there are more students to check before you could finalize list')
            self.exam_attendance_check_options()
    
    def show_search_for_students_page(self):
        student_id = input('Please Enter Your Choice (Student ID): ')
        if self.backend_api.is_student_available(student_id):
            print(self.backend_api.get_student_info(student_id))
            present_or_not = input('Is present? (y/n)')
            if present_or_not=='y':
                self.backend_api.set_present(student_id)
            elif present_or_not == 'n':
                pass
            else: 
                print('Invalid choice.')
                self.exam_attendance_check_options()
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
        print('(3) Submit Attendance Results')
        print('(4) Logout')
        c = input('Please Enter Your Choice (1/2/3/4): ')
        if c=='1':
            self.backend_api.get_data_from_db()
            self.show_choices()
        elif c=='2':
            self.show_exam_list()
        elif c=='3':
            self.backend_api.submit_results()
            self.show_choices()
        elif c=='4':
            self.backend_api.join_all_threads()
            print('^^ Bye ^^')
            exit()
        else:
            self.show_choices()
