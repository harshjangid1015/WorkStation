##The Continue Statement
#continue statement lets us pass the code or skip a set of iterartion
#in break statement you get out of that loop but here you just skip that iterartion
for var in range(1,16):
    if (var in range(9,14)):
        continue        #9 to 14 are skipped
    else:
        print (var)

#eg: ask for a string then dispaly all character of that string without space
print ("Entera string: ")
var=raw_input()
for letter in var:
    if(letter==' '):
        continue
    else:
        print(letter)

