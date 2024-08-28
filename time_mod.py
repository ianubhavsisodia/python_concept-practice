# to calculate the execution time of a program

import time

initial = time.time()
print(initial)
k = 0
while(k<45):
    print("This is Anubhav")
    time.sleep(2) #sleep the loop for the instance of 2 sec and then return the value
    k+=1
print("while loop ran in",(time.time() - initial), "seconds")

initial2 = time.time()

for i in range(45):
    print("This is Anubhav")
print("for loop ran in",(time.time() - initial2), "seconds")

local_time = time.asctime(time.localtime(time.time()))
#time.asctime shows the time in original time format as time.localtime returns it in tuple
print(local_time)