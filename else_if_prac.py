print("Enter your age:")
age = int(input())
if 65>age>18:
    print("Yes, you can drive.")
elif age>65:
    print("You are too old to drive.")
elif age==18:
    print("We can't decide, We need to do your physical test.")
else:
    print("No, you can't drive.")