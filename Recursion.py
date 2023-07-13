#RECURSION the function which call at its own function

def Factorial(n):
    if(n == 0 or n == 1):
        return 1
    else:
      return  n * Factorial(n-1)
       

# print(Factorial(5))
# print(Factorial(6))
# print(Factorial(7))


# for i in range(6):
#     print(i)

# --> TYPES OF RECURSION
#   1) Direct 
#       i) tail -->ii) read
#   2) Indirect

# def tail(n):
#     if n ==0 :
#         return
#     print(n)
#     tail(n - 1)

# tail(6)

# def head(n):
#     if(n > 0):
#         head(n-1)
#         print(n,end=" ")

# head(5)

# def funA(n):
#    if(n > 0):
#       print(n,end=" ")
#       funB(n+1)

# def funB(n):
#    if(n > 1):
#       print(n,end=" ")
#       funA(n-5)

# funA(20)
      

# --> Fibonacci Series
f0 = 0
f1 = 1
f2 = f0 + f1

def f(n):
    if(n == 0):
        return 0
    elif(n == 1 or n == 2):
        return 1
    else:    
        return f(n-1) + f(n-2)
# print(f(3))  

# --> Fibonacci Series --> Next Method
# numOne = 0
# numTwo = 1
# print(numOne)
# print(numTwo)
# for i in range(10):
#     result = numOne + numTwo
#     print(result)
#     numOne = numTwo
#     numTwo = result

# --> Prime Number 
number = int(input("Enter the number\t"))
flag = False
for i in range(2,int(1 + number/2)):
    if(number % i) == 0:
        flag = True
        break

if flag == False:
    print(number, " is prime number")
else:
    print(number, "is not prime number")    