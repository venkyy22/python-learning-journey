class CricketPlayer:
    def __init__(self,name,jersey_number):
        self.jersey_number = jersey_number
        self.name = name

    @classmethod
    def from_string(cls,data):
        name,jersey_number = data.split(",")
        return cls(name,int(jersey_number))

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if isinstance(value,str):
            self._name = value
        else:
            self._name = "invalid"

    @property
    def jersey_number(self):
        return self._jersey_number

    @jersey_number.setter
    def jersey_number(self,value):
        if 1 <= value <= 99:
            self._jersey_number = value
        else:
            self._jersey_number = "unknown"

a = CricketPlayer("virat" ,18)
b = CricketPlayer("mahi" , 7)
CricketPlayer = CricketPlayer.from_string("Rohit,45")
print(a.name,a.jersey_number)
print(b.name,b.jersey_number)
print(CricketPlayer.name , CricketPlayer.jersey_number)
