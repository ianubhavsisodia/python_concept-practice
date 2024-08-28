#arithmetic operators
print("5+6 is", 5+6)
print("5-6 is", 5-6)
print("5*6 is", 5*6)
print("5/6 is", 5/6)
print("15//6 is", 15//6)# float division method, ignores decimal
print("5**3 is", 5**3)#exponential operator
print("5%3 is", 5%3)#modulus remainder

#assignment operators
x = 5 # = is assignment operator
print (x)
x %=7 #increment operator
#similarly : -=, *=, /=, %=, and many more
print(x)

#comparison operator
i = 5
print(i>=6)
#similarly, !=, ==, <=

#logical operators
a = True
b = False
print(a and b)
print(a or b)
 #for 'or' if one is true then true
#but for "and" if both is true then true

#identity operator
a = True
b = False
print(a is b)
print(a is not b)
print(8 is not 8)

#membership operator
list = [3, 5, 7, 4, 12, 33, 21, 15]
print(15 not in list)
print(15 in list)

#bitwise operator
#0 - 00
#1 - 01
#2 - 10
#3 - 11
print(1 & 3)
print(1 | 3)