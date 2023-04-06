#DEFAULT ARGUMENTS
def Average(a = 5,b = 5):
    print("AVERAGE IS:\t",(a+b)/2)


Average() # -->That accept Default arguments

#KEYWORD ARGUMENTS --> Order Does Not matter
Average(b = 9, a= 3) #that overwrite the Arguments

#REQUIRED ARGUEMNTS --> Cannot Skip the Value
def Sum(c,d): #--> For Sum Arguemnts is necessary that is call required arguments
    print("SUM:\t", c + d)

Sum(123,345)  

#VARAIABLE LENGTH ARGUMENTS
def LargeAverages(*numbers): # "*" -->used when  i do not know about length of data 
    sum = 0
    for i in numbers:
        sum = sum + i  
    return sum/len(numbers)   #-->len()--> Built In function 


print("Average ",LargeAverages(1,2,3,4,5,6,7,8,9,10)) 

def Name(*name):
    for i in name:
        print(i)

Name("Muhammad","Aqeel","Shakeel")        

