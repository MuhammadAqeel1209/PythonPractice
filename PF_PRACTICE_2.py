"""
------------------------------------AIRTHMETIC EXPRESSION----------------------------------------------
#PROBLEM NO 1 --> Y = 2X + 1
x = int(input("ENTER THE VALUE\t"))
y = 2 * x + 1
print("RESULT\t",y)
--------------------------------------------------------------------

#PROBLEM NO 2 --> Y = (2X + 1)/5
x = int(input("ENTER THE VALUE\t"))
y = (2 * x + 1) /5
print("RESULT\t",y)
--------------------------------------------------------------------

#PROBLEM NO 3 --> Y = 2(2X + 1)/5
x = int(input("ENTER THE VALUE\t"))
y = 2*(2 * x + 1) /5
print("RESULT\t",y)
--------------------------------------------------------------------

#PROBLEM NO 4 --> Q NO 1 --> Y =  {X/3 - (X - 2)/2 = 7/3}
x = int(input("ENTER THE VALUE\t"))
y =  {x/3 - (x - 2)/2}
print("RESULT\t",y)
--------------------------------------------------------------------


#PROBLEM NO 5 --> Q NO 2 --> Y = {(3 - 7x)/(15 + 2x) = 0}

--------------------------------------------------------------------


------------------------------------ QUADRATIC AIRTHMETIC EXPRESSION-------------------------------------

#PROBLEM NO 1 --> Z = x^2 + y^2
x = int(input("ENTER THE VALUE\t"))
y = int(input("ENTER THE VALUE\t"))
z = (x * x) + (y * y)
print("RESULT:\t",z)
--------------------------------------------------------------------

#PROBLEM NO 2 --> c =  x^2 + y^2 + z^3
x = int(input("ENTER THE VALUE\t"))
y = int(input("ENTER THE VALUE\t"))
z = int(input("ENTER THE VALUE\t"))
c = (x * x) + (y * y) + (z * z * z)
print("RESULT:\t",c)
--------------------------------------------------------------------

#PROBLEM NO 3 -->  c = (x^2 + y^2 + z^2)/5
x = int(input("ENTER THE VALUE\t"))
y = int(input("ENTER THE VALUE\t"))
z = int(input("ENTER THE VALUE\t"))
c = ((x * x) + (y * y) + (z * z)) /5
print("RESULT:\t",c)
--------------------------------------------------------------------


#PROBLEM NO 4 --> Q NO 1 --> Y = {(3 - 7x)/(15 + 2x) = 0}

--------------------------------------------------------------------


#PROBLEM NO 5 --> Q NO 2 --> QUADRATIC EQUATION
import math
a = int(input("ENTER THE VALUE\t"))
b = int(input("ENTER THE VALUE\t"))
c = int(input("ENTER THE VALUE\t"))

determinent = (b * b) - (4 * a* c)
sqrtOfDterminent = math.sqrt(determinent)

rootOne = (- b + sqrtOfDterminent) /(2 * a)
rootTwo = (-b - sqrtOfDterminent) /(2 * a)
if(determinent > 0):
    print("FIRST ROOT:\t",rootOne)
    print("SECOND ROOT:\t",rootTwo)

elif(determinent == 0):
    print("FIRST ROOT:\t",rootOne)
    print("SECOND ROOT:\t",rootTwo)

else:
    print("ROOT ARE IMIGINARY") 

--------------------------------------------------------------------
"""