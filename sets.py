s = set()
print(type(s))

s_from_list = set([1, 2, 3, 4, 5])
print(s_from_list)

l = [6, 7, 8, 9, 10]
s_from_list1 = set(l)
print(s_from_list1)

s_from_list.add(12)
print(s_from_list)

s_from_list.remove(5)
print(s_from_list)

s1 = s_from_list.union(s_from_list1)
#s1 = s_from_list.intersection(s_from_list1)
#s1 = s_from_list.isdisjoint(s_from_list1)
print(s1)
#print(len(s1))
#print(max(s1))
#print(min(s1))