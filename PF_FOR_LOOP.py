"""
#PROBLEM NO 1


for i in range(1,6):
    for j in range(0,i):
        print("*",end= "")
    print()


#PROBLEM NO 2
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end = "")
    print()      
    

#PROBLEM NO 3
for i in range(1,6):
    for k in range (i,5):
        print(" ",end = "")
    for j in range(0,i):
        print("*",end = "")
    print()
   

#PROBLEM NO 4
for i in range(1,11):
    #range(start,end,jump/step)
    for j in range(10,i,-1):
        print("*",end= "")
    print()

#PROBLEM NO 5
for i in range(1,11):
    for k in range(0,i):
        print(" ",end = "")
    for j in range(10,i,-1):
        print("*",end = "")
    print()  
  

 #PROBLEM NO 6
value = 9
for i in range(1,6):
    for j in range(1,i):
        print(" ", end = "")
    for k in range (0,value):
        print("*",end = "")
    print()   
    value = value - 2  


#PROBLEM NO 8
value = 9
for i in range(1,6):
    for j in range(0,i):
        print(" ",end = "")
    for k in range(1,value + 1):
        print(k,end = "")
    print()
    value = value - 2        
      """           