#string slicing
mystr = "Anubhav is a good boy"
print(mystr[4])
print(mystr[0:7])
print(len(mystr))
print(mystr[0:21])
print(mystr[0:21:2]) #advance/extended slicing
#":2" skips 2 characters in the above string
print(mystr[-5:-1]) #negative index
#string functions
print(mystr.isalnum())#check if alpha-numeric 
print(mystr.isalpha())#check if aplhabatical
print(mystr.endswith("boy"))
print(mystr.count('a'))
print(mystr.capitalize())
print(mystr.upper())
print(mystr.lower())
print(mystr.find(" a "))
print(mystr.replace("is", "are"))