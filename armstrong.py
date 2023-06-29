num = int(input("Enter the number\t"))
sum = 0
order = len(str(num))
copy_num = num

while(num > 0):
    digit = num % 10
    sum += digit ** order
    num = num //10

if(sum == copy_num):
    print(F"{copy_num} is a armstrong number")
else:
    print(F"{copy_num} is not armstrong number")
