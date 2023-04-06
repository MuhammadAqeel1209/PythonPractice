def cube(x):
    return x *x *x   

#-->WithOuT  Map -->👇
list1 = [1,2,4,6,4,3]
list2 = []

for i in list1:
    list2.append(cube(i))
print(list2) 

#------------------------------------------------------------------------------------------
#-----> Map ----->
#Synatx of Map --> Map(Function Name as arguemnts,Iteration) 👈
# 👇 --> Map --> 👉 It allows you to process and transform all the items in an iterable without using an explicit for loop, a technique commonly known as mapping
newlist = list(map(cube,list1)) #Map--> Higher Order Function(when one function take other function as arguments)
print(newlist)

#--> Map The Function --> Using lambda Function 👇
newlist = list(map(lambda x: x * x * x,list1)) # using lambda function
print(newlist)

#------------------------------------------------------------------------------------------
#-----> Filter the Function ----->
#Syntax Of Filter --> Filter(Function as arguemnts,Iteration) 👈
# 👇 --> Filter --> 👉 This new iterator can filter out certain specific elements based on the condition that you provide very efficiently 
def FilterFunction(num):
   return num > 1
filterList =list(filter(FilterFunction, list1))
print(filterList)

#filter(function, iterable) --> using Lambda👇
filterList =list(filter(lambda x: x > 4, list1)) # using lambda function
print(filterList)

#------------------------------------------------------------------------------------------
#-----> Reduce The Function ----->
from functools import reduce

#Synatx od Reduce --> reduce(function, sequence, initial) 👈
#👇 --> Reduce --> 👉 it is to take an existing function, apply it cumulatively to all the items in an iterable, and generate a single final value

number = [1,2,3,4,5]
sum = reduce(lambda x ,y: x + y,number) 
#----> 👇 Working of reduce Function 👇 ---->
#Step 1 --> 1 + 2 = 3 --> List are [3,3,4,5]
#Step 2 --> 3 + 3 = 6 --> list are[6,4,5]
#Step 3 --> 6 + 4 = 10 --> list are [10,5]
#Step 4 --> 10 + 5 = 15 --> Function Reduce
print(sum)

data = [100,200,300,400,500]
multiply = reduce(lambda a,b: a * b, data)
print(multiply)