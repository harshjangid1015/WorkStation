##FOR Loop
#used to iterate over elements in set or sequence
# count number of vowels in name
count=0     #initialization
print("Enter your name:")
name=raw_input()
for letter in name:      #letter is variable we use
    if(letter in ['A','E','I','O','U','a','e','i','o','u']):
        count=count+1
print("You have", count,"vowels in your name.")
#? I don't know why I am getting print statement with single quotes
