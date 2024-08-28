print("Enter num1:")
num1 = input()
print("Enter num2:")
num2 = input()
#try executing, if possible execute otherwise ignore
try:
    print("SUM =",int(num1)+int(num2))
except Exception as e: #print exception as string 
    print(e)  

print("This line is very important")