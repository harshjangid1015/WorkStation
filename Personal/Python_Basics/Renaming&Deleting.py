#both renaming and deleting belongs to OS module so we have to import that
# if you don't have the file in python folder which you want to change then you have to write full path
import os
#os.rename("test.txt","new.txt")
# we are changing back, complete path is not necessary but i am writing for refennec as \\ is required insted of \
os.rename("C:\\Workstation\\Personal\\Python_Basics\\new.txt","C:\\Workstation\\Personal\\Python_Basics\\test.txt")

##Remove method is to remove file
#os.remove("test.txt")      #but we are not removing it
