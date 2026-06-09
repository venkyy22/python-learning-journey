
class FamilyMember:
    def __init__(self,name,role):
        self.name = name
        self.role = role

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self,value):
        allowed = ["grandfather", "grandmother", "father", "mother",
                   "brother", "sister", "cousin", "friends"]
        if value in allowed:
            self._role = value
        else:
            print(f"{value} is not a valid role!")

    def introduce(self,):
        return f"hi i am {self.name} and my role is {self.role} in this family"

class Parent(FamilyMember):
    def assign_chore(self,child_name,task):
        return f"{self.name} assigned {task} to {child_name}"

class Child(FamilyMember):
    def complete_chore(self,task):
        return f"{self.name} completed {task}"

class Senior(FamilyMember):
    def request_remainder(self,task):
        return f"{self.name} is requesting a {task}"


e = FamilyMember("rajesh" , "father")
e.name = "someone else"
e.role = 1225
print(e.role)
print(e.name)

p = Parent("teena" , "sister")
print(p.assign_chore("priya" , "dishes"))

c = Child("priya" , "sister")
print(c.complete_chore("dishes"))

s = Senior("grandmother","grandmother")
print(s.request_remainder("medicine remainder"))
