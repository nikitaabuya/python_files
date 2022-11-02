#input in python
#python uses the function input () to capture and store

print("Your Profile Application")

first_name = input("First Name:")
last_name = input("Last Name:")
occupation = input("Occupation:")

print("Your first name is:" + first_name)
print("Your last name is:" + last_name)
print("Your job is:" + occupation)


# print("Your last name is: " + last_name)
# print("Your job is: " + occupation)

#another way of outputting information in python in is through
print (f"Your first name is {first_name} and your job is {occupation}")

#handlng non-string input
age = int (input("Please enter your age: "))
print (f" In two years, your age will be {age+2} ")