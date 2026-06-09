class Hospital:
    count = 0
    def __init__(self,patient_name,age):
        self.patient_name = patient_name
        self.age = age
        Hospital.count += 1

    @classmethod
    def get_count(cls):
        return f"Total patients {cls.count}"

    @classmethod
    def from_string(cls,data):
        patient_name,age = data.split(",")
        return cls(patient_name ,int (age))

    @property
    def patient_name(self):
        return self._patient_name

    @patient_name.setter
    def patient_name(self,value):
        if   isinstance(value,str):
            self._patient_name = value
        else:
            self._patient_name = "unknown"

    @property
    def age (self):
        return self._age

    @age.setter
    def age(self,value):
        if 0 <=  value <= 100:
            self._age = value
            print("valid age")
        else:
            self._age = "unknown"
            print("age is not verified")

a = Hospital("surekha" , 25)
b = Hospital("arjun" , 22)
Hospital = Hospital.from_string("suresh , 45")
print(a.count , a.get_count() , a.age )




