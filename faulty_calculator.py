while(True):
    print("\nCalculator\n")
    print("Enter first number:")
    a = int(input())
    x = input("Choose arithmetic operator:\n""+, -, *, /, **, % :\n")
    print("Enter second number:")
    b = int(input())
    if x == '+' and a ==56 and b==9:
        print(77)
    elif x == '*' and a==45 and b==3: 
        print(145)
    elif x == '/' and a==56 and b==4:
        print(8)       
    elif x == '+':
        print(a+b)
    elif x == '-':
        print(a-b)
    elif x == '*':
        print(a*b)
    elif x == '/':
        print(a/b)  
    elif x == '**':
        print(a**b)
    elif x == '%':
        print(a%b)

    cal = input("Do you want to continue?\n""Y or N\n")
    if cal == "Y": 
        continue
    elif cal== "N":
        print("Thank you for using this calculator!")
        break
    else:
        print("Inavalid input")   



    



