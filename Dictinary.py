#-------------DICTIONARIES------------
"""
dic = {
    Key    : Value
    "NAME" :"AQEEL",
    "WHO"  :"HUMAN BEING"
}

print(dic["NAME"])
"""

rollno = {
    1195 : "Ubaid",
    1196 : "Hanan",
    1197 : "Rafay",
    1198 : "Rafay Mueid", 
    1199 :"Mani",
    1200 : "Doger"
}

rollno2 = {
    1201:"Rehman",
    1202:"Abu Bakar",
    1203:"Ahmed"
}


print(rollno[1199]) #if no exist value in dictionary error exist

print(rollno.get(1201)) #if no exist value in dictionary display none

#-------------ACCESS ALL KEYS-------------
print(rollno.keys())
print(rollno.values())

for data in rollno.keys():
    # print(rollno[data])
    print(f"The data {rollno[data]} corresponding to {data}")

"""
#--------------------------------------METHODS--------------------------------------
#1)--------------------UPDATE -------------------------

rollno.update(rollno2)
print(rollno)

#2)--------------------CLEAR -------------------------
rollno2.clear()
print(rollno2.values())


#3)--------------------POP(REMOVE SOME VALUES)-------------------------
rollno.pop(1199)
print(rollno)


#4)--------------------POP ITEM(REMOVE LAST VALUES)-------------------------
rollno.popitem()
print(rollno)


#5)--------------------DEL KEYWORD-------------------------
del rollno2
print(rollno2)
"""

Student_Marks = {
    "Aqeel":90,
    "Ehtsham":80,
    "Faran":70,
    "Ahsan":60,
    "Ahmed" : 50,
    "Ali":40
}

Student_Grade = {}
for std in Student_Marks:
    marks = Student_Marks[std] 
    if(marks >= 90):
        Student_Grade[std] = "A+"
    elif(marks >= 80):
        Student_Grade[std] = "A"
    elif(marks >= 70):
        Student_Grade[std] = "B"
    elif(marks >= 60):
        Student_Grade[std] = "C"
    elif(marks >= 50):
        Student_Grade[std] = "D"
    else:
        Student_Grade[std] = "F"           

print(Student_Grade)