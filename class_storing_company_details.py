class Programmer:
    company = "apple"
    def __init__(self , name , salary , age):
        self.name = name
        self.salary = 120000
        self.age = 30

d = Programmer("kumar" , 120000 , 30)
print(d.name , d.age , d.salary , d.company)

r = Programmer("ram" , 120000 , 30)
print(r.name , r.age , r.salary , r.company)
