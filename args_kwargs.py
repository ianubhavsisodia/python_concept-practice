# def function_name_print(a, b, c, d, e):
#     print(a, b, c, d, e)

# function_name_print("Harry", "Rohan", "Skillf", "Hammad", "Shivam")

def funargs(normal, *args, **kwargs):
    # print(type(args))
    # print(args[0])
    print(normal)
    for items in args:
        print(items)
    print("\nNow I would like to introduce some of our heroes")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")

list1 = ["Harry", "Rohan", "Skillf", "Hammad", "Shivam", "The programmer"]
normal = "I am a normal argument and the students are:"
kw ={"Rohan":"Monitor", "Harry":"Fitness instructor", "The programmer":"Coordinator", "Shivam":"cook"}
funargs(normal, *list1, **kw)