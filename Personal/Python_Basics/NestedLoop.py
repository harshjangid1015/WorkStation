##Nested Loops
# Nested loops are loops within loops
#Nested if-else statements are statements within if-else statements
#finding prime numbers between 2 & 100
for var1 in range(2,101):    #in range function upper limit is not included in set
    flag=True   #flag variable is used to see whre you are in the program & what is happening
    for var2 in range(2,var1-1):
        if(var1%var2==0):
            print(var1,"is not a prime number")
            flag=False
            break
    if flag:    #if flag value is true
        print(var1,"is a prime number")