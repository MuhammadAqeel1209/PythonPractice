numOne = int(input("Enter the first number\t"))
numTwo = int(input("Enter the second number\t"))

maxNum = max(numOne,numTwo)

while(True):
    if(maxNum % numOne == 0 and maxNum % numTwo == 0):
        break
    maxNum = maxNum + 1

print(f"L.C.M of {numOne} and {numTwo} is {maxNum}")