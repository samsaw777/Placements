class Student:
    schoolNam = "Model English School" # public variable which can be used in all other class.
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    #check if child is adult or not.
    def checkAge(self): # public method which can be used in all other class.
        if self.age > 18:
            print(f"{self.name} is an adult.")
        else:
            print(f"{self.name} is a child.")
        print(f"Printing the global variable {self.schoolNam}")


# Create an object of class Item.
child1 = Student("sameep",20)
child1.checkAge() # calling the public method.

child2 = Student("sameep",10)
child2.schoolNam = "Vidyalankar Polytechnic" # changing the value of public variable.
child2.checkAge()