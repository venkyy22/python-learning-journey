
class Student:
    count = 0

    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
        Student.count += 1

    @classmethod
    def get_count(cls):
        return f" The total number of students created: {Student.count}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if isinstance(value , str):
            self._name = value
        else:
            self._name = "unknown"

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self,value):
        if 0 <= value <= 100:
            self._grade = value
        else:
            self._grade = "unknown"

a = Student("suraj"  , 75)
b = Student("ashish" , 25)
c = Student("venkatesh" , 100)
d = Student("sumeeth" , 10)
print(a.name , a.grade ,a.get_count())
