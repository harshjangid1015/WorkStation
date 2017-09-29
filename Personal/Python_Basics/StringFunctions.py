#Capitalised string function
#returns with first letter capital if not already
str1="hey what's up!"
print str1.capitalize()
#Hey what's up!

#Count method
#used to calculate number of times a string exist in another string
str1=""""Tom is a good guy
Tom is honest
Tom is a team player
Tom is a party pooper
Tom sleeps early
Tom works out"""
print str1.count('Tom')
#6

#ENDS WITH Function
str1="ilovetennis.com"
print str1.endswith('.org')     #False
print str1.endswith('.com')     #True

#FIND Method
#checks if the string which passed exists in the calling string or not
#if it exist then it returns index position of the first character of the argument which you passed
#if it doesn't exist then it retuns -1
str1="catch me if you can"
print str1.find('you')      #12 as its the position of y
print str1.find('us')       #-1

#IS LOWER Method
# check if all charcter of the calling string in lower case or not
str1= "Hello World"
print str1.islower()    #False
str1="hello world"
print str1.islower()    #True

#ISUPPER function
# checks if all charcter are in upper case or not
str1="HAVE A NICE DAY"
print str1.isupper()    #True

#LEN method or Length function
#it returns the number of characters in the string
print len(str1)     #15

#LOWER method
#changes all upper case character into lower case character
print str1.lower()      #have a nice day

#LSTRIP function
#removes character from left side of the string
str1="!!!!!!!What's up dudes?"
print str1.lstrip('!')  #What's up dudes?

#RSTRIP method
#removes charcters from right side of the string
str1= "This is so cool!!!!!"
print str1.rstrip('!')  #This is so cool

#UPPER method
#changes all character to upper case
print str1.upper()

#REPLACE method
#replaces a part or full string with a new string
str1= "I once had a fox."
#now repalcing worf fox with lion
print str1.replace('fox','lion')    #I once had a lion.

#SPLIT method
# splits a string on the occurence of the optional delimiter found in the argument
str1= "Tom Cruise"
#space character is a default delimiter
print str1.split()      #['Tom', 'Cruise']

#STRIP method
#strippping on both ends
str1="####Good Morning####"
print str1.strip('#')   #Good Morning

#SWAP CASE method
#convers lower case charcters into upper case charcters and vice versa
str1="I LOVE python"
print str1.swapcase()   #i love PYTHON

#TITLE function
#changes charcter of a string in such a way that starting charcter of each word will be in upper case and rest character will bw in lower case
print str1.title()      #I Love Python
