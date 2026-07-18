# Dictionary

# A Python dictionary is a built-in data type used to store data as key-value pairs
# the key is the word
# the value is its meaning
birthday = {
    "virat": "05-11-1988",
    "darshan": "09-08-1980",
}

print(birthday["virat"])  # output: 05-11-1988

# example
karnataka_food = {
    "bengaluru": "dose",
    "mysuru": "mysorepak",
    "mangaluru": "neer dose",
}
print(karnataka_food["mysuru"])  # output: mysorepak


# safe access using dict.get
print(birthday.get("virat"))
print(birthday.get("darshan"))

print(birthday.get("varshan", "Not found"))# output:not found


#additional adding
birthday["sudeep"] = "02-09-1973"
print(birthday)

#updating
birthday["virat"]="05-11-2026"
print(birthday)

print("updating...")
birthday["virat"] = "05-11-1988"
print(birthday)


#removing elements from dictionary
#you can remove items from dictionary
birthday = {
    "virat": "05-11-1988",
    "darshan": "09-08-1980",
}


birthday.pop ("virat")


#dictionary methods

print(birthday.keys()) #dict_keys(['darshan'])


print(birthday.values()) #dict_values(['09-08-1980'])


print(birthday.items()) #dict_items([('darshan', '09-08-1980')])


#update()
    #example

karnataka_food = {
    "bengaluru": "dose",
    "mysuru": "mysorepak",
    "mangaluru": "neer dose",
}
print(karnataka_food["mysuru"]) 

new_dish = {
    "huballi": "Girmit",
}

karnataka_food.update(new_dish)
print(karnataka_food) == {}



#dictionary methods

item1 = {
    "name" : "milk",
    "weight" : 1,
    "price"  : 50  
}

item2 = {
    "name" : "sugar",
    "weight" : 2,
    "price"  : 99.58  
}

item3 = {
    "name" : "cofffe",
    "weight" : 10,
    "price"  : 5000  
}
print(item1)
print(item2)
print(item3)

print(f"Total sum names: {item1['name']} + {item2['name']}+ {item3['name']}")
print(f"Total sum weight: {item1['weight'] + item2['weight']} + {item3['weight']}")
print(f"Total sum price: {item1['price'] + item2['price']}+ {item3['price']}")

