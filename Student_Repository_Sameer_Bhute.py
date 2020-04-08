from HW08_Sameer_Bhute import file_reader
import os 
from collections import defaultdict
from prettytable import PrettyTable
from typing import DefaultDict,Dict,Tuple,Iterator,List

class Student:
    """ Contains the info of the student and stores the information present in the file"""

    def __init__(self,cwid:str ,name:str ,major:str):
        self._cwid: str = cwid
        self._name: str = name
        self._major: str = major
        self._summary_st: Dict[str,str] = dict()

    def student_course(self, course: str, grade: str):
        self._summary_st[course] = grade
    
    def pretty_student(self) -> Tuple[str,str,List[str]]:

        # print(self._cwid, self._name, sorted(self._summary_st.keys()))
        return[self._cwid, self._name, sorted(self._summary_st.keys())]
    
    # def calculate_grade(self):
        
    #     for x in self._summary_st:


class Instructor:
        """ Contains the info of the Instructor and stores the information present in the file"""

        def __init__(self,cwid:str , name:str, dept:str) -> None:
            self._cwid: str = cwid
            self._name: str = name
            self._dept: str = dept
            # self.summary: DefaultDict = defaultdict()
            self._students: DefaultDict[str,int] = defaultdict(int)
            # self.gradeslist_in:DefaultDict= defaultdict(str)

        def add_student(self, course:str) -> None:  
            self._students[course] +=1
        
        def pretty_instructor(self) -> Iterator[Tuple[str,str,str,str,int]]:

            for course,count in self._students.items():
                yield self._cwid,self._name,self._dept,course,count 


class Repository:
    """ Repository class which contins the info of student and grades"""

    def __init__(self,directory:str):
        self.directory: str = directory
        self._Student: Dict[str,Student] = dict()
        self._Instructor: Dict[str,Instructor] = dict()

        try:
            self._get_students(os.path.join(directory,'students.txt'))
            self._get_instructor(os.path.join(directory,'instructors.txt'))
            self._get_grades(os.path.join(directory,'grades.txt'))
        except ValueError as ve:
            print("The specified field doesn't match with file")
        except FileNotFoundError as fn:
            raise FileNotFoundError
        
    def _get_students(self,directory: str) -> None:

        for cwid,name,major in file_reader(directory,3,sep='\t',header=False):
            self._Student[cwid] = Student(cwid,name,major)
    
    def _get_instructor(self,directory: str) -> None:

        for cwid,name,dept in file_reader(directory,3,sep='\t',header=False):
            self._Instructor[cwid] = Instructor(cwid,name,dept)
    
    def _get_grades(self,directory: str) -> None:

        for st_cwid,course,grade,ins_cwid in file_reader(directory,4,sep='\t',header=False):
            if st_cwid in self._Student:
                self._Student[st_cwid].student_course(course,grade)
            else:
                print(f"Found grade for unknown student '{st_cwid}'")
            if ins_cwid in self._Instructor:
                self._Instructor[ins_cwid].add_student(course)
            else:
                print(f"Found grade for unknown instructor'{ins_cwid}'")
    
    def pretty_print_st(self):
        """Prints the summary of the instructor and grades file by the field 'CWID','Name','Course' and 'No of student' """

        pt_student: PrettyTable = PrettyTable()
        pt_student.field_names = [
            "CWID",
            "Name",
            "Completed Course",
        ]

        # print(self.summary)
        for student in self._Student.values():
            pt_student.add_row(student.pretty_student())

        print('\n')
        print("Student Summary")
        print(pt_student)

    def pretty_print_ins(self):
        """Prints the summary of the instructor and grades file by the field 'CWID','Name','Course' and 'No of student' """

        pt_instructor: PrettyTable = PrettyTable()
        pt_instructor.field_names = [
            "CWID",
            "Name",
            "Dept",
            "Course",
            "Students"
        ]

        # print(self.summary)
        for instructor in self._Instructor.values():
            for row in instructor.pretty_instructor():
                pt_instructor.add_row(row)

        print('\n')
        print("Instructor Summary")
        print(pt_instructor)

if __name__ == '__main__':
    r = Repository('C:\\Users\\samee\\Desktop\\Second_Sem\\SSW_810\\HW09')
    # r.Student.pretty_print()
    r.pretty_print_st()
    r.pretty_print_ins()

 