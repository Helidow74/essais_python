import pandas as pd

list_of_things_to_do = []

while True:
    new_thing = input('Ajoutez une chose à ne pas oublier ou taper "*" pour terminer : ')
    if new_thing == "*":
        break
    else:
        if new_thing not in list_of_things_to_do:
            list_of_things_to_do.append(new_thing)

print("---------- Choses à ne pas oublier : ----------------")
for thing in list_of_things_to_do:
    print(f"- {thing}")

df = pd.DataFrame(list_of_things_to_do)

with open('todolist.csv', "a"):
    df.to_csv("todolist.csv", mode='a', header=False, index=False)

