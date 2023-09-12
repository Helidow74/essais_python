friends = input("Quels sont les noms de vos amis ? (Séparer les noms avec virgule)")
amounts = input("Combien chacun a-t-il dépensé ? (Garder le même ordre que précédemment et séparer avec une virgule)")

# on splitte en utilisant la "," pour obtenir des listes d'éléments exploitables :
list_of_friends = friends.split(",")
list_of_amounts = amounts.split(",")

# on va récupérer les valeurs des deux listes et les zipper dans une liste de dictionnaires :
list_friends_amounts = []
for friend, amount in zip(list_of_friends, list_of_amounts):
    list_friends_amounts.append({"Name": friend, "Amount": amount})

print(list_friends_amounts)

# ------------------------------

# with tuples :

friends2 = input("Quels sont les noms de vos amis ? ")
amounts2 = input("Combien chacun a-t-il dépensé ? ")

list_of_friends2 = friends2.split(",")
list_of_amounts2 = amounts2.split(",")

list_friends_amounts2 = []

for friend2, amount2 in zip(list_of_friends2, list_of_amounts2):
    list_friends_amounts2.append((friend, amount))

print(list_friends_amounts2)
