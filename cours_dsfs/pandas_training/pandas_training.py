import pandas as pd

# création d'une variable avec le chemin vers les données pour être sûre de prendre les bonnes
# pour trouver le path, on tape dans la console "!pwd"
path_to_file = "/data/home/dubois/PycharmProjects/pythonProject/cours_jedha/pandas_training"

# Lecture des données depuis le fichier csv
data = pd.read_csv(path_to_file + "/covid-19.csv")

print(data.head())

# --------------------------------------------------
# data exploratory analysis principal functions :
# -------------------------------------------------

print(f"describe : \n {data.describe()}")

print(f"mean : \n {data.mean()}")

print(f"count : \n {data.count()}")

print(f"max : \n {data.max()}")

print(f"min : \n {data.min()}")

print(f"cases sum : \n {data['cases'].sum()}")
print(f"deaths sum : \n {data['deaths'].sum()}")

# -------------------------------------------
# select columns
# ------------------------------------------

# sélectionner des colonnes et des lignes en utilisant iloc [début ligne : fin ligne, début colonne : fin colonne]
# iloc means : index location
# ici on sélectionne toutes les lignes et les colonnes à partir de la deuxième colonne
print(data.iloc[:, 1:].head())

data = data.iloc[:, 1:]

# sélectionner avec le nom des colonnes : loc
columns = ["year", "cases", "deaths", "countriesAndTerritories"]
print(data.loc[:, columns].head())


# ----------------------------------------
# filter data
# ---------------------------------------

# filter data with masks
# Etape1 : on crée le masque :
mask = data["geoId"] == "BE"
# Etape 2 : on applique le masque pour sélectionner les données :
print(data[mask])

# 2ème exemple de filtrage : on filtre les données de façon à ne conserver que les cases >= 1000
mask_cases = data["cases"] >= 1000
print(data[mask_cases])

# -------------------------------------
# create and manipulate columns
# ------------------------------------
# trouver l'"inflection point" (le moment où les contaminations arrêtent d'augmenter de manière exponentielle
# pour cela on calcule le growth ratio entre les nouveaux cas du jours divisés par le nombre de cas du j-1
# si le ratio est >1 ça veut dire qu'on est encore en phase d'augmentation.
# si le ratio est <1 ça veut dire qu'on est en phase de diminution

mask_us = data["geoId"] == "US"

data_us = data[mask_us]
print(data_us)

# on reset l'index pour que les lignes partent à nouveau de 0
data_us = data_us.reset_index(drop=True)
print(data_us.head())

# pour trouver le nombre de cas cumulés, il faut d'abord créer une nouvelle colonne.
# on le fait de la même façon qu'on créerait une nouvelle clé dans un dictionnaire : new key = new column in dataframe
data_us["cumulated_cases"] = 0
print(data_us.head())

# ensuite, on constate que les données sont triées de la plus récente à la plus ancienne.
# pour procéder au calcul des cas cumulés, il nous faut partir de la plus ancienne à la plus récente.
# on va donc inverser l'ordre des lignes en utilisant la fonction range
# Ex avec des chiffres de 0 à 10 :
croissant = [i for i in range(0, 10, 1)]
print(croissant)

decroissant = [i for i in range(9, -1, -1)]  # on commence à 9 et on termine par -1 pour bien obtenir l'index 0
print(decroissant)

# appliquons à notre cas.
# on crée une variable "total_rows" pour prendre en compte la longueur du dataframe

total_rows = len(data_us)

for i in range(total_rows-2, -1, -1):
    data_us.loc[i, "cumulated_cases"] = data_us.loc[i, "cases"] + data_us.loc[i + 1, "cumulated_cases"]

print(data_us)

# on calcule les nouveaux cas de chaque jour dans une nouvelle colonne

data_us["new_cases"] = 0

for i in range(total_rows-2, -1, -1):
    data_us.loc[i, "new_cases"] = data_us.loc[i, "cumulated_cases"] - data_us.loc[i + 1, "cumulated_cases"]

print(data_us.head())

# on va calculer le growth ratio : new_cases du jour / new_cases du jour d'avant

data_us["growth_ratio"] = 0

for i in range(total_rows-2, -1, -1):
    data_us.loc[i, "growth_ratio"] = data_us.loc[i, "new_cases"] / data_us.loc[i + 1, "new_cases"]

print(data_us.head())


# datavisualisation avec pandas

data_us.plot.line(x="dateRep", y="cumulated_cases")


