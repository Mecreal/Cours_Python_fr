from modules import *
from screen import *
from do import *

def main():
    bibliotheque = Bibliotheque()
    bibliotheque.initialiser_bibliotheque()

    while True:
        afficher_menu()
        choix = input("Choisissez une option: ")

        if choix == '1':
            ajouter_livre(bibliotheque)
        elif choix == '2':
            inscrire_adherent(bibliotheque)
        elif choix == '3':
            emprunter_livre(bibliotheque)
        elif choix == '4':
            retourner_livre(bibliotheque)
        elif choix == '5':
            afficher_livres(bibliotheque)
        elif choix == '6':
            afficher_adherents(bibliotheque)
        elif choix == '7':
            sauvegarder_bibliotheque(bibliotheque)
        elif choix == '8':
            nouvelle_bibliotheque = charger_bibliotheque()
            if nouvelle_bibliotheque:
                bibliotheque = nouvelle_bibliotheque
        elif choix == '9':
            print("Merci d'avoir utilisé le système de bibliothèque. Au revoir!")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")