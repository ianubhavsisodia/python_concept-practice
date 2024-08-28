s= int(input("Enter number of siblings: "))
p= int(input("Enter number of popsicles left: "))

if p%s!=0:
    print("Eat it all!")
elif p%s==0:
    print("Give All!!")
