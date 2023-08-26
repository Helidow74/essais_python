def ask_names_of_friends():
    asked_friends = input("\nWhat are the names of your friends ? (separate their names by a comma) : \n")
    asked_list_of_friends = asked_friends.split(",")
    return asked_list_of_friends


def ask_amounts():
    asked_amounts = input("\nHow much each of your friends spent (keep the same order as above and seperate by a comma)"
                          " : \n")
    asked_list_of_amounts = asked_amounts.split(",")
    return asked_list_of_amounts


list_of_friends = ask_names_of_friends()
list_of_amounts = ask_amounts()

while True:
    try:
        for i, amount in enumerate(list_of_amounts):
            list_of_amounts[i] = float(amount)
        break
    except ValueError:
        print("--------------------------------------------")
        print("\nPlease enter numbers of the amounts spent : ")
        list_of_amounts = ask_amounts()

while len(list_of_friends) != len(list_of_amounts):
    print("You did not enter the same number of friends than amounts spent!")

    list_of_friends = ask_names_of_friends()
    list_of_amounts = ask_amounts()

    while True:
        try:
            list_of_amounts = [float(amount) for amount in list_of_amounts]
            break

        except ValueError:
            print("Please enter numbers of the amounts spent ")
            list_of_amounts = ask_amounts()
else:
    friends = []
    total_spent = 0
    for friend, amount in zip(list_of_friends, list_of_amounts):
        friends.append((friend, amount))
        total_spent += float(amount)

    for friend, amount in zip(list_of_friends, list_of_amounts):
        even_share = total_spent / len(list_of_friends)
        friend_balance = float(amount) - even_share

        if friend_balance < 0:
            print(f"{friend} needs to give {-friend_balance:.2f}€")  # on met "-" pour obtenir montant positif
        elif friend_balance > 0:
            print(f"{friend} must be given {friend_balance:.2f}€")  # on arrondit 2 chiffres après virgules avec ":.2f"
        else:
            print(f"{friend} doesn't need to give or receive anything.")

    # print(f"\n{friends}")
    print("---------------------------------------------")
    for friend, amount in friends:
        print(f"- {friend} spent : {amount}€")
    print("------------------------------------------------")
    print(f"Total amount spent during the trip is : {total_spent}€")
    print("------------------------------------------------")
