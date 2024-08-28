f = open("Anubhav.txt")
#print(f.tell())#tells the location of file pointer
print(f.readline())
f.seek(12) # read the file from specified character
#print(f.tell())
print(f.readline())
#print(f.tell())
f.close()