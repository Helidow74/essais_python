from loto import Loto
from plotly.graph_objs import Bar, Layout
from plotly import offline

results = []


def tirage_num():
    result_tirage = []
    result_tirage2 = []

    for nombre_tirage in range(5):
        result = tirage.roll1()
        while len(result_tirage) < 5:
            if result not in result_tirage:
                result_tirage.append(result)
            else:
                result = tirage.roll1()
    for nombre_tirage in range(2):
        result = tirage.roll2()
        while len(result_tirage2) < 2:
            if result not in result_tirage2:
                result_tirage2.append(result)
            else:
                result = tirage.roll2()
    return result_tirage, result_tirage2


# ------------------------------
# nombre de tirages à simuler :
for x in range(10000):
    tirage = Loto()
    serie = tirage_num()
    results.append(serie)

# print(results)


# -------------------------------
# analyser les résultats :
princ_num_results = []
comp_num_results = []

for princ, comp in results:
    princ_num = princ
    comp_num = comp
    princ_num_results.append(princ_num)
    comp_num_results.append(comp_num)

    # print(princ, comp)
    # print(princ_num_results)
    # print(comp_num_results)

# ----------------------------
# on aplatit les listes imbriquées pour pouvoir ensuite calculer les fréquences de valeurs :
flat_list_princ = [item for item in princ_num_results for item in item]
# print(flat_list_princ)

flat_list_comp = [item for item in comp_num_results for item in item]
# print(flat_list_comp)

# ------------------------------
# calcul des fréquences de valeurs pour numéros principaux :
frequencies_princ = []

for value in range(1, 51):
    frequency_princ = flat_list_princ.count(value)
    frequencies_princ.append(frequency_princ)
# print(frequencies_princ)

# ----------------------------
# calcul des fréquences de valeurs pour numéros complémentaires :
frequencies_comp = []

for value in range(1, 13):
    frequency_comp = flat_list_comp.count(value)
    frequencies_comp.append(frequency_comp)
# print(frequencies_comp)

# -------------------------------
# Visualiser les résultats :
# ------------------------------

# 1) pour les nombres principaux :
x_values = list(range(1, 51))
data = [Bar(x=x_values, y=frequencies_princ)]

x_axis_config = {'title': 'Résultat'}
y_axis_config = {'title': 'Fréquence du résultat'}

my_layout = Layout(title='Résultats des tirages des numéros principaux', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='princ.html')

# ------------------------------
# 2) pour les nombres complémentaires :
x_values = list(range(1, 13))
data = [Bar(x=x_values, y=frequencies_comp)]

x_axis_config = {'title': 'Résultat'}
y_axis_config = {'title': 'Fréquence du résultat'}

my_layout = Layout(title='Résultats des tirages des numéros complémentaires', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='comp.html')

# -----------------------------
# A voir : calculer les fréquences à partir des fichiers CSV de la française des jeux et visualiser les résultats.
