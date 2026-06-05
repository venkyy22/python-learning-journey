class Mobile:
    company = "samsung"
    def __init__(self,model,price):
        self.model = model
        self.price = price
        print(f"model is {self.model}")

    @classmethod
    def change_company(cls,new_name):
            cls.company = new_name

o1 = Mobile("samsung" , 12100)
o2 = Mobile("galaxy google pixel" , 1200)

Mobile.change_company("apple")

o1.company = "one plus"
print(o1.company)
print(o2.company)
