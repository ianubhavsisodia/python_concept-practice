d1 = {"rubric":"category name", 
"tautology":"useless repetition", 
"abhorrent":"offensive to the mind", 
"dolorous":"showing sorrow", 
"purvey":"supply with provisions" }

print("Enter word")
word = input()
#to lower case the first letter
a = word[0].lower() + word[1:]
d1.get(a)
print("Meaning of", a, "is", d1.get(a))
