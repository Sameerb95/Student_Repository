"""This is a unittest file to test all the cases to check all cases works fine and all the exceptions are caught properly"""
import unittest
from Student_Repository_Sameer_Bhute import Repository, Student, Instructor
import os, sys
from prettytable import PrettyTable
import sqlite3

class Test_HW10(unittest.TestCase):
    """ Test_HW10 is to perform all the cases to check if all the errors are handled properly """
    
    def test_class_student(self):
        """ test_class_student is to test if the values provided to the pretty table are correct or not"""
        stevens: Repository = Repository(r"C:\\Users\\samee\\Desktop\\Second_Sem\\SSW_810\\HW11\\Student_Repository")
        list1 = list()
        list2 = [['10103', 'Jobs, S', 'SFEN', ['CS 501', 'SSW 810'], ['SSW 540', 'SSW 555'], [], '3.38'], ['10115', 'Bezos, J', 'SFEN', ['SSW 810'], ['SSW 540', 'SSW 555'], ['CS 501', 'CS 546'], 0.0], ['10183', 'Musk, E', 'SFEN', ['SSW 555', 'SSW 810'], ['SSW 540'], ['CS 501', 'CS 546'], '4.00'], ['11714', 'Gates, B', 'CS', ['CS 546', 'CS 570', 'SSW 810'], [], [], '3.50']]
        for student in stevens._Student.values():
            list1.append(student.pretty_student())
            # print(list1)
        
        self.assertEqual(list1, list2)

    def test_class_instructor(self):
        """ test_class_instructor is to test if the values provided to the pretty table are correct or not """
        stevens: Repository = Repository(r"C:\\Users\\samee\\Desktop\\Second_Sem\\SSW_810\\HW11\\Student_Repository")
        list1 = list()
        list2 = [['98764', 'Cohen, R', 'SFEN', 'CS 546', 1], ['98763', 'Rowland, J', 'SFEN', 'SSW 810', 4], ['98763', 'Rowland, J', 'SFEN', 'SSW 555', 1], ['98762', 'Hawking, S', 'CS', 'CS 501', 1], ['98762', 'Hawking, S', 'CS', 'CS 546', 1], ['98762', 'Hawking, S', 'CS', 'CS 570', 1]]
        for instructor in stevens._Instructor.values():
            for row in instructor.pretty_instructor():
                list1.append(list(row))
     
        self.assertEqual(list1, list2)
    
    def test_class_major(self):
        """ test_class_student is to test if the values provided to the pretty table are correct or not """
        stevens: Repository = Repository(r"C:\\Users\\samee\\Desktop\\Second_Sem\\SSW_810\\HW11\\Student_Repository")
        list1 = list()
        list2 = [['SFEN', ['SSW 540', 'SSW 555', 'SSW 810'], ['CS 501', 'CS 546']], ['CS', ['CS 546', 'CS 570'], ['SSW 565', 'SSW 810']]]
        for major in stevens._Major.values():
            list1.append(major.pretty_major())
        
        self.assertEqual(list1, list2)
    
    def test_class_grade(self):
        db: sqlite3.Connection = sqlite3.connect("C:\\Users\\samee\\Desktop\\Second_Sem\\SSW_810\\HW11\\Student_Repository\\HW11_Tables")
        list1 = list()
        list2 = [('Jobs, S', '10103', 'A-', 'SSW 810', 'Rowland, J'),('Jobs, S', '10103', 'B', 'CS 501', 'Hawking, S'),('Bezos, J', '10115', 'A', 'SSW 810', 'Rowland, J'), ('Bezos, J', '10115', 'F', 'CS 546', 'Hawking, S'),  ('Musk, E', '10183', 'A', 'SSW 555', 'Rowland, J'),  ('Musk, E', '10183', 'A', 'SSW 810', 'Rowland, J'),  ('Gates, B', '11714', 'B-', 'SSW 810', 'Rowland, J'),('Gates, B', '11714', 'A', 'CS 546', 'Cohen, R'),('Gates, B', '11714', 'A-', 'CS 570', 'Hawking, S')]
        for row in db.execute("SELECT (s.Name) as 'Student',(s.CWID) as 'CWID',(g.Grade) as 'Earned_grade',(g.Course) as 'In_Course',(i.Name) as 'Thought_by' from students as s inner join grades as g on s.CWID = g.StudentCWID inner join instructors i on g.InstructorCWID = i.CWID"):
            list1.append(row)
        # print(list1)
        self.assertEqual(list1, list2)
    
    def test_file_not_found_error(self) -> None:
        """To test if any of the file is not correctly found or the path given isn't correct"""
        with self.assertRaises(FileNotFoundError):
            Repository(r"C:\\Users\\samee\\Desktop\\Second_Sem\\SSW_810\\HW09\\Nofile")

        

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)

