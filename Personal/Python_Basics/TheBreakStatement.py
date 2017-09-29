##The Break Statement
#used to prematuraly terminate excution of loop
var=1
while (var<=15):
    print (var)
    var=var+1
print ("Good Bye!")

var=1
while (var<=15):
    if(var==10):
        break
    print (var)
    var=var+1
print ("Good Bye! again")

while True:
    print("Enter a digit :")
    num=raw_input()
    var=str(num)
    #ASCI values 0=48, 9=57
    #Range function gives value from starting to ending
    if(ord(var) in range(48,58)):
        break
print("you are very obidient")




