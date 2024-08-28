# lambda functions or anonymous functions
def add(a, b):
    return a+b

adds = lambda x, y: x+y
f=int(input("1"))
g=int(input("2"))
print(adds(f,g))


# def z_first(z):
#     return z[1]


# z = [[1,14],[5,6],[8,23]]
# z.sort(key=z_first)
# print(z)

z = [[1,14],[5,6],[8,23]]
z.sort(key=lambda c:c[1])
print(z)