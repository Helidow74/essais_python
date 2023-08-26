import pandas as pd

# choix de la checklist :
name = input("\n a - checklist_soussou"
             "\n b - checklist_phaton"
             "\n c - checklist_ket"
             "\n d - checklist_commune"
             "\n -------------------------------------------------------------------"
             "\nEntrez la lettre de la checklist parmi les choix proposés ou entrez une nouvelle personne : ")

# correspondance du choix précédent avec un filename et un list_name :
match name:
    case "a":
        filename = "checklist_soussou.csv"
        list_name = "checklist soussou"
    case "b":
        filename = "checklist_phaton.csv"
        list_name = "checklist phaton"
    case "c":
        filename = "checklist_ket.csv.csv"
        list_name = "checklist ket"
    case "d":
        filename = "checklist_commune.csv"
        list_name = "checklist commune"
    case _:
        filename = "checklist_" + name + ".csv"
        list_name = "checklist " + name


# ajouter des choses à la liste choisie :
def add_thing_to_do():
    list_of_things_to_do = []
    print("\n---------------------------------------------------------------------")
    while True:
        new_thing = input(f'Entrez une chose à ajouter à la liste "{list_name}" ou taper "*" pour terminer : ')
        if new_thing == "*":
            break
        else:
            if new_thing not in list_of_things_to_do:
                list_of_things_to_do.append(new_thing)

    # print("---------- Choses à ne pas oublier : ----------------")
    # for thing in list_of_things_to_do:
    #     print(f"- {thing}")

    df = pd.DataFrame(list_of_things_to_do)
    return df


# enregistrer les données de la liste dans un fichier en utilisant le filename défini au début :
def save_to_file(df_data, file_name):
    try:
        with open(file_name, "a") as f:
            df_data.to_csv(file_name, mode='a', header=False, index=False)
    except AttributeError:
        print(f"Rien n'a été ajouté au fichier")


# ---------------------------------
# programme principal :
df_list = add_thing_to_do()
save_to_file(df_list, filename)


# ------------------------------
# Modifier le code existant pour AJOUTER une fonction permettant d'éliminer les doublons :
# - récupérer les données du csv dans un dataframe
# - fusionner le dataframe des nouvelles choses avec le dataframe  du csv dans un set
# - reconvertir le set en dataframe
# - sauvegarder dans le fichier l'intégralité du dataframe obtenu (ne plus utiliser "a"(append) et utiliser "w" (write)
