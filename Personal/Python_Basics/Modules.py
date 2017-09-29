##Modules
#module is a python script containing code
# advantage is you can save your code,varibale , classes, function and can be used by importing
import sys
print sys.path
"""['C:\\Workstation\\Personal\\Python_Basics', 'C:\\Workstation\\Personal\\Python_Basics', 'C:\\Python27\\python27.zip', 'C:\\Python27\\DLLs', 'C:\\Python27\\lib', 'C:\\Python27\\lib\\plat-win', 'C:\\Python27\\lib\\lib-tk', 'C:\\Python27', 'C:\\Python27\\lib\\site-packages']
"""
#python looks for modules in all these direcories
def hello():
    print ("What's your name?")
    name=raw_input()
    print ("Hello", name,"have a nice day!" )
    return

hello()

##runned this module by saving this module in the python directory where it search for


