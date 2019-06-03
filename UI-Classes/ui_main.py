from sys import path 
from constants import BACKEND_CODES

from login_page import LoginPage

path.append(BACKEND_CODES)
from attendenceCheckHandler import AttendenceCheckHandler

class UI: 
    def __init__(self):
        self.backend_api = AttendenceCheckHandler()

    def start(self):
        if LoginPage(self.backend_api).login():
            pass
        else:
            exit()