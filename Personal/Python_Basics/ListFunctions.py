#lEN/lENGTH method
#returns number of elemnets presents in the list
mylist=[1,3,5,9,4]
print len(mylist)   #5

#MAX method
#returns highest value in the list
print max(mylist)   #9

#MIN method
#returns minimum value from the list
print min(mylist)   #1

#COUNT method
#returns number of times a elements present in the list
mylist=[3,3,3,3,3,1,1,5,5,5,7,7,7,7,9,9,]
print mylist.count(7)   #4

#APPEND method
# used to add a element at the end of the list
mylist.append(8)
#limitation is you can add one element at a time
print mylist    #[3, 3, 3, 3, 3, 1, 1, 5, 5, 5, 7, 7, 7, 7, 9, 9, 8]

#INSERT method
#used to insert a element in a list at a given index position
mylist=[4,1,9,3,7,2]
mylist.insert(5,6)  #5 is index position & 6 is the element we want to add
print mylist    #[4, 1, 9, 3, 7, 6, 2]

#REMOVE function
#used to remove a element from the list
#removes onlu first instance of the number/elemnet
mylist.remove(9)
print mylist    #[4, 1, 3, 7, 6, 2]

#REVERSE metjod
#reverses current order of the elements in the list
mylist.reverse()
print mylist    #[2, 6, 7, 3, 1, 4]

#SORT function
#organises elements of the list in ascending order by default
mylist.sort()
print mylist    #[1, 2, 3, 4, 6, 7]

