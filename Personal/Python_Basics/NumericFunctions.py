##Numeric Functions

#Absolute Function returns distance of the function from Zero
print (abs(5))
print (abs(-5))     #-5 and +5 both have same distance from 0

#Module Function
#Module is like a library, we use to use this to use all functions that are in that module
import math # import statement to import module
print math.ceil(35.74)      #ceil function returns next higher intiger
print math.ceil(-35.74)

#exp function return exponent of number passes to it
print math.e
print (math.exp(7))     #equal to e**7

#Floor Method
#returns next lower integer value
print math.floor(16.97)
print math.floor(-16.94)

#SQRT(square root) function
#used to calculate square root of the number
print math.sqrt(25)

#Log function- Natural Log
#import math as usual
print math.log(5)
print math.log(math.e)
print math.log10(2)     #Log base 10

#MAX Function
#no need for math module
#gives maximum values from given arguments
print max(10,15,20,45,-18)

#MIN Function
#gives least value among arguments
print min(11,19,17,6,-213)

#ROUND function
#round off the vakue given
print round(17.4576,2)      #(_,2) means round off upto 2 digits

#Mode F method
#pass a fractional number and it gives you intiger part of number and fractional part of number seperartly
#import math module
print math.modf(11.971)

#Power method
#gives power of a number raise to another
print math.pow(4,2)     #equal to 4**2
#(0.9710000000000001, 11.0)

#Hypot method
#used to compute hypotnious of a triangle if we knows base and huight
print math.hypot(3,4)     #3 as base, 4 as height
#5.0

#Degrees method
#returns angle values in degrees for angle pass in radian
print math.degrees(math.pi)
print math.degrees(-4)      #-229.183118052

#RADIANS Method
#degree to radians
print math.radians(-229.183118052)  #-3.99999999999
