# data Type is used to define the data in which form 
# int data type is used to store the numeric data type.
# Note:- In python we don't need to declare the data types.
# We just assign the value in variable.
# Variable can store any type of value with any type of data.
age = 18
name = "Deepanshu Anand" 
salary = 6700
# how to pass a variable inside the print statement .  
# print("My name is"+ name + "and age"+ age)
# It generates the type error reason : string only concatenates with string only.
# solution 1 : replace  + by , where data type is not string.  
print("My Name is " + name , "And Age ", age, "And Salary ", salary)
# solution 2 : pass the variables in print statement with f()
print(f"My Name is {name} Salary is {salary} and Age is {age}")
# solution 3 : typecast the data into string. 
salarystring = string(salary)
agestring = string(age)
print("My Name is "+ name + "And Age "+ agestring + "And Salary " + salarystring)
# To find the type of data we use the type() function: 
print(type(name))
print(type(age))
print(type(salary))
