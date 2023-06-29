"""
#PROBLEM NO 1--> PRINT YOUR NAME
print("MUHAMMAD AQEEL")
--------------------------------------------------------------------

#PROBLEM NO 2 --> SUM TWO NUMBERS
one = 34
two = 23
print("SUM IS\t",one+two)
--------------------------------------------------------------------

#PROBLEM NO 3--> INPUT TWO NUMBER FROM USER AND PERFORM ADDITION
numOne = int(input('enter value for first number\t'))
numTwo = int(input('enter value for second number\t'))
print("SUM IS\t",numOne+numTwo);
--------------------------------------------------------------------

#PROBLEM NO 4 -->EVEN ODD NUMBER
number = int(input("ENTER THE NUMBER FOR EVEN AND ODD:\t"))
if(number%2 == 0):
    print("NUMBER IS EVEN")

else:
    print("NUMBER IS ODD")
--------------------------------------------------------------------

#PROBLEM NO 5 --> CHECK GREATER AND LESSER NUMNER
checkNum = int(input("ENTER THE NUMBER FOR GREATER AND SMALLER:\t"))
if(checkNum > 10):
    print("NUMBER IS GREATER THEN 10")
    
else:
    print("NUMBER IS SMALLER THAN 10")
--------------------------------------------------------------------

#PROBLEM NO 6 --> CALCULATE THE GRADE
obtainedMarks = float(input("ENTER THE OBTAINED MARKS:\t"))
totalMarks = float(input("ENTER THE TOTAL MARKS:\t"))
percentage = (obtainedMarks / totalMarks) * 100

if(percentage >= 90 and percentage <= 100):
    print("A")

elif(percentage >= 80 and percentage < 90 ):
    print("B")

elif(percentage >=70 and percentage < 80):
    print("C")

else:
    print("F")
--------------------------------------------------------------------    

#PROBLEM NO 7 --> WRITE A TABLE WITH WHILE LOOP
number = int(input("ENTER THE NUMBER FOR TABLE\t"))
limit = int(input("ENTER THE LIMIT OF TABLE:\t"))
multilyer = 1

while(multilyer <= limit ):
    print(number,"X",multilyer,"=",multilyer*number)
    multilyer = multilyer + 1
--------------------------------------------------------------------

#PROBLEM NO 8 --> WRITE A TABLE WITH FOR LOOP
number = int(input("ENTER THE NUMBER FOR TABLE\t"))
limit = int(input("ENTER THE LIMIT OF TABLE:\t"))
multilyer = 1

for i in range(multilyer,limit+1):
    print(number,"X",multilyer,"=",multilyer*number)
    multilyer = multilyer + 1
--------------------------------------------------------------------
   
#PROBLEM NO 9 --> SUM OF SUM 15 NUMBER
sum = 0   
for i in range(1,16):
    sum = i + sum

    print(sum)
--------------------------------------------------------------------
  
 #PROBLEM NO 10 --> FIND EQUAL GREATER OR SMALLER    
numOne = int(input('enter value for first number\t'))
numTwo = int(input('enter value for second number\t'))
if(numOne == numTwo):
    print("BOTH NUMBER ARE EQUAL")

elif(numOne > numTwo):
    print(numOne," IS GREATER THAN",numTwo)

else:
    print(numOne," IS SMALLER THAN",numTwo)
  
--------------------------------------------------------------------

#PROBLEM NO 11 --> ADD TWO NUMBER WITH DEFIND DATA TYPE
num1 = 1.5
num2 = 6.3
print("SUM OF", num1,"AND",num2, "IS:\t",float(num1)+float(num2))
--------------------------------------------------------------------


#PROBLEM NO 12 --> TAKING INPUT FROM USER ADD TWO NUMBER WITH DEFIND DATA TYPE
no1 = input("ENTER THE NUMBER:\t")
no2 = input("ENTER THE NUMBER:\t")
print("SUM OF", no1,"AND",no2, "IS:\t",float(no1)+float(no2))
--------------------------------------------------------------------


#PROBLEM NO 13 --> LCM OF TWO NUMBER(NOT PROPER UNDERSTAND)
import math

def lcm(a, b):
     #return(a * b)
    return math.gcd(a, b)

number1 = 54
number2 = 24

print("LCM OF ",number1, "AND",number2,"IS:\t",lcm(number1,number2))    
--------------------------------------------------------------------

#PROBLEM NO 13 --> USING FUNCTION
def Add(x,y):   
    return x + y

def Subtract(x,y):
    return x - y

def Multiply(x,y):
    return x * y

def Divide (x,y):
    return x / y

print("1 FOR ADDITION");
print("2 FOR SUBTARCTION");
print("3 FOR MULTIPLICATION");
print("4 FOR DIVISION");

choice = int(input("ENTER YOU CHOICE\t"));

if choice == 1:
    one = int(input('enter value for first number\t'))
    two = int(input('enter value for second number\t'))
    print(one, "+",two, "IS = \t" , Add(one, two))

elif choice == 2:
    one = int(input('enter value for first number\t'))
    two = int(input('enter value for second number\t'))
    print(one, "-",two, "IS = \t" , Subtract(one, two))

elif choice == 3:
    one = int(input('enter value for first number\t'))
    two = int(input('enter value for second number\t'))
    print(one, "*",two, "IS = \t" , Multiply(one, two))

elif choice == 4:
    one = int(input('enter value for first number\t')) 
    two = int(input('enter value for second number\t'))
    print(one, "/",two, "IS = \t" , Divide(one, two))  

else:
    print("PLZ ENTER CORRECT CHOICE")    
--------------------------------------------------------------------
    """