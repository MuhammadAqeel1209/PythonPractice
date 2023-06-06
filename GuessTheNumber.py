n = 18
numberOfGuess = 9
checkHuess = 1
for i in range(numberOfGuess):
    num = int(input("Enter the number\t"))
    if(num == n):
        print("Guess the number is\t",n)
        print(f"You Guess the number in {checkHuess} try")
        numberOfGuess = numberOfGuess -1
        break
    if(n > num):
        print("Number High")
    if(n < num):
        print("Number is low")    
    numberOfGuess = numberOfGuess - 1
    checkHuess = checkHuess + 1

print("Number of Guess is left\t",numberOfGuess)