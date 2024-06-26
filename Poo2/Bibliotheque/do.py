from modules import *


def ajouter_livre(bibliotheque):
    titre = input("Titre du livre: ")
    auteur = input("Auteur du livre: ")
    try:
        nombre_pages = int(input("Nombre de pages: "))
        livre = Livre(titre, auteur, nombre_pages)
        bibliotheque.ajouter_livre(livre)
        print("Livre ajouté avec succès.")
    except ValueError:
        print("Erreur : Nombre de pages invalide."+"\n"+"#"*50)

def inscrire_adherent(bibliotheque):
    nom = input("Nom de l'adhérent: ")
    prenom = input("Prénom de l'adhérent: ")
    id = input("ID de l'adhérent: ")
    adherent = Adherent(nom, prenom, id)
    bibliotheque.inscrire_adherent(adherent)
    print("Adhérent inscrit avec succès."+"\n"+"#"*50)

def emprunter_livre(bibliotheque):
    titre = input("Titre du livre à emprunter: ")
    adherent_id = input("ID de l'adhérent: ")
    bibliotheque.emprunter_livre(titre, adherent_id)

def retourner_livre(bibliotheque):
    titre = input("Titre du livre à retourner: ")
    bibliotheque.retourner_livre(titre)

def afficher_livres(bibliotheque):
    bibliotheque.afficher_livres()

def afficher_adherents(bibliotheque):
    bibliotheque.afficher_adherents()

def sauvegarder_bibliotheque(bibliotheque):
    nom_fichier = input("Nom du fichier de sauvegarde: ")
    bibliotheque.sauvegarder(nom_fichier)

def charger_bibliotheque():
    nom_fichier = input("Nom du fichier à charger: ")
    bibliotheque = Bibliotheque.charger(nom_fichier)
    if bibliotheque is not None:
        return bibliotheque
    else:
        print("Échec du chargement de la bibliothèque.")
        return None