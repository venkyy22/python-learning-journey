class School:
    count = 0
    def __init__(self,school_name,total_students):
        self.school_name = school_name
        self.total_students = total_students
        School.count += 1

    @classmethod
    def to_count(cls):
        return f"Total schools created {cls.count}"

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
        if  1 <= value <=5000:
            self._total_students = value
        else:
            self._total_students = 0

    def school_size(self):
        if self._total_students < 500:
            return "small school"
        else:
            return "large school"

a = School("oxford" , 33)
b = School("howard" , 55)
a.school_size()
print(a.school_name , a.total_students,a.to_count(),a.school_size())
print(b.school_name , b.total_students,b.to_count(),b.school_size())
