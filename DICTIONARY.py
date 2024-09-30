# Dictionary : It can store the data in key value pair.
# Information about a particular person.
# eg:- name : Deepanshu 
# Ordered . 
# No duplicate. 
# changeable.
myInfo = { "Name" : "Deepanshu Anand",
           "Email" : "d@gmail.com", 
           "Mobile" : "9354788705",
           "Age" : "18" } 
# to access specific data from a dictionary.
print(myInfo["Mobile"])
# syntax : dict_name["key"]
print("My Name is : " , myInfo["Name"])
print("My Age is : " , myInfo["Age"])
print("My Mobile is : ", myInfo["Mobile"])
# Access the complete dictionary key value.
for value in myInfo.values() :
    print(value)
for key in myInfo.keys() :
    print(key)
# Modifying and adding the data in a dictionary. 
myInfo["Name"] = "Deepanshu Anand"
myInfo["Age"] = "19"
myInfo["Email"] = "deep@gmail.com"
myInfo["Mobile"] = "9856475323"
print(myInfo)
myInfo["College_Name"] = "ITS COLLEGE"
print(myInfo)
# using update function 
myInfo.update({ "Gender" : "Male" })
print(myInfo)
# Deleting the data 
myInfo.pop("Gender")
print(myInfo)
del myInfo["Email"]
print(myInfo)