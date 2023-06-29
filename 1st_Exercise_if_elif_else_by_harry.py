#CALCULATOR IN PYTHON 
# one = 17;
# two = 8;
# one = int(input('enter value for first number\t'))
# two = int(input('enter value for second number\t'))

# print(one, "+",two, "IS = \t" , one+two)
# print(one, "-",two, "IS = \t" , one-two)
# print(one, "*",two, "IS = \t" , one*two)
# print(one, "/",two, "IS = \t" , one/two)
# print(one, "//",two,"IS = \t" , one//two)
# print(one, "%",two,"IS = \t" , one%two)


print("1 For Addition")
print("2 For Subtraction")
print("3 For Multiplication")
print("4 For Division")
print("5 For Double Division")
print("6 For Modulus")
choice = int(input("Enter Your Choice\t"))

one = int(input('enter value for first number\t'))
two = int(input('enter value for second number\t'))

if choice == 1:
    print(one, "+",two, "is = \t" , one+two)

elif choice == 2:
    print(one, "-",two, "is = \t" , one-two)

elif choice == 3:
    print(one, "*",two, "is = \t" , one*two)

elif choice == 4:
    print(one, "/",two, "IS = \t" , one/two)  

elif choice == 5:
    print(one, "//",two,"IS = \t" , one//two)

elif choice == 6:
    print(one, "%",two, "IS = \t" , one%two)

else:
    print("Plz Enter Correct Option")




