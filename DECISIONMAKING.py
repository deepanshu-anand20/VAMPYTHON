#  Program to check whether a person is eligible for voting or not.
age = int(input("Enter your age: "))
# if age > 18 :
#    print(" You are eligible for voting. ")
# else :
#    print("You are not eligible for voting.")   
# Program to check whether a person is eligible for vote and super vote.
#  For Super Vote the user should be above 55 years of age.
if age > 18 and age < 55 :
    print("You are eligible for voting.")
elif age > 55 :
    print("You are eligible for super vote.")
else :
    print("You are not eligible either for voting or super voting.")         
