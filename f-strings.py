#formatting
me = "Harry"
a1 = 3
# a = "This is %s"%me
# a = "This is {}{}"  
# a = "This is {1} {0}" 
# b = a.format(me,a1)
# print(b)
import math
#f strings- helps to increase the readability of the code and makes the code optimized
a = f"This is {me} {a1} {math.cos(30)}"
print(a)
