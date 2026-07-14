age = input("Age:") #input
print("Your age is:", age)



name=input("Enter your name:")#input
age =int(input("Enter your age:"))


boy_name=input(" boy's name:")#output
girl_name=input(" girl's name:")#output
print("Boy's name is:", boy_name)
print("Girl's name is:", girl_name)

#formated string
boy_name=input("Boy's name:")
boy_age = int(input("Boy's age:"))
girl_name=input("Girl's name:")
girl_age = int(input("Girl's age:"))#int() converts string to integer  #string formatting
print(f"Boy's name is {boy_name}, Boy's age is {boy_age}, and Girl's name is {girl_name} and Girl's age is {girl_age}")

age_diff = abs(boy_age - girl_age)#abs= absolute value
print(f"{boy_name} loves {girl_name}. The age difference is {age_diff}.")


#COMMENTS
# This program takes input for two people's names and ages, then calculates and displays the age difference.

#single line comment
# This is a single line comment
print("This is a single line comment example.")


#multi-line comment
# This is a multi-line comment example.
# """ or '''
print("This is a multi-line comment example.")
