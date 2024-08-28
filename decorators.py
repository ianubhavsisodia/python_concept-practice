# def function1():
#     print("Subscribe now")

# func2 = function1
# del function1
# func2() 

def funcret(num):
    if num==0:
        return print
    if num==1:
        return sum
# here we can see that we can return a function with a function
a = funcret(1)
print (a)

def executor(func):
    func("This")
# here we can see that we can write a function as a argument in another function
executor(print)


def dec1(func1):
    def nowexec():
        print("Executing Now")
        func1()
        print("Executed")
    return nowexec
@dec1 #decorator
def who_is_anubhav():
    print("Anubhav is a good boy")

# who_is_anubhav = dec1(who_is_anubhav) #decorator
who_is_anubhav()