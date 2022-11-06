#declare and initialize a list
fruits = ["Orange", "Peach", "Banana", "Mango", "Plum"]
print(fruits)

#loop through entire list of fruits
for fruit in fruits:
    print(fruit)

# retrieve list items
print(f"The fruit at position 1: {fruits[0]}")
print(f"The fruit at index 1: {fruits[1]}")

#check length of the list
print(f"The fruit basket currently has {len(fruits)} fruits")

# add something to the list
fruits.append("Lemon")
print(fruits)

#check length of the list
print(f"the fruit basket currently has {len(fruits)} fruits ")

#add a list item to a specific position in the list
fruits.insert(2, "Apple")
print(fruits)