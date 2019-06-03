from sys import path 
from constants import BACKEND_CODES

from login_page import LoginPage
from user_profile_page import UserProfilePage

path.append(BACKEND_CODES)
from attendenceCheckHandler import AttendenceCheckHandler

class UI: 
    def __init__(self):
        self.backend_api = AttendenceCheckHandler()
        self.login_page = LoginPage(self.backend_api)
        self.profile_page = UserProfilePage(self.backend_api)

    def start(self):
        if self.login_page.login():
            self.profile_page.show_choices()
        else:
            exit()