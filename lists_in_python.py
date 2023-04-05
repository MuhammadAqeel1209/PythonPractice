#LISTS ARE THE COLLECTION OF ITEMS OF DIFFERENT DATA TYPE
# THEY USED TO STORE MULTIPLE ITEM IN SINGLE VARAIBLE

# lists = [1,2,3,4,5,6,7,8,9,10,"Muhammad","Aqeel"]
# # print(lists)
# # print(type(lists))
# #range(start,end,jump/step)
# print(lists[0:8:2])

# color = ["Red","Blue","Green","Yellow"]
#       [0,     1,      2,      3] Positive index
#       [-4,     -3,     -2,      -1] Negative index
# print(color)
# print(color[0])
# print(color[3])

# #negative index
# print(color[-2])

# if "Black" in color:
#     print("Yes")
# else:
#     print("No")  

# if "ll" in "Yellow":
#     print("YES")
# else:
#     print("NO")

#-----------------------------------------------------------------------
#                           LIST COMPREHESION

# lst = [i for i in range(12)]
# print(lst)

# names = ["Ahmed","Aqeel","Ali","Faheem","Ijaz","Rizwan","Ehtsham","Faran","Owais","Hadeed"]
# lsts = [item for item in names]
# print(lsts,"\n")

# names = ["Ahmed","Aqeel","Ali","Faheem","Ijaz","Rizwan","Ehtsham","Faran","Owais","Hadeed"]
# lsts = [item for item in names if  "A" in item]
# print(lsts)

# names = ["Ahmed","Aqeel","Ali","Faheem","Ijaz","Rizwan","Ehtsham","Faran","Owais","Hadeed"]
# lists = [item for item in names if  (len(item) < 4)]
# print(lists)


#-----------------------------------------------------------------------
#                          METHOD OF LIST
listsInt = [11,2,34,4,565,65,4,67,9]
# print(listsInt)
listsInt.remove(565)
print(listsInt)

#-----------------------------------------------------------------------
#      APPEND USED TO ADD SOME NEW OBJECT
# listsInt.append(10)
# print(listsInt)

#-----------------------------------------------------------------------
#      SORT USED TO SORT THE LIST
# listsInt.sort()
# print(listsInt)

#-----------------------------------------------------------------------
#      REVERSE USED TO REVERSE THE LIST
# listsInt.sort(reverse=True)
# listsInt.reverse()
# print(listsInt)

#-----------------------------------------------------------------------
#    INDEX METHOD USED TO TELL THE INDEX OF VALUE
# print(listsInt.index(11))

#-----------------------------------------------------------------------
#COUNT METHOD IS USED TO COUNT THE VALUE IN LIST
# print(listsInt.count((4)))

#-----------------------------------------------------------------------
#COPY METHOD IS USED TO COPY THE METHOD
# newLists = listsInt.copy()
# print(newLists)


#-----------------------------------------------------------------------
#INSERT METHOD USED TO INSER THE VALUE
#listname.indexMethod(indexvalue,valueinlist)
# listsInt.insert(2, 1000)
# print(listsInt)


#-----------------------------------------------------------------------
#EXTEND METHOD USED TO EXTEND THE ONE LIST WITH THE HELP OF OTHER LIST
secondList = [1200,3455,34678,90000]
# listsInt.extend(secondList)

# print(listsInt)

# finalList = listsInt + secondList
# print(finalList)
secondList.clear()
print(secondList)

list1 =[]

for i in range(0,10):
    data = int(input("Enter the number\t"))
    list1.append(data)

print(list1)
    

