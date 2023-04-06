"""
#Print whether the given number is even or odd using functions

def EvenOddNumber(number):
    if number %2 ==0:
        print(number," Is Even")
    else:
        print(number, " Is Odd")


data = int(input("Enter the Number:\t"))
EvenOddNumber(data)


#Print whether the number is positive or negative

def PositiveNegativeNumber(number):
    if(number >= 0):
        print(number," Is Postive")
    else:
            print(number," Is Negative")


integer = float(input("Enter the number\t"))
PositiveNegativeNumber(integer)


#Get the number of days in a month by the input of month name using function.
def FindMonthDay(monthName):
    if monthName == "January" or monthName == "March" or monthName == "May" or monthName == "July" or monthName == "August" or monthName == "October" or monthName == "December":
        return 31
    elif monthName == "April" or monthName == "June" or monthName == "September" or monthName == "November":
        return 30    
    elif monthName == "Feburary":
        return 28
    else:
        return 0


name = input("Enter the month name:\t")
FindMonthDay(name)

if(FindMonthDay(name) == 0):
    print("Invalid Month Name!!!")
else:
    print(name , "has", FindMonthDay(name),"days")    
 

#Print even or odd as well as positive and negative    
def EvenOddNumber(number):
    if number %2 ==0:
        print(number," Is Even")
    else:
        print(number, " Is Odd")

def PositiveNegativeNumber(number):
    if(number >= 0):
        print(number," Is Postive")
    else:
            print(number," Is Negative")

def EvenOddNumberPositiveNegativeNumber(number):
    PositiveNegativeNumber(number)
    EvenOddNumber(number)

data = int(input("Enter the number\t"))
EvenOddNumberPositiveNegativeNumber(data)


# velocity = distance/time

def CalculateVelocity(distance,time):
    return distance/time     
def CalculateDistance(velocity,time):
    return velocity *time    
def CalculateTime(velocity,distance):
    return distance/velocity



choice = input("1)Velocity\t2)Distance\t3)Time\nEnter the choice\t")
if(choice == "Velocity"):
    distance = float(input("Enter the value of distance:\t"))
    time = float(input("Enter the value of time:\t"))
    print("Velocity =\t",CalculateVelocity(distance, time))

elif(choice == "Time"):
    velocity = float(input("Enter the value of velocity:\t"))
    distance = float(input("Enter the value of distance:\t"))
    print("Time =\t",CalculateTime(velocity, distance))

elif(choice == "Distance"):
    time = float(input("Enter the value of time:\t"))
    velocity = float(input("Enter the value of velocity:\t"))
    print("Distance =\t",CalculateDistance(velocity, time))

else:
    print("INVALID INPUT!!")        

       """