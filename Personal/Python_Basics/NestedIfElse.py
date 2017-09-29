##Nested IF-ELSE statement
#ASCI A=65, B=90, a=97, z=122

# print "Enter a char to see apl/cons/vovel" +

char = raw_input("Enter a char to see apl/cons/vovel: ")
#???(why incorrect)char= input("Enter a char to see apl/cons/vovel: ")
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
