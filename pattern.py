# # pattern printing
#try:
while(True):
    n = int(input("No of rows you want:\n"))
    x = int(input("Enter 0 or 1:\n"))
    z = bool(x)
    if z == True:
        for i in range(0,n+1):
            print("*"*i)

    elif z == False:
        for i in range(n,0,-1):
            print("*"*i)
    ask = input("Do you want to continue?\n""Y for yes or N for no:\n")
    ask = ask.capitalize()
    if ask == "Y":
        continue
    else:
        print("Thank you!")
        break
#except Exception as e:
   # print(e,"\n\nInvalid Input!")

# x=int(input("Enter the number of rows you want to print:\n"))
# a=int(input("Enter 1 for True and 0 for False:\n"))
# if(a==1):
#     for i in range(x+1):
#         for j in range(i):
#             print("*",end="")
#         print()
# elif(a==0):
#     for i in range(x+1):
#         for j in range(x-i):
#             print("*",end="")
#         print()
                    


