from offerings import Offering

class Semester:
    def __init__(self, date):
        self.date = date
        self.offerings = []
    
    def find_room_based_on_number(self, rooms, room_number):
        for r in rooms:
            if room_number == r.get_room_number():
                return r
    
    def find_course_based_on_course_name(self, courses, course_name):
        for c in courses:
            if course_name == c.get_course_name():
                return c
    
    def find_professor_based_on_id(self, professors, _id):
        for p in professors:
            if _id == p.get_id():
                return p

    def add_classes(self, classes, rooms, courses, professors, students):
        for c in classes:
            co = self.find_course_based_on_course_name(courses, c['course_name'])
            r = self.find_room_based_on_number(rooms, c['room_number'])
            p = self.find_professor_based_on_id(professors, c['professor']['id'])
            o = Offering(co, p)
            o.add_information(c, r, students)
            self.offerings.append(o)
    
    def get_exam_list(self):
        ex_li = []
        for o in self.offerings:
            ex_li.append(o.get_exam_info())
        return ex_li
    
    def get_curr_exam(self, exam_id):
        for o in self.offerings:
            if exam_id == o.get_exam_id():
                return True, o
        return False, None
