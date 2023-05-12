#BREAK STATEMENT IS A STATEMENT IN WHICH WE EXIT THE LOOP
for i in range(1 ,16):
    if(i == 11):
        print("EXIT FROM LOOP")
        break
    print("5 X ",i," = ",5 * i)


print("------------------------------------------------------------------")

#CONTNUE STATEMENT IS A STATEMENT IN WHICH WE SKIP THAT ITERATION
for i in range(1 ,16):
    if(i == 11):
        print("SKIP THE NUMBER FROM LOOP ")
        continue
    print("5 X ",i," = ",5 * i)

    