#Polymorphism = Same action, different results
# Example: Light switch
#You press the same switch.
#But in one room it turns on a tube light, in another room it turns on a fan.
#Same action → different behavior.

class Human:
    def work(self):
        print("Human is working")

class Student(Human):
    def work(self):
        print("Student is studying")

class Teacher(Human):
    def work(self):
        print("Teacher is teaching")

class Doctor(Human):
    def work(self):
        print("Doctor is treating patients")


if __name__ == "__main__":
    people = [Human(), Student(), Teacher(), Doctor()]
    for p in people:
        p.work()





#ABSTRACTION

#Abstraction = Show only what’s needed 
# Example: ATM machine
#You just press buttons: withdraw, deposit, check balance.
#You don’t need to know how the bank servers or cash dispenser work inside.
#The ATM hides complexity and shows only the important parts.

from abc import ABC, abstractmethod


class Payment(ABC):
    # Abstract method
    @abstractmethod
    def pay(self, amount):
        pass


class CardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Card")


class UpiPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")


# Create objects
card = CardPayment()
upi = UpiPayment()

# Make payments
card.pay(1000)
upi.pay(500)
