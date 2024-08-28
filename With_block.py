# with function will handle both open and close func
with open("----.txt") as f:# no need to use close and open func
    a=f.readlines()
    print(a)


#f = open("Anubhav.txt", "rt")
#print(f.readline()) #it will stop the file pointer after giving the output and the code will not be executed further
#print(f.readline())


f.close()