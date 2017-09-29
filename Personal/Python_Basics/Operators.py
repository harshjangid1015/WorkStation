###9. Airthmatic & Comparision Operators
#07types opeartors in python

#Airthmatic operators
print 10+15
print 15-10
print 15*10
print 15/10
print 15%10  # modulus operator gives remainder
print 3**2   # ** for raise to power

#Comparision Operator
a=15
b=10
print a==b    #equality check
print a!=b    #not equal check
print a>b
print a<b
print a>=b
print a<=b

#Bitwise opeartors
#works on binary numbers/bits in binary numbers
a=15
b=10
print bin(a)
print bin(b)
print bin(a&b)  #AND operartion
print bin(a|b)  #OR operator
print bin(a^b)  #Exclusive OR operator...0 is removed bec of insignificant. actual output 0b0101

#Logical Operators
#works on whole value true or false
#in python all non zero numbers are true only zero is false
a=True
b=False
print a and b ##AND Operation results in true only when both are true
print a or b    #or operator
print not a     #not opeartor gives opposite value
print not b

#Membership opeartor
#lets you check if a value is present in the set or not
str1= "I have a lazy dog"
print str1
print "dog" in str1
print "lion" in str1
# doesn't care if the word is separate it just check same character is there in string in same sequence
mylist=[1,3,19,32,48,77]
print 65 in mylist
print 19 in mylist

#Identity Operators
#compare memory loactions of the object & the tell you if two variables have same value as well as same data types
a=42    #numeric value
b='42'  #string
print a is b    #is identity opeartor
c=42
print a is c    # now both data types and values are same
# "is not" checks either values are different or data types are different
print a is not b

#Operator Precedence
print 5+4*2     #'*' before '+'
# to avoid knowing all we can use ()
print (5+4)*2


