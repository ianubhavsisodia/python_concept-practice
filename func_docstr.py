a = 9
b = 8
c = sum((a, b)) #built in function
print(c)

#user defined functon
def function1(a,b):
    print("Hello you are in function 1", a+b)

def function2(a,b):
    """This a function to calculate avg of two numbers"""
    average = (a+b)/2
   #print(average)
    return average
v=function2(5,7)
print(v)

print(function2.__doc__)

#to update the code just update the function and it will automatically update the code according to your requirement
