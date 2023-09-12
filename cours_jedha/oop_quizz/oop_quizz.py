class Question:
    def __init__(self, question, choix, answer):
        self.question = question
        self.choix = choix
        self.answer = answer

    def poser_question(self):
        print("QUESTION")
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

            print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
        except ValueError:
            print("ERREUR : Veuillez rentrer uniquement des chiffres")
        return Question.demander_reponse_numerique_utilisateur(self, min, max)


class Questionnaire:
    def __init__(self, questions):
        self.questions = questions

    @staticmethod
    def play_again():
        want_to_play_again = input("Do you want to play again ? (Enter Yes or No) ")
        if want_to_play_again.lower() in ["yes", "y"]:
            score = 0
            questionnaire2 = Questionnaire(list_of_questions).lancer_questionnaire()
        else:
            print("------------------\n Good bye !")
        # exit()

    def lancer_questionnaire(self):
        score = 0
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
                 ("Moscou", "Kiev", "Saint-petersbourg", "Melitopol", "Odessa"), "Kiev")
    )
questionnaire = Questionnaire(list_of_questions).lancer_questionnaire()
