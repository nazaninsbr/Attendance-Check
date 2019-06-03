class LoginPage:
    def __init__(self, backend_api):
        self.backend_api = backend_api
    
    def show_login_error(self):
        print('* Incorrect username or password *')
        self.login_choices()
    
    def login_choices(self):
        print('(1) Login')
        print('(2) Forgot Password')
        print('(3) Exit')
        c = input('Please Enter Your Choice (1/2/3): ')
        if c=='1':
            self.login()
        elif c=='2':
            self.forgot_password_page()
        elif c=='3':
            return False
        else:
            self.login_choices()
        
    def forgot_password_page(self):
        print('^^ Forgot Password ^^')
        answer = input('Please Enter Your Secret Answer: ')
        if self.backend_api.check_secter_answer(answer):
            new_password = input('New Password: ')
            self.backend_api.change_password(new_password)
            self.login()
        else:
            pass

    def login(self):
        print('^^ Login ^^')
        username = input('Username: ')
        password = input('Password: ')
        if self.backend_api.login_to_account(username, password):
            return True
        else:
            self.show_login_error()
    