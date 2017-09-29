#creating dictionary
#years values as key & movies released in those years as values

movies={1994:"Pulp Fiction",1997:"Seven",2000:"Cast Away",2006:"Blood Diamond"}
print movies

#finding number of elements or key value i have in the dictionary
print len(movies)   #4 key values in association

#dispalying only key values
print movies.keys()     #[2000, 1994, 1997, 2006]

#dispalying only values from dictionary
print movies.values()   #['Cast Away', 'Pulp Fiction', 'Seven', 'Blood Diamond']

#if you want to add more keys and value from another dictionary
new={1972:"The Godfather",1980:"Raging Bull",2004:"The Aviator"}
print new   #{1980: 'Raging Bull', 1972: 'The Godfather', 2004: 'The Aviator'}
movies.update(new)
print movies    #{2000: 'Cast Away', 1972: 'The Godfather', 2006: 'Blood Diamond', 2004: 'The Aviator', 1994: 'Pulp Fiction', 1980: 'Raging Bull', 1997: 'Seven'}

#clear method
#used to clear content of the dictionary
movies.clear()
print movies    #{}