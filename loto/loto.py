from random import randint


class Loto:
    """ Classe représentant un tirage de boule au loto """

    def __init__(self):
        """ Définit nombre de numéros possibles"""

    @staticmethod
    def roll1(num_numbers=50):
        """ Retourne une valeur aléatoire entre 1 et num_numbers"""
        return randint(1, num_numbers)

    @staticmethod
    def roll2(num_numbers=13):
        """ Retourne une valeur aléatoire entre 1 et num_numbers"""
        return randint(1, num_numbers)
