##managing dierectories
#we need os module for this

import os
#os.mkdir("C:\\Workstation\\Personal\\Python_Basics\\New Folder")
#made this line commnets after excuting bec it cannot create same folder again
#new folder has been created
#os.mkdir("New Folder2")
#New Folder2 is created without giving full path as working in the same directory
# for changing directory
#os.chdir("C:\\Workstation\\Personal\\Python_Basics\\New Folder")
#os.mkdir("test")
#test folder craeted inside new folder

#for removing folder
#os.rmdir("C:\\Workstation\\Personal\\Python_Basics\\New Folder\\test")
#test folder is deleted
#os.rmdir("New Folder")
#os.rmdir("New Folder2")


#to find your working directory if you are lost
print os.getcwd()   #C:\Workstation\Personal\Python_Basics
