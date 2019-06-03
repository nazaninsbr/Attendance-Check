class UserProfilePage:
    def __init__(self, backend_api):
        self.backend_api = backend_api
    
    def show_choices(self):
        print('^^ User Profile ^^')
        print('(1) Get Exam List')
        print('(2) Perform Attendance Check')
        print('(3) Confirm Attendance Check List')
        print('(4) Submit Attendance Results')
        print('(5) Logout')
        c = input('Please Enter Your Choice (1/2/3/4/5): ')
        if c=='1':
            self.backend_api.get_exam_list()
        elif c=='2':
            self.search_for_student_page()
        elif c=='3':
            self.confirm_list_page()
        elif c=='4':
            self.backend_api.submit_results()
        elif c=='5':
            return
        else:
            self.show_choices()

    def search_for_student_page(self):
        print('^^ Search For Student ^^')

    def confirm_list_page(self):
        print('^^ Confirm List ^^')
