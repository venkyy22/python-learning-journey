class Employee:
    count = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.count +=1

    @classmethod
    def to_count(cls):
        return f"Total employees {cls.count}"

    @classmethod
    def from_string(cls,data):
        name,salary = data.split(",")
        return cls(name,int(salary))

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
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self,value):
        if value > 0:
            self._salary = value
        else:
            self._salary = "unknown"


a = Employee("kumar" ,1500)
b = Employee("vishwas" , 250)
Employee = Employee.from_string("Rahul,5000")
print(Employee.name, Employee.salary)

print(a.name,a.salary,a.to_count())
print(b.name,b.salary,b.to_count())
