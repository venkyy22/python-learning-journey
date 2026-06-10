
class Library:
    def __init__(self,title,pages):
        self.title = title
        self.pages = pages

    @classmethod
    def from_string(cls,data):
        title,pages = data.split(",")
        return cls(title,int(pages))

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self,value):
        if isinstance(value,str):
            self._title = value
        else:
            self._title = "unknown"

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self,value):
        if 1<= value <= 2000:
            self._pages = value
        else:
            self._pages = "unknown"

a = Library("think and rich ", 200)
b = Library("steal like an artist" , 350)
Library = Library.from_string("harry potter,500")
print(a.title , a.pages,)
print(b.title,b.pages)
print(Library.title , Library.pages )
