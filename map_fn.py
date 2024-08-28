# # map function applies a specific function to whole list

# numbers = ["3", '34', "64"]

# #for i in range(len(numbers)): #since list contains str data type we used len function
# #    numbers[i] = int(numbers[i])

# numbers = list(map(int, numbers)) #map func returns a object, we need to specify the funct in the map func argument

# numbers[2] = numbers[2] + 1
# print(numbers[2])


# # def sq(a):
# #     return a*a

# # num = [2,3,4,6,76,3,3,2]
# # square = list(map(sq, num))
# # print(square)

# num = [2,3,4,6,76,3,3,2]
# square = list(map(lambda x: x*x, num))
# print(square)


def sq(a):
     return a*a

def cube(a):
     return a*a*a

funcs = [sq, cube]
# num2= [2,3,4,6,76,3,3,2]
for i in range(5):
    val = list(map(lambda x:x(i), funcs))
    print(val)

