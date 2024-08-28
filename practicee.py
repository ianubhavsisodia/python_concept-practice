#leap year
year=int(input("Enter the year: "))
if year%4==0 or year%100!=0 and year%400==0:
    print('This is a leap year')  
else:
    print("not leap")

#positive number
num=int(input("Enter the number: "))
if num>=0:
    print('This is a Positive Number')  # if input is positive, output "positive"
else:
    print("The number is not positive")

#counting using while loop
#defining variable
day=0
squats=0
total=0
print("Enter the no. of squats you did on each day for the last week\n")
#loop body
while day<=6:
    day=day+1
    squats=int(input("Squats on Day {} : ".format(day)))
    total=total+squats

avg_sqts=total/day
print("\nAverage Squats per day = {:.2f}".format(avg_sqts))

# multiplication table
num=int(input("Enter the number: "))
i=1

while i<=12  :
    
    a=num*i
    print("{} * {} is {}".format(num,i,a))
    i=i+1

## factorial
num= int(input("Enter the number : "))
fact=1
for x in range(1, num+1):
    fact=fact*x
print("The factorial of {} is {}".format(num, fact))

#func to check purchasing eligibility
def verdict(m1,m2,m3):
    sum=m1+m2+m3
    if total>=15000:
        print("Yes, you can get a new smartphone")
    else:
        print("Sorry, this is not the right time to splurge on a smartphone")
    return

gift=int(input("Gift money from family : Rs."))
savings=int(input("Savings : Rs. "))
internship=int(input("Internship earned: Rs. "))

verdict(gift,savings,internship)


#calculate total contribution per person

def food(f):
    tip=0.1*f
    f=f+tip
    fperson=f/num
    return fperson

def movie(m):
    mperson=m/num
    return mperson

num=int(input("No. of friends : "))
ftotal=int(input("Spent of food : "))
mtotal=int(input("Spent on movie : "))

x = food(ftotal)
y = movie(mtotal)
print("The per person total is :",x+y)