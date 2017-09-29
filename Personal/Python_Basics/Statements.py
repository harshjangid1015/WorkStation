##IF Statements
# in python we don't have {} of seperating bloack of code like in java
# here in python we use Tab/5Space for same
myvar= 50
if myvar<100:    #all statements which are at same level of indentation are in same block of code
     print ("you are short of being 100 percent")
#back space for coming out block of code
print ("Good Bye!")
myvar=150
if myvar<100:
    print ("you are short of being 100 percent")    #will not excuted
print ("Good Bye!")


##IF-ELSE Statement
#else block excuted if condition in the if bloack is false
myvar=50
if myvar<100:
    print ("you are short of being 100 percent")
else:       #back space for going out of if block
    print ("Yoy are at ypur best")
print ("Good Bye!")


##The ELIF statement
#elif allows to check multiple conditions
sp=1500     #selling price
cp=1200     #cost price
if (sp>cp):
    print("Congratulations !")
    print ("You have made a profit of ",sp-cp,"bucks")
#insted of creating two more IF statement for other two conditions we can use elif
#elif statement excute if IF statement fails
elif(cp>sp):
    print("Oops")
    print("you made a loss of ", cp-sp, "bucks")
else:       #excute this if both condition above are false
    print ("You didn't make or lose money.")


##Nested IF-ELSE statement
#ASCI A=65, B=90, a=97, z=122
char= input()
if ord(char)>=65 and ord(char)<=90:
    print ("you entered an upper alphbet")
    if char in ['A','E','I','O','U']:
        print("you entered a vowel")
    else:
        print("you entered a consonant")
elif ord(char)>=97 and ord(char)<=122:
    print ("you entered an lower alphbet")
    if char in ['a','e','i','o','u']:
        print("you entered a vowel")
    else:
        print("you entered a consonant")
else:
    print ("you didn't enter an alphabet")

