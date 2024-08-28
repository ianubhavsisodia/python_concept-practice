#to read a file
f = open("Anubhav.txt") #file pointer - returned by open
print(f.readlines()) # to read as list
# print(f.readline()) #to read line by line
#content = f.read()

#for line in content:
   # print(line)

# for line in f: #to read line by line
    #print(line, end="")    
#f = open("Anubhav.txt", "rt")
#content = f.read()
#print(content)

#content = f.read(3)
#print(content)

#content = f.read(3)
#print(content)

#content = f.read(300)
#print("1", content)

f.close()
