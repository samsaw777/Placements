class Student:
    __name = None
    __age = None
    __rollno = None

    def __init__(self,name,age,rollno):
        self.__name = name
        self.__age = age
        self.__rollno = rollno
    

    def __display(self):
        print(f"Name: {self.__name}")
        print(f"Age: {self.__age}")
        print(f"Rollno: {self.__rollno}")
    
    def display(self):
        self.__display()


stud1 = Student("sameep",20,21)
# stud1.__display() # cannot call this method as it is private.
stud1.display()


class Item:
    name = None

    def display(self):
        print(f"Name: {self.name}")


item1 = Item()

item1.display()
item1.name = "Sameep"
item1.display()