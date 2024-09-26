# TYPECASTING 
amount = 2500.89
print(type(amount))
print(int(amount)) # typecast 
# Convert int to string 
amount = 2599
stringamount = str("2599")
print(stringamount)
string = 'Deepanshu Anand'
# print(int(string)) # string cannot be converted into integer.
# single character can be cvonverted into integer as it does have a ASCII value 
# And hence a string cannot be converted into an integer as string do not have ASCII values.
#TAKING INPUT FROM THE USER: 
myname  = str(input("Enter the name of the student: "))
print("My name is"+  myname)
age = int(input("Enter the age of the student: "))
print("My age is", age)
# the retrun type of input() function is string.
# Find the age in years when bornyear and current year is given by the user.
# Find the currency in rupees to usd(1 usd = 84rs)