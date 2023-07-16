num = int(input("Enter the number for factorial\t"))


result = 1
def Factorial(result,num):
    for i in range(num):
        i = i + 1
        result *= i
    return result    

def FactorailZeros(num):
    i = 5
    count = 0
    while(num // i != 0):
        count += int(num/i)
        i = i*5 
    return count    

print(f"Factorial of {num} is {Factorial(result,num)}")
print(f"Number  of Zero in Factorial {num} is {FactorailZeros(num)}")
