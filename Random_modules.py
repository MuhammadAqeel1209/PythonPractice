import random
num = random.random()  
print(num)  
print("-------------------------------------------")

"""Generate Random Integers -->The random.randint() function generates a random integer 
from the range of numbers supplied."""
for i in range(1,11):
    num = random.randint(1, 500)  #--> Print number in between 1 - 500
    print( num )  
print("-------------------------------------------")

"""Generate Random Numbers within a Defined Range -->The random.randrange() function selects 
an item randomly from the given range defined by the start, the stop, and
the step parameters. By default, the start is set to 0.
Likewise, the step is set to 1 by default. """

for i in range(1,11):  
    num = random.randrange(1, 10) #in this Function Default Step is set Which is "1" 
    print( num )  
print("-------------------------------------------")

#num = random.randrange(start,stop,step)
for i in range(1,11):  
    num = random.randrange(1, 10,2) # -->All number is odd due to start "1" and increment "2" --> 1,3,5,7 etc 
    print( num )              
print("-------------------------------------------")

for i in range(1,11):  
    num = random.randrange(0, 101, 10) #All the number display after the jump of "10" number like -->"in for of mutiplr of 10" 
    print( num )   
print("-------------------------------------------")

"""Select Random Elements-->The random.choice() function selects an item
from a non-empty series at random. An IndexError is thrown when the parameter
is an empty series.""" 
for i in range(1,4):
    random_l = random.choice([23, 54, 765, 23, 45, 45]) #a list  
    print( random_l )  
print("-------------------------------------------")

for i in range(1,4):    
    random_s = random.choice((12, 64, 23, 54, 34)) #a set  
    print( random_s )  
print("-------------------------------------------")

"""Shuffle Elements Randomly-->A general sequence, like integers or floating-point series,
can be a group of things like a List / Set. The random module contains methods
that we can use to add randomization to the series."""

for i in range(1,4):
    a_list = [34, 23, 65, 86, 23, 43]  
    random.shuffle( a_list )  
    print( a_list )  
    random.shuffle( a_list )  
    print( a_list )  
print("-------------------------------------------")
