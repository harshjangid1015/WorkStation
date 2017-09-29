##Pass by Reference vs Value
#when you pass something by reference then you are passing the object itself
#when you are passing something by value then you are creating copy of that object or variable then you are passing the copy to the function. whereas when you pass something by reference then any change which you make inside the finction those changes are reflected outside value as well. where as if you pass something by value then the changes which you make to the function/copy of the variable ,those changes are not reflected back to the calling function

employee={'Alex':1500,'John':1200,'Peter':1400}     #creating dictionary
def test(employee):
    new={'Buck':2000,'Stan':4000}   #creating new dictionary / new employee joined
    employee.update(new)    #updating the dictionary
    print ("inside the function", employee)
    return
test(employee)
print ("Outside the function", employee)
"""
('inside the function', {'Stan': 4000, 'Buck': 2000, 'John': 1200, 'Alex': 1500, 'Peter': 1400})
('Outside the function', {'Stan': 4000, 'Buck': 2000, 'John': 1200, 'Alex': 1500, 'Peter': 1400})

"""
#changes which we made inside the function reflected putside the function as well
#this proves that in python variables are passed by reference not by value

employee2={'Alex':1500,'John':1200,'Peter':1400}     #creating dictionary
def test2(employee):
    employee2={'Buck':2000,'Stan':4000}   #creating new dictionary / new employee joined
    print ("inside the function", employee2)
    return
test2(employee2)
print ("Outside the function", employee2)
"""
('inside the function', {'Stan': 4000, 'Buck': 2000})
('Outside the function', {'John': 1200, 'Alex': 1500, 'Peter': 1400})
"""
#value outside is same as the value with which we created dictionary
