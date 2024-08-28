# a is for append and w is for write
# f = open("Anubhav.txt", "w") #since write mode is not default, we need to specify it
# a = f.write("Anubhav is studying in VIT\n")
# print(a)
# f.close()

# f = open("Anubhav.txt", "w") #since write mode is not default, we need to specify it
# a = f.write("Anubhav is studying in VIT\n")
# print(a)
# f.close()

#handle read and write both
f = open("Anubhav.txt", "r+")
print(f.read())
f.write("Thank you")

