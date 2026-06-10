class Restaurant:
    count = 0
    def __init__(self,name,rating):
        self.name = name
        self.rating = rating
        Restaurant.count +=1

    @classmethod
    def to_count(cls):
        return f"Total restaurants {cls.count}"

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
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self,value):
        if 1<= value <=5:
            self._rating = value
        else:
            self._rating = "unknown"

a = Restaurant("taj" , 5)
b = Restaurant("oberoi" , 4)
print(a.name , a.rating , a.to_count())
print(b.name , b.rating , b.to_count())
