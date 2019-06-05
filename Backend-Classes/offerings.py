from course import Course
from exam import Exam
from room import Room
from student_exam import StudentExamInfo

class Offering:
    def __init__(self, course, prof):
        self.course = course
        self.exam = None
        self.prof = prof
        self.students = []
    
    def find_student_based_on_id(self, students, _id):
        for s in students:
            if _id == s.get_id():
                return s
    
    def add_information(self, info, r, students):
        self.exam = Exam(info['exam_id'], info['start_at'], info['end_at'], r)
        for s in info['students']:
            stu = self.find_student_based_on_id(students, s['id'])
            self.students.append(StudentExamInfo(stu, s['chair_number']))

    def get_exam_info(self):
        return str(self.exam)
    
    def get_exam_id(self):
        return str(self.exam.get_id())
    
    def get_student_ids(self):
        ids = []
        for s in self.students:
            ids.append(str(s))
        return ids
    
    def is_student_available(self, student_id):
        for s in self.students:
            if student_id == str(s.get_id()):
                return True
        return False
    
    def confirm_attendance(self, student_id):
        for s in self.students:
            if student_id == str(s.get_id()):
                s.confirm_attendance()
                return 
