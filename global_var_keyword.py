# l = 10 #GLOBAL VARIABLE

# def function1(n):
#     #l = 5 #local variable
#     m = 8 #local variable
#     global l # global keyword, helps to modify globa variable
#     l = l + 45 # can't update a global variable within the function, need to use gobal keyword
#     print(l,m) #first it will search in local scope then in global scope
#     print(n, "I have printed")

# function1("This is me")
# print(l) #it will only search in global scope
x = 100
def anubhav():
    x = 20
    def rohan(): #nested function
        global x
        x = 88
    print("before calling rohan()", x)
    rohan()
    print("after calling rohan()", x)

anubhav()
print(x) 