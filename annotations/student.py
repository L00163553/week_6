"""
#
# File          : student.py
# Created       : 01/11/21 11:13 AM
# Author        : Ron Greego
# Version       : v1.0.0
# Description   :
#
"""
from annotations.module import Module


class Student:
    """student class where student details are included"""

    student_id: str
    student_name: str
    module: Module

    def __init__(self, stu_id, name, ph_num: int, mod):
        self.student_id = stu_id
        self.student_name = name
        self.phone_number = ph_num
        self.module = mod





