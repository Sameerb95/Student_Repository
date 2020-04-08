"""This is a unittest file to test all the cases to check all cases works fine and all the exceptions are caught properly"""
import unittest
from HW09_Sameer_Bhute import Repository, Student, Instructor
import os, sys
from prettytable import PrettyTable

class Test_HW09(unittest.TestCase):
    """ TEst_HW09 is to perform all the cases to check if all the errors are handled properly """
    def test_class_student(self):
        """ test_class_student is to test if the values provided to the pretty table are correct or not"""
        stevens: Repository = Repository(r"C:\\Users\\samee\\Desktop\\Second_Sem\\SSW_810\\HW09")
        list1 = list()
        list2 = [['10103', 'Baldwin, C', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687']], ['10115', 'Wyatt, X', ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687']], ['10172', 'Forbes, I', ['SSW 555', 'SSW 567']], ['10175', 'Erickson, D', ['SSW 564', 'SSW 567', 'SSW 687']], ['10183', 'Chapman, O', ['SSW 689']], ['11399', 'Cordova, I', ['SSW 540']], ['11461', 'Wright, U', ['SYS 611', 'SYS 750', 'SYS 800']], ['11658', 'Kelly, P', ['SSW 540']], ['11714', 'Morton, A', ['SYS 611', 'SYS 645']], ['11788', 'Fuller, E', ['SSW 540']]]
        for student in stevens._Student.values():
            list1.append(student.pretty_student())
        
        self.assertEqual(list1, list2)

    def test_class_instructor(self):
        """ test_class_student is to test if the values provided to the pretty table are correct or not """
        stevens: Repository = Repository(r"C:\\Users\\samee\\Desktop\\Second_Sem\\SSW_810\\HW09")
        list1 = list()
        list2 = [['98765', 'Einstein, A', 'SFEN', 'SSW 567', 4], ['98765', 'Einstein, A', 'SFEN', 'SSW 540', 3], ['98764', 'Feynman, R', 'SFEN', 'SSW 564', 3], ['98764', 'Feynman, R', 'SFEN', 'SSW 687', 3], ['98764', 'Feynman, R', 'SFEN', 'CS 501', 1], ['98764', 'Feynman, R', 'SFEN', 'CS 545', 1], ['98763', 'Newton, I', 'SFEN', 'SSW 555', 1], ['98763', 'Newton, I', 'SFEN', 'SSW 689', 1], ['98760', 'Darwin, C', 'SYEN', 'SYS 800', 1], ['98760', 'Darwin, C', 'SYEN', 'SYS 750', 1], ['98760', 'Darwin, C', 'SYEN', 'SYS 611', 2], ['98760', 'Darwin, C', 'SYEN', 'SYS 645', 1]]
        for instructor in stevens._Instructor.values():
            for row in instructor.pretty_instructor():
                list1.append(list(row))

        self.assertEqual(list1, list2)
    
    def test_file_not_found_error(self) -> None:
        """To test if any of the file is not correctly found or the path given isn't correct"""
        with self.assertRaises(FileNotFoundError):
            Repository(r"C:\\Users\\samee\\Desktop\\Second_Sem\\SSW_810\\HW09\\Nofile")

    def test_missing_any_value(self) -> None:
        """To test if there is any missing values in the txt files"""
        with self.assertRaises(ValueError):
            Repository(r"C:\Users\mayur\Desktop\Stevens\Courses\SEMESTER_2\SSW-810\Assignment_9\StevensValueerror")
    
    def test_wrong_number_of_field(self) -> None:
        """To test if there is wrong number of field in the file which doesn't match to the field specified"""
        with self.assertRaises(ValueError):
            Repository(r"C:\Users\mayur\Desktop\Stevens\Courses\SEMESTER_2\SSW-810\Assignment_9\Stevensfields")

    def test_wrong_grade_value(self) -> None:
        """To test if there is grade for an unknown student or instructor """
        with self.assertRaises(ValueError):
            Repository(r"C:\Users\mayur\Desktop\Stevens\Courses\SEMESTER_2\SSW-810\Assignment_9\Stevenswronggrade")

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)

