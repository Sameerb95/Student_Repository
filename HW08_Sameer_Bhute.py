from datetime import datetime, timedelta,date
from typing import Tuple,Iterator
from prettytable import PrettyTable
import os


def date_arithmetic() -> Tuple[datetime, datetime, int]:
    """ returns date three days after Feb 27, 2000, Feb 27, 2017 and number of days between Feb,1 2019 and Sept 30, 2019 """

    three_days_after_02272000: datetime =  datetime.strptime('Feb 27, 2020', "%b %d, %Y") + timedelta(days = 3) 
    three_days_after_02272017: datetime =  datetime.strptime('Feb 27, 2019', "%b %d, %Y")+ timedelta(days = 3) 
    days_passed_01012017_10312017: int = (datetime.strptime('Sep 30, 2019', "%b %d, %Y") - datetime.strptime('Feb 1, 2019', "%b %d, %Y")).days


    return three_days_after_02272000, three_days_after_02272017, days_passed_01012017_10312017

def file_reader(path, fields, sep=',', header=False) -> Iterator[Tuple[str]]:

    """returns a tuple containing values which are separated by either a comma(,) or a pipe(|)"""

    lineCount = 1
    try:
        fp: IO = open(path,'r')
    except FileNotFoundError:
        raise FileNotFoundError(f'Cannot open the file in the path {path}')

    else:
        with fp:
            if header:
                next(fp)

            for line in fp:
                values = line.rstrip('\n').split(sep)

                if len(values) != fields:
                    raise ValueError(f'{os.path.basename(path)} has  {len(values)} fields on line {lineCount} but excepted {fields}')

                lineCount +=1
                yield tuple(values)


class FileAnalyzer:
    """ This class contains functions which takes directory path as input and anlayze the directory to find .py python file
        and count the function,class,lines and character"""

    def __init__(self, directory: str) -> None:
        """ The intialize function which accepts path and create the file summary dictonary and calls the analyze_file function"""

        self.directory: str = directory 
        self.files_summary: Dict[str, Dict[str, int]] = dict() 
        self.analyze_files() 

    def analyze_files(self) -> None:
        """ This function opens .py python files and analyzes python files to count the functions,classes,lines and characters in the file"""
        try:
            directory: [str] = os.listdir(self.directory)    
        except FileNotFoundError:
            raise FileNotFoundError('Directory you are trying to open does not exist')
        else:
            for file in directory:
                if file.endswith(".py"):
                    self.files_summary[file]={}
                    try:
                        fp:IO = open(os.path.join(self.directory,file),'r')
                    except FileNotFoundError:
                        raise FileNotFoundError('File you are trying to open does not exist')
                    else:
                        with fp:
                            self.files_summary[file]['line'] = sum(1 for line in fp)
                            defCount = 0
                            classCount = 0
                            fp.seek(0)
                            data = fp.read()
                            characters = len(data)
                            fp.seek(0)
                            for line in fp:
                                line = line.strip('\n')
                                wordslist = line.split()

                                if 'def' in wordslist and line.endswith(':'):
                                    defCount = defCount + 1
                                if 'class' in wordslist and line.endswith(':'):
                                    classCount = classCount + 1

                            self.files_summary[file]['function'] = defCount
                            self.files_summary[file]['class'] = classCount
                            self.files_summary[file]['char'] = characters


    def pretty_print(self) -> None:
        """ prints the file name, class count, function count, no of lines and no of characters in each py file"""

        pt:PrettyTable = PrettyTable()
        pt.field_names: list = [
            "File Name",
            "Classes",
            "Functions",
            "Lines",
            "Characters"]

        for k1, v1 in self.files_summary.items():
            l = list()
            l.append(k1)
            l.append(v1['class'])
            l.append(v1['function'])
            l.append(v1['line'])
            l.append(v1['char'])
            pt.add_row(l)

        return pt


# print(date_arithmetic())
# path = "C:\\Users\\samee\\Desktop\\Second_Sem\\SSW_810\\HW05\\HW08_test.txt"
# for cwid, name, major in file_reader(path, 3, sep='|', header=True):  
    # print(f"cwid: {cwid} name: {name} major: {major}") 

# o = FileAnalyzer('C:\\Users\\samee\\Desktop\\Second_Sem\\SSW_810\\HW07')
# o.analyze_files()
# print(o.pretty_print())

