##Global & Local Variable
# a varible which you create in you main program is Global variable. this function will be known to all parts of the program
# a variable which you create inside a function has local scope, this variable will not be known outside of the function

var=100
def sample():
    var=0
    print ("local value:", var)
    return
print ("Global value:", var)
sample()
"""('Global value:', 100)
('local value:', 0)"""

var=100
def sample(var):
    var=0
    print ("local value:", var)
    return
print ("Global value:", var)
sample(var)
"""('Global value:', 100)
('local value:', 0)"""
#again same values as value 100 is not used inside the function

var=100
def sample(var):
    print ("local value:", var)
    return
print ("Global value:", var)
sample(var)
"""('Global value:', 100)
('local value:', 100)"""

##Updating Global variable
"""var=100
def test():
    var=var+10
    print (var)
    return
test()  #Results in error bec variable var is being used eventhough its not initialised earlier
"""
var=100
def test():
    global var
    var=var+10
    print (var)
    return
test()  #110
print (var)  #110
#this means gloabal variable has been updated succesfully


