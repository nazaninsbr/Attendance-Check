import requests

from local_db import LocalDB

from semester import Semester
from room import Room
from course import Course
from professor import Professor
from student import Student

class DBHandler:
    def __init__(self):
        self.db_address = 'http://142.93.134.194:8088/api/attendance'
        self.local = LocalDB()
        # TODO: find a better way or place to save these
        self.rooms = []
        self.courses = []
        self.professors = []
        self.students = []

    def create_instances(self):
        self.local.create_instances()

    def login(self, username, password):
        return self.local.login(username, password)
    
    def get_curr_user(self):
        return self.local.get_curr_user()

    def check_secter_answer(self, username, answer):
        return self.local.check_secter_answer(username, answer)
    
    def change_password(self, username, new_password):
        self.local.change_password(username, new_password)

    def create_all_rooms(self, classes):
        for c in classes:
            room_number = c['room_number']
            matched = False
            for r in self.rooms:
                if room_number == r.get_room_number():
                    matched = True
            if matched == False:
                self.rooms.append(Room(room_number))
    
    def create_all_courses(self, classes):
        for c in classes:
            course_name = c['course_name']
            matched = False
            for co in self.courses:
                if course_name == co.get_course_name():
                    matched = True
            if matched == False:
                self.courses.append(Course(course_name))

    def create_all_profs(self, classes):
        for c in classes:
            professor = c['professor']
            professor_id = professor['id']
            matched = False
            for p in self.professors:
                if professor_id == p.get_id():
                    matched = True
            if matched == False:
                self.professors.append(Professor(professor['first_name'], professor['last_name'], professor['id']))
    
    def create_all_students(self, classes):
        for c in classes:
            for student in c['students']:
                student_id = student['id']
                matched = False
                for s in self.students:
                    if student_id == s.get_id():
                        matched = True
                if matched == False:
                    self.students.append(Student(student['first_name'], student['last_name'], student['id']))
        
    def get_data_from_db(self):
        data = self.read_from_db()
        date = data['date']
        classes = data['classes']

        self.create_all_rooms(classes)
        self.create_all_courses(classes)
        self.create_all_profs(classes)
        self.create_all_students(classes)

        s = Semester(date)
        s.add_classes(classes, self.rooms, self.courses, self.professors, self.students)

        # TODO: add local saving capabilities 

        return s
    
    def write_to_db(self, write_data):
        r = requests.post(url = self.db_address, data=write_data)
        self.isAttendanceSubmitted = True
    
    def read_from_db(self):
        r = requests.get(url = self.db_address)
        data = r.json() 
        return data
