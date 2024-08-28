#list and lists functions
grocery = ["detol","vim","deo","fasewash", 69, 89]
print(grocery)
print(grocery[0]) #list index also starts from 0

numbers = [2, 6, 8, 9, 4]
#numbers.sort()
#numbers.reverse()
numbers.append(12)

print(numbers)

#list slicing
print(numbers[0:3])
print(numbers[::2])
print(numbers[::-1])

#list functions
print(len(numbers))
print(max(numbers))
print(min(numbers))

number = []
number.append(12)
number.append(4)
number.append(19)
number.append(16)
number.insert(1, 65)
number.pop()
number.remove(65)
number[1] = 6 #change the num at the specified index
print(number)

#list is mutable
#tuple is immutable
tp = (1, 2, 3)
print(tp)
#you cannot make tuple of one element, you need to add comma after the element (1,)

#swapping
a = 1
b = 2
(a, b) = (b, a)
print(a, b)