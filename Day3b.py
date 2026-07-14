#string manupulation
#string are immutable in python


first_name="Varshan"
last_name="gowda"
full_name=first_name+ " " +last_name
print(full_name)

#repetition of string
#example HELLO

print("HELLO!" * 3)
message="HELLO!"
print(message.lower())
print(message.upper())

print(message.strip())# removes whitespace from the beginning and end of the string

print(message.replace("HELLO","WARNING"))#REPLACE HELLO WITH WARNING

print(len(message))#used to know length


#accesing string character
name = "chandan"
print(name[2])#accessing 3rd character c=0 h=1 a=2 n=3 d=4 a=5 n=6 etc

#string slicing
name = "chandan"
print(name[2:5])#accessing characters from index 2 to 4

#from backward
name = "chandan"
print(name[-2])#accessing 2nd character from the end

#cutting string 
name = "chandan \n is a good boy"   #\n is used to print in new line
print(name)                       

name = "chandan \t is a good boy"      #\t is used to print in tab space
print(name)  