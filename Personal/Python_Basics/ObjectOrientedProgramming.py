###Object Oriented Programming

#Class is connstruct which has some data members and also functions that use those data members or varibles to perform some operartions
class myclass:
    sample=0    #variable with value 0
    w=0         #w for white with initial count 0
    b=0         #blacl
    g=0         #gray
    o=0         #other
    color_list=['black','white','gray']     #created list
    def __init__(self,name):    #__init__is a special/conctroctor function for this class, this function will be called autimatically when an object of the class is created #all function in classes in python takes argument Self/ self has to be one of the argument
        myclass.name=name
        print ("What is the color of your car?")
        myclass.color=input()
        myclass.sample=myclass.sample+1
    def check_color(self):
        if myclass.color in myclass.color_list:
            if myclass.color==myclass.color_list[0]:
                myclass.b=myclass.b+1
            elif myclass.color==myclass.color_list[1]:
                myclass.w=myclass.w+1
            else:
                myclass.g=myclass.g+1
        else:
            myclass.o=myclass.o+1

    def display_result(self):
        print ("Hello",myclass.name)
        print ("Total number of black cars:",myclass.b)
        print ("Total number of white cars:", myclass.w)
        print ("Total number of gray cars:", myclass.g)
        print ("Other:",myclass.o)
        print ("Sample Size:",myclass.sample)

myobj=myclass("John")
myobj.check_color()
myobj.display_result()
