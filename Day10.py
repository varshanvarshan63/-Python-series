#for loop
    #used to itterate Over a sequence [list,tuple,string] and execute a block of code repeatedly  for each elements in the sequence

cities = ["New York", "London", "Tokyo", "Mumbai"]

for city in cities:
    print(city)     #o/p



bag = ["red","green","blue"]
for ball in bag :
    print(ball)     #o/p

for i in range (1,11,2):
    print(i,end=" ")    #o/p 1 3 5 7 9 
    print(i)


name ="VARSHAN"
for letters in name :
    print(letters * 6) 


numbers = [ 10, 20, 30]
for index, num in enumerate(numbers):
    print(f"{num} is in {index}th index")

#output:
#10 is in 0th index
#20 is in 1th index
#30 is in 2th index

name = "varshan"
for index, letter in enumerate(name):
    print(letter * (index + 1))


d = {"name":"varshan","age":"22","income":1}
for key, value in d.items():
    print(key, "", value)
#OUTPUT:
#name  varshan
#age  22
#income  1

#[NESTED LOOPS]
for i in range(1,11):
    print(f"2x{i}={2*i}")#o/p:tables of 2x1=2(1,11)


for i in range(2, 11):
    for j in range(1, 11):
        print(f"{i}x{j}={i*j}")#o/p:tables of 2x1=2 to 10x10=100




for i in range (1,6):
    print (i)

items = [0]
terms = [1, 2, 3]
for i in terms:
    print(items)
    items.append(i)