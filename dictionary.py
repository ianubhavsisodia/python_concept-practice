#dictionary is nothing but key value pairs
d1 = {}
#print(type(d1))
d2 = {"Anubhav":"Burger", "Rohan":"Fish", "Himanshu":"Roti",
"Rakesh":{"B":"maggie", "L":"rice", "D":"chicken"}}

print(d2["Rohan"])
d2["Shubham"] = "maggie" #to add new data
d2[33] = "fruits"
 # type: ignore
del d2[33]

#d3 = d2
d3 = d2.copy()
del d3["Rakesh"]

#functions
print(d2.get("Anubhav"))
d2.update({"Sahej":"coffee"})
print(d2.keys())
print(d2.items())
print(d2)

