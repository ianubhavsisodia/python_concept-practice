import random 

#we can use functions and sub-modules provided by the modules
# some modules only provide functions only

random_number = random.randint(0,5)
#print(random_number)
randd = random.random()*100
#print(randd)

listt = ["starplus",'DD1','Aaj tak', "CodeWithHarry"]
choice = random.choice(listt)
print(choice)
