##Handling Files
#Read methos is for reading text from the file
#create a file using open function in python


#creating a text file using python
myobj=open("test.txt","w")  #two arguments, 1st for file name which we want to create, 2nd arguments is the mode in which you want to access the file
#w for write mode
myobj.write("""this is so cool!
Now I can create text files using python,""")
myobj.close()   #till we don't do this close our object text in file won't be saved
# we can see that a text file with name test is created in the working directory

myobj=open("test.txt","a")  #'a' for append, with 'w' it will replace the text in the text file
myobj.write(""" Let's see where this text goes!""")
myobj.close()

myobj=open("test.txt","r")
# creating a variable text which will save content of the text file in the variable content
text=myobj.read()
print (text)
myobj.close()


