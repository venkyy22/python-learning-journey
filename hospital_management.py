from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def get_info(self):
        return f"here is the information"

class Patient(Person):
    def __init__(self,name,age):
        self.name = name
        self.age = age

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
    def age(self):
        return self._age

    @age.setter
    def age(self,value):
        if 10<= value <=100:
            self._age = value
        else:
            self._age = "unknown"

    def get_info(self):
        return f"name is {self._name} and age is {self._age}"

    def to_check(self):
        if self._age >= 60:
            return "critical"
        else:
            return "Not critical"

class Doctor(Person):
    def __init__(self,name,specialization):
        self.name = name
        self.specialization = specialization

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
    def specialization(self):
        return  self._specialization

    @specialization.setter
    def specialization(self,value):
        if isinstance(value,str):
            self._specialization = value
        else:
            self._specialization ="unknown"

    def get_info(self):
        return f"name is {self._name} and specialization is {self._specialization}"

    def assign_specialization(self,new_specialization):
        self._specialization = new_specialization
        return f"{self._name} has specialized in {self._specialization}"

class Hospital:
    count = 0
    def __init__(self,patient,doctor):
        self.patient = patient
        self.doctor = doctor
        self._patient = []
        self._doctor  = []
        Hospital.count += 1

    @property
    def patients(self):
        return self._patient

    @patients.setter
    def patients(self,value):
        if isinstance(value,str):
            self._patient = value
        else:
             self._patient = "unknown"

    @property
    def doctors(self):
        return self._doctor

    @doctors.setter
    def doctors(self,value):
        if isinstance(value,str):
            self._doctor = value
        else:
            self._doctor = "unknown"

    def add_patient(self,name,age):
        p = Patient(name,int(age))
        self._patient.append(p)
        return f"{name} add to hospital"

    def add_doctor(self,name,specialization):
        d = Doctor(name,specialization)
        self._doctor.append(d)
        return f"{name} add to hospital"

    def get_info(self):
        patient_info = [p.get_info() for p in self._patient]
        doctor_info = [d.get_info() for d in self._doctor]
        return f"Patients: {patient_info} \nDoctors: {doctor_info}"

    @classmethod
    def total_hospitals(cls):
        return f"The total hospitals are {cls.count}"

hospital = Hospital("kumar" ,"dr ajay")
print(hospital.add_patient("vikas" ,50))
print(hospital.add_doctor("dr robert" ,"urologist"))
print(hospital.get_info())
print(hospital.total_hospitals())

p = Patient("kishore" , 60)
print(p.get_info())
print(p.to_check())

d = Doctor("dr vijay" , "general physician")
print(d.get_info())
print(d.assign_specialization("gastroentrologist"))

