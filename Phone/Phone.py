class Phone:
    count = 0
    def __init__(self,brand,battery):
        self.brand = brand
        self.battery = battery
        Phone.count += 1

    @classmethod
    def total_count(cls):
        return f"Total phones created {cls.count}"

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self,value):
        if  isinstance(value,str):
            self._brand = value
        else:
            self._brand = "unknown"

    @property
    def battery(self):
        return self._battery

    @battery.setter
    def battery(self,value):
        if 0<= value <= 100:
            self._battery = value
        else:
            self._battery = "unknown"

a = Phone("apple" , 100)
b = Phone("samsung" , 25)
print(a.brand , a.battery ,a.total_count())
print(b.brand , b.battery ,b.total_count())
