#function is a block of code that performs some task can be called by a given name
#mainadavantage of using reusability of code/ you can use that same code a bunch of time
#this is different from loops btw loops have different iteration with different inputs but in function same thing happening over and over again but you can change input of function if you want
# use def key word to create
#example- creating a function with name sample which take text as argument and dispaly that text on screen
def sample(text):   #takes text input as argument
    print(text)
    return
#now using this function
sample("Hello world!")      #Hello world!

def sample2():  #not necessary for ur function to take in some arguments
    print("I will print this no matter what!")
    return
sample2()       #I will print this no matter what!
#since i have print statement in the function and i called the function so despite having no input in the function it will print

#creating a finction which will take more than one argument
def calculator(a,b):     #a,b are my dummy parameters
    print ("Addition:", a+b)
    print ("Subtraction:", a-b)
    print ("Multiplication:", a*b)
    print ("Division:", a/b)
    return
# now using this function calculator
calculator(155,25)
"""
('Addition:', 180)
('Subtraction:', 130)
('Multiplication:', 3875)
('Division:', 6)
"""

def power(a,b):
    var=a**b
    return var      #it will return value of the var
print power(6,3)    #216
