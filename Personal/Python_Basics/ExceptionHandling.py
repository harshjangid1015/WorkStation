##Exception Handling
"""
print ("Enter numerator:")
num=input()
print ("Enter denominator:")
den=input()
res=int(num)/int(den)
print res     #15/3=5
"""
# if we use 15/0 then it gives error as we can't devide by zero
# but if we want to change the comment of error then

print ("Enter numerator:")
num=input()
print ("Enter denominator:")
den=input()
try:
    res=int(num)/int(den)
except:
    print("You can't divide by zero baby!")
else:
    print ("result:",res)
#15/0
#You can't divide by zero baby!