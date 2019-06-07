import requests
import json 
from multiprocessing import Process
import time

from local_db import LocalDB

from semester import Semester
from room import Room
from course import Course
from professor import Professor
from student import Student

from urllib.request import urlopen

def internet_on():
    try:
        urlopen('http://216.58.192.142', timeout=1)
        return True
    except Exception as e: 
        return False

class DBHandler:
    def __init__(self):
        self.db_address = 'http://142.93.134.194:8088/api/attendance'
        self.local = LocalDB()
        self.rooms = []
        self.courses = []
        self.professors = []
        self.students = []
        self.processes = []

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
        
        with open(DB_FilePath, mode='w') as myFile:
            employee_writer = csv.writer(myFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            # employee_writer.writerow(['John Smith', 'Accounting', 'November'])
            for x in xrange(0, len(classes)):
                employee_writer.writerow([classes[x], date])

        return s
    
    def post_all_present_data(self, all_data_to_post):
        p = Process(target=self.post_all_present_data_using_process, args=(all_data_to_post, ))
        self.processes.append(p)
        p.start()

    def join_all_threads(self):
        print(self.processes)
        print('^^ Joining all processes ^^')
        for p in self.processes:
            p.join()

    def post_all_present_data_using_process(self, all_data_to_post):
        print('** Submitting Data in the Background **')
        count = 0
        while not internet_on():
            count += 1

        while not len(all_data_to_post)==0:
            all_data_to_retry = []
            for d in all_data_to_post:
                result = self.write_to_db(d)
                if not result:
                    all_data_to_retry.append(d)
            all_data_to_post = all_data_to_retry

    def write_to_db(self, write_data):
        write_data = json.dumps(write_data)
        headers = {
            'Content-Type': "application/json"
        }
        r = requests.post(url = self.db_address, data=write_data,headers=headers)
        if r.json()['status']==200:
            print('** Successful Post **')
            return True
        return False
            
            
    def read_from_db(self):
        r = requests.get(url = self.db_address)
        data = r.json() 
        return data
