# This list comprehension code :
comp = [i for i in range(10)]
print(comp)

# does the same as this code :
comp = []
for i in range(10):
    comp.append(i)
print(comp)

# but in a more pythonic and neat way.
# --------------------------------------------

# other example of comprehension list use case :

i_plus_10 = [i + 10 for i in range(20)]
print(i_plus_10)

# -----------------------------------------
# another example with enumerate :

greetings = ["Hello", "World", "from", "Jedha"]
jedha_greeting = [(i + 10, hello) for i, hello in enumerate(greetings)]
print(jedha_greeting)

# ---------------------------------------
# another try with zip :

first_names = ["Lucy", "John", "Jade"]
surnames = ["Durand", "Eastwood", "Sheridan"]

persons = [(first_name + " " + surname) for first_name, surname in zip(first_names, surnames)]
print(persons)

# -------------------------------------
