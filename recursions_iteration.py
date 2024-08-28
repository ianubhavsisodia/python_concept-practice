#recursion
#using function inside a function
def print2(str1):
    #print2(str1) # gives recursion error
    print("This is " + str1)

print2("Anubhav")

# n! = (n) * (n-1) * (n-2) * (n-3)......1
# n! = n * (n-1)!

#iterative approach
def factorial_iterative(n):
    """
parameter n : Int
return: (n) * (n-1) * (n-2) * (n-3)......1
"""
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac
number = int(input("Enter the number:\n"))
print("Factorial using iterative method is ",factorial_iterative(number))

#recursive approach

def factorial_recursive(x):
    """
parameter n : Int
return: (n) * (n-1) * (n-2) * (n-3)......1
"""
    if x == 1:
        return 1 

    else:
        return x * factorial_recursive(x-1) 
# 5 * factorial_recursive(4)
# 5 * 4 * factorial_recursive(3)
# 5 * 4 * 3 * factorial_recursive(2)
#  and so on
# when factorial_recursive (1) then it will again return 1

number = int(input("Enter the number:\n"))
print("Factorial using recursive method is ",factorial_recursive(number))


def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
num = int(input("Enter number:\n"))
print(fibonacci(num))
    


