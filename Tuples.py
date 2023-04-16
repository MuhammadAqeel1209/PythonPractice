#TUUPLE CAN NOT CHANGE ABLE
# tup = (1,2,3,4,5,6,7,8,9)
# print(type(tup),tup)

#tupp =(1) #If we have write 1 value python complier consider it "INT"
# print(type(tupp))

#SAME NEAGATIVE AND POSITIVE INDEX IN TUPLE AS SAME AS LISTS
# if 7 in tup:
#     print("YES")


# tup2 = tup[0:5]
# print(tup2)

#-----------------------------------------------------------------------
#First we convert tupple in list then changing in it in list and convert to tupple 
tupple = ("Red","Black","Blue","Yellow","Green")
print(tupple)
temp = list(tupple)
temp.append("Grey")
temp.pop(2)
tupple = tuple(temp)

print(tupple)

#-----------------------------------------------------------------------
#CONCETATION OF TUPPLE

int1Tup =(1,2,3,3,5)
int2Tup = (6,7,8,9,0)

finalTup = int1Tup+int2Tup
print(finalTup)

#-----------------------------------------------------------------------
#COUT METHOD IN TUPPLE
print(int1Tup.count(3))

#-----------------------------------------------------------------------
#INDEX METHOD USED TO TELL THE INDEX OF VALUE
print(int1Tup.index(3))