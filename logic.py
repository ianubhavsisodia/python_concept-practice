def swap_case(a):
    b=list(a)
    for i in range(0,len(b)):
        if b[i].islower():
            b[i]=b[i].upper()
    
        elif b[i].isupper():
            b[i]=b[i].lower()
    c=''''''    
    for i in range(len(b)):
        c=c+b[i]

    return c

s=input()
result=swap_case(s)
print(result)

###### polynomial evaluation #####
fx = input("Enter a Polynomial: ")
x = int(input("At which position should the polynomial be evaluated: "))
print(eval(fx.replace('x', str(x))))


def print_formatted(number):
    for i in range(1,number+1):
        print((bin(i)[2:]))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


#### String Validation #####
a = input()
def alnum(a):
    if a.isalnum():
        return True
    else:
        return False


    
if any([alnum(i) for i in a ]):
    print(True)
else:
    print(False)
    
    
for i in range(len(a)):
    if a[i].isalpha():
        print(True)
        break
else:
    print(False)    
    
for i in range(len(a)):
    if a[i].isdigit():
        print(True)
        break
else:
    print(False)
            
for i in range(len(a)):
    if a[i].islower():
        print(True)
        break
else:
    print(False)
            
for i in range(len(a)):
    if a[i].isupper():
        print(True)
        break
else:
    print(False)

##### set symmetry ###### 
a=('2','4','5','9')
b=('2','4','11','12')
c=set(a)
d=set(b)
print("\n".join(sorted((c-d|d-c),key=int)))


students = int(input())
    
