from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def get_info(self):
        return "Get the information"

class Student(Person):
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if isinstance(value,str):
            self._name = value
        else:
            self._name = "unknown"

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self,value):
        if 0 <= value <=100:
            self._grade = value
        else:
            self._grade = "unknown"

    def get_info(self):
        return f"name: {self._name} , grade: {self._grade}"

    def pass_or_fail(self):
        if self._grade >= 40:
            return "pass"
        else:
            return "fail"


class Teacher(Person):
    def __init__(self,name,subject):
        self.name = name
        self.subject = subject

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if isinstance(value,str):
            self._name = value
        else:
            self._name = "unknown"

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self,value):
        if isinstance(value,str):
            self._subject = value
        else:
            self._subject = "unknown"

    def get_info(self):
        return f"Teacher name is {self._name} , subject he teaches is {self._subject}"

    def assign_subject(self,new_subject):
        self._subject = new_subject
        return f"{self._name} now teaches {self._subject}"


class School:
    count = 0
    def __init__(self,school_name,total_students):
        self.school_name = school_name
        self.total_students = total_students
        self.students = []
        self.teachers = []
        School.count += 1

    @property
    def school_name(self):
        return self._school_name

    @school_name.setter
    def school_name(self,value):
        if isinstance(value,str):
            self._school_name = value
        else:
            self._school_name = "unknown"

    @property
    def total_students(self):
        return self._total_students

    @total_students.setter
    def total_students(self,value):
        if 1<= value <= 5000:
            self._total_students = value
        else:
            self._total_students = "unknown"

    def add_student(self,name,grade):
        s = Student(name,grade)
        self.students.append(s)
        return f"{name} add to school"

    def add_teacher(self,name,subject):
        t = Teacher(name,subject)
        self.teachers.append(t)
        return f"{name} add to school"

    def get_info(self):
        return f"The school name is {self._school_name} , and total students are: {self._total_students}"


    @classmethod
    def total_schools(cls):
        return f"Total schools are: {cls.count}"

s = Student("kumar" ,25)
print(s.get_info())
print(s.pass_or_fail())

school = School("oxford" ,500)
print(school.add_student("priya", 25))
print(school.add_teacher("virat","maths"))
print(school.total_schools())
print(school.get_info())
print(school.total_students)

t = Teacher("vishwas","science")
print(t.get_info())
print(t.assign_subject("physics"))




