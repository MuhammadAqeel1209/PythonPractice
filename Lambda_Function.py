# def double(num):
#     return num * 2

#lambda argument : expression -->Syntax Of Lambda
double = lambda x : x * 2 #-->Lambda KeyWord that make Function 
cube = lambda x : x * x * x #--> Lambda (arguments) : Expression -->Syntax Of Lambda
avg = lambda x,y : (x+y)/2
print(double(5))    
print(cube(5))
print(avg(4,6))

def appl(fx,value):
    return 6 + fx(value)
#   (appl(fx(Lambda), 2(Value)))
print(appl(lambda x:x * x, 2))
store = lambda x:x * x + 6
print(store(2)) #--> 2 is value of arguemmts in lambda (x)

#-----> Input By User ----> 
import math as m
data = int(input("Enter the value:\t"))
value = int(input("Enter the value:\t"))
Ans = lambda data,value : m.sqrt(data * value)
print(Ans(data,value))