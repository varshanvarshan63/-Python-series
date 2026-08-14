#Encapsulation
#Encapsulation means wrapping data (variables) and methods (functions) together inside a class and controlling access to them.
#It hides the internal details and only exposes what’s necessary.

class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    def get_details(self):
        return f"Name: {self.__name}, Marks: {self.__marks}"

    def set_marks(self, marks):
        if marks >= 0:
            self.__marks = marks
        else:
            print("Invalid marks!")


student1 = Student("Varshan", 85)

print(student1.get_details())

student1.set_marks(95)

print(student1.get_details())

student1.set_marks(-10)


print ("inheritance")
#Inheritance
#Inheritance is about reusing code by letting one class derive from another.
#The child class inherits properties and methods of the parent class.

class Animal:
    def speak(self):
        print("This animal makes a sound")


class Dog(Animal):
    def speak(self):
        print("Woof! Woof!")


class Cat(Animal):
    def speak(self):
        print("Meow!")


dog = Dog()
cat = Cat()

dog.speak()
cat.speak()