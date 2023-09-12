friends2 = input("Quels sont les noms de vos amis ? ")
amounts2 = input("Combien chacun a-t-il dépensé ? ")

list_of_friends2 = friends2.split(",")
list_of_amounts2 = amounts2.split(",")

list_friends_amounts2 = []

if len(list_of_friends2) == len(list_of_amounts2) and len(list_of_friends2) == 2:
    for friend2, amount2 in zip(list_of_friends2, list_of_amounts2):
        list_friends_amounts2.append((friend2, amount2))
    print(list_friends_amounts2)
elif len(list_of_friends2) == len(list_of_amounts2) and len(list_of_friends2) != 2:
    print("Vous ne devez entrer que 2 amis et 2 montants")
else:
    print("le nombre d'amis ne correspond pas au nombre de montants.")
