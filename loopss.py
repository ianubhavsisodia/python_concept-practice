#for loops
list1 = ["Anubhav","Shubham","Aryan","Aksh","Arushi"]
#print(list1[0], list1[1])
for item in list1:
    print(item)

list2 = [["Anubhav", 4],["Shubham", 7],["Aryan", 8],["Aksh", 5],["Arushi", 11]]
for item, lollypop in list2:
    print(item, "eats", lollypop, "lollypop" )

dict1 = dict(list2) #typecasting
print(dict1)

for item, lollypop in dict1.items():
    print(item, "eats", lollypop, "lollypop" )

for item in dict1: #print keys of dict
    print(item)

#practice

list3  = [1, 2, 3, "hjdfh", "gdhgd", 8, 21, 13, 6, "ueru", 33, 8, 10, 14, 17, 18]
for item in list3:
    if str(item).isnumeric() and item>6:
        print(item)

#while loops
i = 0
while(i<45):
    print(i)
    i = i+1

