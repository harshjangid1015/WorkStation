# symobol is for comments
print "Hello World"

str1= "Hi there !"  #"" for strings
print str1


#"""write & hit enter to write in next line, then close this with again """
str2="""My new
String"""
print str2

#to have two excutable stement in one line separated by ;
print "Hi there!" ; print "what's up !"

# if you created a variable and if you restart shell then those avriables are lost

###4. Variables in Python
var1=var2=var3=100
print var1; print var2;print var3
#assigning different values to variables in single line
var1, var2, var3=100, 65.2, "String"
print var1; print var2;print var3

###5. Numbers & Strings
# del var1 will delete variable var1
#integers, float, long, complex(real, imaginary) data types are supported by Python
myvar=7-4j
yourvar=3+10j
print myvar+yourvar

#printing part of the string
str="Hello World"
print str[0]
print str[0:5]
print str[6:]
print str*4 #dispalying str four times
print str + " what's up?"  #concatinate(adding string)


###6. Lists & Tuples
#list- hybrid date type means in list we can add different data types
# list in python is similar to array in c/c++ but in c/c++ all data types in array shouls be same
mylist=['one', 'two','three', 4,5.0, 6+2j]
print mylist
print mylist[0]
print mylist[1:]

newlist=[7,'eight',9.0]
print mylist + newlist
newlist[0]='seven'  #updating list
print newlist

#tuples are similar to list but two differences
#1tuples are created with () not []
#2 tuples cannot be updated
mytuples=('a word', 'a number', 10)
print mytuples
# partial printing is similar to list


###7. Dictionaries
#two ways to creating dictionary
address={} # we us e{} for dictionary
address["John"]="john@gmail.com"
address["Adam"]="adam@gmail.com"
address["Peter"]="peter@gmail.com"
print (address)  #: is used to sepearte key & its value in the result
#2nd way of creating dictionary
new={'apple': 'fruit', 'iphone': 'phone', 7: 'a number'}
print new
#how to see only keys in dictionary without values
print address.keys()
print address.values()


###8. data type conversion
print int(55.83)  #float to integer
print float(36)   #integer to float
# #ineger to string my_string=str(9500)...it id giving error but working in python shell
# usful to extract some digits or entire digits out of numbers
#tuple method for converting a string to tuple
print tuple("This is a string")
#list method to convert a strint to a list
print list("This will be a list")
#chr function to get ASCI value of a character
print chr(65)
#ord function is to give number ASCI value of a charcter
print ord('a')
print hex(4500)  # to find hex code of a function
print oct(4500)  # octal code
print bin(42)    # find binary value of a number

