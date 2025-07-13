#Receiving user input

#Ask their user for their current age
current_age = input("How old are you?")

#Convert the input from string to integer
current_age = int(current_age)

#Add 27 years to get the age in 2050 (Current year is assumed to be 2023)
age_in_2050 = current_age + 27

#Final output
print(f"In 2050, you will be {age_in_2050} years old.")