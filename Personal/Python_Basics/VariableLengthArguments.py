##function with variable length Arguments
#while creating a function when we are not sure what number of argumnets will be pass through the function
def variable(*mytuple):
    for var in mytuple:
        print(var)
    return
variable(10)    #10 #one argument
variable(10,20,30,40,50) #5argument
"""10
10
20
30
40
50"""
variable("Hello", "World")
"""Hello
World"""