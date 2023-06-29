import time

#import datetime

# timestramp = time.strftime('%H:%M:%S')
# print(timestramp)
# the_day = time.strftime("%A")

# print(the_day)
# datestramp = datetime.datetime(2023,2,8)
# print(datestramp.strftime("%d-%m-%y"))


# Get the current time
current_time = time.strftime("%H:%M:%S %p %A") # IN THE FORM OF 1 to 24 HOURS
today_time = time.strftime("%I:%M:%S %p  %A") # IN THE FORM OF 1 to 12 HOURS

hours = int(input("Enter the Hours in the form of 12:\t"))
hours = int(time.strftime("%I"))

if(hours >= 0 and hours <12):
    print("Say Good Morning")
elif(hours >= 12 and hours <17):
    print("Say Good Afternoon")
elif(hours >=17 and hours < 19):
    print("Say Good Evening")
else:
    print("Say Good Night")            


# Check if it is AM or PM
if today_time == "PM":
    print("Good evening, the current time is ",current_time)
else:
    print("Good morning, the current time is " ,current_time)
