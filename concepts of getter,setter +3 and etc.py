#1. Getter and Setter Methods
#A getter is a method used to read/access the value of a private variable.
#In Python, private variables are commonly written using __

class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks


student = Student("Varshan", 85)

print(student.get_marks())



#2. Setter Methods
#setters are methods used to set or update the value of a private variable.

class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks")


student = Student("Varshan", 85)

print(student.get_marks())

student.set_marks(95)

print(student.get_marks())



#3. Method Overloading
#Overloading means having multiple methods with the same name but different parameters.
class Calculator:

    def add(self, a, b=0, c=0):
        return a + b + c


calc = Calculator()

print(calc.add(10, 20))
print(calc.add(10, 20, 30))

#4. Method Overriding
#overloading is not natively supported in Python, but we can achieve similar functionality using default arguments or variable-length arguments.
class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")

class cat(Animal):

    def sound(self):
        print("cat meows")

animal = Animal()
dog = Dog()
cat = cat()

animal.sound()
dog.sound()
cat.sound()



#5.Abstract Classes
#Abstract classes are classes that cannot be instantiated and are meant to be subclassed. They can contain abstract methods that must be implemented by their subclasses.
from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CardPayment(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using Card")


class UpiPayment(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using UPI")


card = CardPayment()
upi = UpiPayment()

card.pay(1000)
upi.pay(500)