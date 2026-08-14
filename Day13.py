#FUNCTIONS -ADVANCED CONCEPTS


# 1. keyword

def display_info(name,age):
    print (f"Name:{name},Age:{age}")
display_info (age =25, name="varshan")#o/p:Name:varshan,Age:25


#2.variable length argument
#can use *args and **kwargs to accept a variable numbers of arguments in a function

# ex- *args
def total_sum(*numbers):
    result = 0
    for num in numbers:
        result += num
    return result

print(total_sum(5,45,6))#o/p=56



#**kwargs
def student_info(**details):
    for key,value in details.items():
        print(f"{key}:{value}")
student_info(name ="Anand",age =29,course="python")



#LAMBDA FUNCTIONS
#its a small arguments function that can take any numbers of arguments but has only one expression
#def sdd (a,b):
    #return a+b
    
add = lambda a,b :a+b
print(add(9,2))     #O/p:11

double = lambda x :2*x
print(double(200))      #O/p:400


#recursion
#it occurs when a function call itself .it breakdownn into smaller ,similar problems

def factorial(n):
    # handle 0 and 1 as base cases
    if n <= 1:
        return 1
    return n * factorial(n-1)


# call the function (moved outside the function definition)
print(factorial(5))



   # nested function
   #its a  function indside another function
def outer_function(name):
    def inner_function():
        print(f"Hello,{name}!")
        inner_function(0)
