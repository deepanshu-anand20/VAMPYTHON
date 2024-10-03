# # Creating a List, Tuple, Set and Dictionary 
# # Add data Pawan, Manan, Tanya, Mukul
# # Delete pawan
# # Access all data 
# # update Mukul to Deepanshu 
# # print the data 
# # working on list
# # mylist = []
# # mylist.append("Pawan")
# # mylist.append("Manan")
# # mylist.append("Tanya")
# # mylist.append("Mukul")
# # print(mylist)
# # mylist.remove("Pawan")
# # print(mylist)
# # mylist[2] = "Deepanshu"
# # print(mylist)
# # working on tuple 
# mytuple = ("Pawan","Manan","Tanya","Mukul")
# mytuplelist = list(mytuple)
# mytuplelist.remove("Pawan")
# mytuplelist[2]="Deepanshu"
# print(mytuplelist)
# Working on dictionary
mydict = {"Name":"Deepanshu", "Class":"BCA", "Section":"B"}
print(mydict)
mydict["College Name"] = "ITS College"
print(mydict)
mydict.pop("College Name")
print(mydict)
# working on set 
myset = {"Pawan","Tanya","Mukhul"}
myset.remove("Pawan")
myset.add("Pawan")
print(myset)