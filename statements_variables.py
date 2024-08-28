#VARIABLES (containers/ memory slots)

#integers
x = 5
print(type(x))

#string
y = "hello world"
print(y)
print(type(y))

#float
z = 2.5
print(type(z))

#boolean
t= False 
print(type(t))

#arethematic operations
print(x+z)
print(x*z)
print(x-z)
print(x/z)
print(x//z) #gives int part of divison
print(x%z) #gives the remainder part of divisions 

#typecasting #change the type of data  
a = 69
b = 89
print(a+b)
print(str(a)+str(b))

print(10*"hello world\n") #to print multiple times

c = "20"
d = "10"
print(int(c)+int(d))
print(10*str(int(c)+int(d)))
print(10*(c,d))


#input function
print("Enter your number")
num = input()
print("You entered", num)

#calculator
print("Enter numnber 1")
num1 = int(input())
print("Enter number 2")
num2 = int(input())
print("Sum is",num1+num2)
