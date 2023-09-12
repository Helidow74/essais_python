# I tried to code a very simple authentication system that gives access to a quizz game
# Quizz code part is in OOP
# ----------------------------------------------------------

# new credentials creation ------------------------
credentials = {}
register = True
access = False


def ask_new_pseudo():
    new_pseudo = input("Entrez un pseudo : ")
    return new_pseudo


def ask_new_password():
    new_password = input("Entrez un mot de passe : ")
    return new_password


def update_credentials(new_pseudo, new_password):
    credentials.update({new_pseudo: new_password})
    return credentials


def add_new_credentials():
    new_pseudo = ask_new_pseudo()
    new_password = ask_new_password()
    update_credentials(new_pseudo, new_password)


def new_register(register_status):
    while register_status:
        add_new_credentials()
        relancer = input("Voulez-vous enregistrer une autre personne ? (O ou N)")
        if relancer.upper() == "O":
            new_register(register_status)
        elif relancer.upper() == "N":
            register_status = False
            menu_launch()
        else:
            print("Cette option ne figure pas dans les choix mais nous la considérons comme un non")
            register_status = False
        return register


def launch_new_register(register_status):
    credentials_new = new_register(register)
    return credentials


# authentication -----------------
def authenticate(access_status):
    while not access_status:

        pseudo_input = input("\nEntrez votre pseudo : ")
        password_input = input("Entrez votre mot de passe : ")

        try:
            pseudo_input.capitalize()
            if password_input == credentials[pseudo_input.capitalize()]:
                access_status = True
                print("\n-----------------------\nConnexion réussie\n-----------------------\n")
                questionnaire = Questionnaire(list_of_questions).lancer_questionnaire()
                return access_status

            else:
                print("\n-----------------------\nAccès refusé \n-----------------------")
                print("wrong password")

        except KeyError:
            print("\n-------------------------------\nERREUR : Ce pseudo n'existe pas\n-------------------------------")
            menu_launch()


# Quizz part in OOP -----------------
class Question:
    def __init__(self, question, choix, answer):
        self.question = question
        self.choix = choix
        self.answer = answer

    def poser_question(self):
        print("      QUESTION")
        print("  " + self.question)
        for i in range(len(self.choix)):
            print("  ", i + 1, "-", self.choix[i])

        print()
        resultat_response_correcte = False
        life = 3
        while life > 0 and not resultat_response_correcte:
            reponse_int = Question.demander_reponse_numerique_utilisateur(self, 1, len(self.choix))
            if self.choix[reponse_int - 1].lower() == self.answer.lower():
                print("Bonne réponse")
                resultat_response_correcte = True
            else:
                print("Mauvaise réponse")
                life -= 1

        print()
        return resultat_response_correcte

    def demander_reponse_numerique_utilisateur(self, min, max):
        reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + ") : ")
        try:
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max:
                return reponse_int

            print("ERREUR : Vous devez entrer un nombre entre", min, "et", max)
        except ValueError:
            print("ERREUR : Veuillez entrer uniquement des chiffres")
        return Question.demander_reponse_numerique_utilisateur(self, min, max)


class Questionnaire:
    def __init__(self, questions):
        self.questions = questions

    @staticmethod
    def play_again():
        want_to_play_again = input("Voulez-vous rejouer ? (Oui ou non) ")
        if want_to_play_again.lower() in ["oui", "0"]:
            score = 0
            questionnaire2 = Questionnaire(list_of_questions).lancer_questionnaire()
        else:
            print("\n-----retour au menu principal : -----\n ")
            menu_launch()
        # exit()

    def lancer_questionnaire(self):
        score = 0
        print("\n*** Début du quizz ***\n")
        for question in self.questions:
            if question.poser_question():
                score += 1
        print("Score final :", score, "sur", len(self.questions))
        self.play_again()
        return score


list_of_questions = (
        Question("Quelle est la capitale de la France ?",
                 ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"),
        Question("Quelle est la capitale de l'Italie ?",
                 ("Rome", "Venise", "Pise", "Florence"), "Rome"),
        Question("Quelle est la capitale de la Belgique ?",
                 ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles"),
        Question("Quelle est la capitale de l'Ukraine ?",
                 ("Moscou", "Kiev", "Saint-petersbourg", "Melitopol", "Odessa"), "Kiev"),
        Question("Quelle est la capitale de la Grèce ?",
                 ("Santorin", "Bruges", "Athènes", "Odessa", "Olympe"), "Athènes")
    )


# main menu --------------------
def menu_launch():
    print("\n** Que voulez-vous faire : **")
    print("--------------------------------")
    print("Tapez 1 pour vous enregistrer")
    print("Tapez 2 pour vous connecter")
    print("Tapez 3 pour sortir du programme")
    menu_choice = input("\nVotre choix : ")

    if menu_choice == "1":
        launch_new_register(register)
    elif menu_choice == "2":
        authenticate(access)
    elif menu_choice == "3":
        print("\n*** Vous êtes déconnecté ***")
        # exit()
    else:
        print("Cette option ne figure pas dans les choix. Sortie du programme.")


# launching ------------------
menu_launch()
