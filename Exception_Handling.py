#---------------------------------HANDLE THE ERROR---------------------------------

# number = (input("Enter the number\t"))
# print(f"Multiplication of {number} are as folow")
# try:
#     for i in range(1,11):
#         print(f"{int(number)} X {i} = {int(number)*i}")
# except:
#         print("Some Error occured")
# print("End The Program")  

# try:
#     num = int(input("Enter the index\t"))
#     array = [2,3,4,5]
#     print(array[num])
# except ValueError:
#     print("Number not a integer")
# except IndexError:
#     print("Index Error!!")   
# finally:
#     print("I am always executed")   

a = (input("Enter the number b/w 5 and 9:\t"))

if(a == "quit"):
    print("Quit The Program")

elif(a < 5 or a > 9):
    raise ValueError("ERROR")