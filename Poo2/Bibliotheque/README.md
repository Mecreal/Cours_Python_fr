Voici un exemple de fichier README en français pour ce projet :

---

# Système de Gestion de Bibliothèque

Ce projet est un système de gestion de bibliothèque simple en Python, permettant d'ajouter des livres, d'inscrire des adhérents, d'emprunter et de retourner des livres, et de sauvegarder et charger l'état de la bibliothèque.

## Fonctionnalités

- Ajouter des livres à la bibliothèque.
- Inscrire de nouveaux adhérents.
- Emprunter des livres.
- Retourner des livres empruntés.
- Afficher tous les livres disponibles.
- Afficher tous les adhérents inscrits.
- Sauvegarder l'état actuel de la bibliothèque dans un fichier.
- Charger l'état de la bibliothèque à partir d'un fichier de sauvegarde.

## Prérequis

- Python 3.x

## Installation

1. Clonez le dépôt dans votre répertoire local :

    ```bash
    git clone https://votre-url-depot.git
    cd votre-repertoire-depot
    ```

2. Assurez-vous d'avoir Python 3.x installé sur votre machine.

## Utilisation

Pour exécuter l'application, lancez le fichier `main.py` :

```bash
python main.py
```

Le programme affichera un menu interactif avec les options suivantes :

```plaintext
Menu de la Bibliothèque
1. Ajouter un livre
2. Inscrire un adhérent
3. Emprunter un livre
4. Retourner un livre
5. Afficher tous les livres
6. Afficher tous les adhérents
7. Sauvegarder l'état de la bibliothèque
8. Charger l'état de la bibliothèque
9. Quitter
```

Suivez les instructions à l'écran pour effectuer les différentes opérations.

## Fichiers du Projet

- `main.py` : Point d'entrée principal de l'application.
- `router.py` : Contient la logique principale et l'appel des fonctions.
- `screen.py` : Contient la fonction d'affichage du menu.
- `do.py` : Contient les fonctions pour chaque option du menu (ajouter un livre, inscrire un adhérent, etc.).
- `modules.py` : Contient les définitions des classes `Livre`, `Adherent`, et `Bibliotheque`.

## Exemple d'Initialisation

L'application initialise automatiquement la bibliothèque avec quelques livres et adhérents par défaut pour vous permettre de commencer rapidement :

```python
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
```

## Contribution

Les contributions sont les bienvenues ! Veuillez soumettre des demandes de tirage (pull requests) ou signaler des problèmes (issues) sur le dépôt GitHub.

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

---

Ce fichier README fournit une vue d'ensemble du projet, ses fonctionnalités, des instructions d'installation et d'utilisation, ainsi que des informations sur la contribution et la licence.
