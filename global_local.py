x = 5
def myfunction():
    y = 4
    x = 3
    for i in range(0,3):
        global z
        z = 7
        x = x + 1
        print(y)
        z = z + 2
        print(f"The local varaible of x is {x}")
myfunction()
print(f"The global varaible of x is {x}")
# print(y) error throw because this local varaible that is used in function 
# print the information when function is call 

print(f"The global varaible z using global keyword is {z}")