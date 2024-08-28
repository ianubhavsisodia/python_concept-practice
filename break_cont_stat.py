i = 0
while(True):
    if i+1<5:
        i = i+1
        continue
    print(i+1, end=" ")
    if i==44:
         break #stop the loop
    #print(i+1, end=" ")
    i = i+1



'''while(True):
    if a<=100:
         print("Sorry, try again!\n""Enter the number again:")
    a= int(input())
    
    if a>100:
        print("You got it")'''

###
while(True):
    print("\nEnter a number greater than 100:")
    a=int(input())
    if a>100:
        print("You got it!\n")
        break
    else:
        print("Try Again!")
        continue
        
    
        
    


    
   


    

    
        
        

