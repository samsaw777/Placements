class Student:

    # declaring protected variable which can be accessed by it's immediate class.
    _name = None
    _age = None
    _rollno = None

    def __init__(self,name,age,rollno):
        self._name = name
        self._age = age
        self._rollno = rollno
    
    # creating private method
    def _displayInformation(self):
        print(f"Name: {self._name}")
        print(f"Age: {self._age}")
        print(f"Rollno: {self._rollno}")


class Child(Student):
    def __init__(self,name,age,rollno):
        Student.__init__(self,name,age,rollno)

    
    def _displayInformation(self):
        Student._displayInformation(self)
    
    def display(self):
        self._displayInformation()
        print("Child class")


class Item:
    def __init__(self):
        child2 = Student("Rohan",22,1)
        child2._displayInformation()




child1 = Child("Sameep",20,21)
child1.display()
child1._displayInformation()

item1 = Item()