# lets first talk about variables in a class.
# variables in a class are for 2 types: 1. Instance variables 2. Class variables.

class Student:
    # First we will create class variables.
    """ 
    Class variables are variables that are shared among all the objects of a class
    and are same for all the instances.
    """
    schoolName = "Model English School"

    # Constructor
    def __init__(self, name, age, rollNo):
        # Instance variables.
        """
        Instance variables are variables that are specific to each object.
        They are created when an object is created.
        They are different for all objects.
        """
        self.name = name
        self.age = age
        self.rollNo = rollNo

    def display(self):
        return self.name + self.age + self.rollNo + self.schoolName


# Now we will create an object of the class.
student1 = Student("John", "20", "10")
print(student1.display())

# Now let change the class variable.
student1.schoolName = "Vidyalankar Polytechnic" # So by using the instance we cannot change the class variable.
print(Student.schoolName)
Student.schoolName = "Vidyalankar Polytechnic"
print(student1.schoolName)
print(Student.schoolName)

Student.name = "Sameep" # this create a class variable and does not change the instance variable.
print(student1.name)
print(Student.name)




"""
     Class variables can only be changed using the class name and not by any instance.
     But it can be accessed by the INSTANCE.
"""

# Let's look into the methods.
# Methods are of 3 types. 1. Instance methods 2. Class methods 3. Static methods.

class Item:
    itemType = "Electronics" # This is a class variable.

    # Constructor is also a instance method.
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # Instance method which is specific to each object and has a self parameter.
    def display(self):
        return self.name + self.price

    # Class method which is specific to the class and has cls parameter.
    # Class method always need @classmethod to be called.
    @classmethod
    def displayItemType(cls):
        return cls.itemType

    #Static method is a method which is not specific to any object or class.
    @staticmethod
    def displayItemTypeStatic():
        return "Static method"

item = Item("Laptop", "Rs. 5000")
print(item.display())
print(item.displayItemType()) 
print(Item.displayItemType())

print(item.displayItemTypeStatic())
print(Item.displayItemTypeStatic())