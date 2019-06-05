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
        self.prof_confirmed = False
        self.posted_to_remote_db = False
    
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
    
    def get_student_info(self, student_id):
         for s in self.students:
            if student_id == str(s.get_id()):
                return str(s)
    
    def confirm_attendance(self, student_id):
        for s in self.students:
            if student_id == str(s.get_id()):
                s.confirm_attendance()
                return 
    
    def are_all_studence_checked(self):
        for s in self.students:
            if not s.is_confirmed():
                return False
        return True
    
    def prof_confirm(self):
        self.prof_confirmed = True

    def get_offering_prof_info(self):
        return str(self.prof)
    
    def set_present(self, student_id):
        for s in self.students:
            if student_id == str(s.get_id()):
                s.set_present()
                return 
