"""
# 
# File          : room.py
# Created       : 02/11/21 1:37 PM
# Author        : Ron Greego
# Version       : v1.0.0
# Description   :
#
"""
from annotations.student import Student
from annotations.module import Module


class Room:
    room_number: int

    # initialised a list with type Student
    students: [Student] = []

    def __init__(self, room_num):
        self.room_number = room_num

    def add_students(self, student):
        # add students to class room
        self.students.append(student)

    def display_details(self):
        for student in self.students:
            print("Student ID: {}\nStudent Name: {}"
                  "\nPhone Number: {}\nModule: {}\nRoom {}\n\n".format(student.student_id, student.student_name,
                                                                       student.phone_number, student.module.module_name,
                                                                       self.room_number))


if __name__ == "__main__":
    module = Module('Information Technology')
    stu1 = Student("L00163553", "Jane", 894438804, module)
    stu2 = Student("L00163558", "Jason", 894478804, module)
    room = Room(2409)
    room.add_students(stu1)
    room.add_students(stu2)
    room.display_details()
