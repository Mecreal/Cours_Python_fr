import pickle

class Livre:
    """
    Représente un livre dans la bibliothèque.

    Attributs:
        titre (str): Le titre du livre.
        auteur (str): L'auteur du livre.
        pages (int): Le nombre de pages du livre.
        est_emprunte (bool): Indique si le livre est emprunté.
    """

    def __init__(self, titre, auteur, pages):
        self.titre = titre
        self.auteur = auteur
        self.pages = pages
        self.est_emprunte = False

    def afficher_infos(self):
        """
        Affiche les informations du livre.
        """
        etat = "Emprunté" if self.est_emprunte else "Disponible"
        print(f"Titre: {self.titre}, Auteur: {self.auteur}, Pages: {self.pages}, État: {etat}"+"\n"+"#"*50)

class Adherent:
    """
    Représente un adhérent de la bibliothèque.

    Attributs:
        nom (str): Le nom de l'adhérent.
        prenom (str): Le prénom de l'adhérent.
        id_adherent (str): L'identifiant de l'adhérent.
    """

    def __init__(self, nom, prenom, id_adherent):
        self.nom = nom
        self.prenom = prenom
        self.id_adherent = id_adherent

    def afficher_adherent(self):
        """
        Affiche les informations de l'adhérent.
        """
        print(f"Adhérent ID: {self.id_adherent}, Nom: {self.nom}, Prénom: {self.prenom}"+"\n"+"#"*50)

class Bibliotheque:
    """
    Représente une bibliothèque.

    Attributs:
        livres (list): La liste des livres dans la bibliothèque.
        adherents (list): La liste des adhérents inscrits à la bibliothèque.
    """

    def __init__(self):
        self.livres = []
        self.adherents = []

    def ajouter_livre(self, livre):
        """
        Ajoute un livre à la bibliothèque.

        Args:
            livre (Livre): Le livre à ajouter.
        """
        self.livres.append(livre)
        print(f"Livre '{livre.titre}' ajouté à la bibliothèque."+"\n"+"#"*50)

    def inscrire_adherent(self, adherent):
        """
        Inscrit un nouvel adhérent à la bibliothèque.

        Args:
            adherent (Adherent): L'adhérent à inscrire.
        """
        self.adherents.append(adherent)
        print(f"Adhérent '{adherent.nom} {adherent.prenom}' inscrit avec ID {adherent.id_adherent}."+"\n"+"#"*50)

    def emprunter_livre(self, titre, adherent_id):
        """
        Emprunte un livre de la bibliothèque.

        Args:
            titre (str): Le titre du livre à emprunter.
            adherent_id (str): L'identifiant de l'adhérent qui emprunte le livre.
        """
        for livre in self.livres:
            if livre.titre == titre and not livre.est_emprunte:
                livre.est_emprunte = True
                print(f"Livre '{titre}' emprunté par l'adhérent ID {adherent_id}."+"\n"+"#"*50)
                return
        print(f"Livre '{titre}' non disponible ou inexistant."+"\n"+"#"*50)

    def retourner_livre(self, titre):
        """
        Retourne un livre emprunté à la bibliothèque.

        Args:
            titre (str): Le titre du livre à retourner.
        """
        for livre in self.livres:
            if livre.titre == titre and livre.est_emprunte:
                livre.est_emprunte = False
                print(f"Livre '{titre}' retourné."+"\n"+"#"*50)
                return
        print(f"Livre '{titre}' non trouvé ou n'a pas été emprunté.")

    def afficher_livres(self):
        """
        Affiche la liste des livres dans la bibliothèque.
        """
        if not self.livres:
            print("Aucun livre dans la bibliothèque."+"\n"+"#"*50)
        else:
            for livre in self.livres:
                livre.afficher_infos()

    def afficher_adherents(self):
        """
        Affiche la liste des adhérents inscrits.
        """
        if not self.adherents:
            print("Aucun adhérent inscrit."+"\n"+"#"*50)
        else:
            for adherent in self.adherents:
                adherent.afficher_adherent()

    def sauvegarder(self, nom_fichier):
        """
        Sauvegarde l'état de la bibliothèque dans un fichier.

        Args:
            nom_fichier (str): Le nom du fichier de sauvegarde.
        """
        try:
            with open(nom_fichier, 'wb') as fichier:
                pickle.dump(self, fichier)
            print(f"Bibliothèque sauvegardée dans le fichier '{nom_fichier}'."+"\n"+"#"*50)
        except Exception as e:
            print(f"Erreur lors de la sauvegarde de la bibliothèque : {e}")

    @staticmethod
    def charger(nom_fichier):
        """
        Charge l'état de la bibliothèque depuis un fichier.

        Args:
            nom_fichier (str): Le nom du fichier de sauvegarde.

        Returns:
            Bibliotheque: Une instance de la bibliothèque chargée depuis le fichier.
        """
        try:
            with open(nom_fichier, 'rb') as fichier:
                bibliotheque = pickle.load(fichier)
            print(f"Bibliothèque chargée depuis le fichier '{nom_fichier}'.")
            return bibliotheque
        except FileNotFoundError:
            print(f"Fichier '{nom_fichier}' non trouvé."+"\n"+"#"*50)
        except Exception as e:
            print(f"Erreur lors du chargement de la bibliothèque : {e}")
        return None
    
    
    def initialiser_bibliotheque(bibliotheque):
        """
        Initialise la bibliothèque avec quelques livres et adhérents.

        Args:
            bibliotheque (Bibliotheque): L'instance de la bibliothèque à initialiser.
        """
        livres = [
            Livre("1984", "George Orwell", 328),
            Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 96),
            Livre("Les Misérables", "Victor Hugo", 1488)
        ]

        adherents = [
            Adherent("Dupont", "Jean", "A001"),
            Adherent("Durand", "Marie", "A002"),
            Adherent("Martin", "Pierre", "A003")
        ]

        for livre in livres:
            bibliotheque.ajouter_livre(livre)

        for adherent in adherents:
            bibliotheque.inscrire_adherent(adherent)