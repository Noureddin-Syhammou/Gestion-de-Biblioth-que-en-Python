from datetime import datetime

class Livre:
    def __init__(self,titre,auteur,genre,statut="Disponible"):
        self.titre = titre
        self.auteur = auteur
        self.genre = genre
        self.statut = statut  
        self.next = None  

class ListeLivres:
    def __init__(self):
        self.head = None

    def ajouter_livre(self,arbre_biblio):
        titre = input("Titre du livre : ")
        auteur = input("Auteur du livre : ")
        genre = input("Genre du livre : ")
        
        # verification ci le livre deja exeste 
        current = self.head
        while current:
            if current.titre == titre:
                print("\n***Ce livre est déja existe dans la bibiotheque!!***")
                return
            current = current.next
            
        nouveau_livre = Livre(titre, auteur, genre) 
        nouveau_livre.next = self.head
        self.head = nouveau_livre
        
        # Ajouter le livre à l'arbre
        arbre_biblio.ajouter(nouveau_livre)
        
        print(f"le livre \"{titre}\" a été ajouter.")

    def afficher_livres(self):
        current = self.head
        if not current:
            print("Aucun livre dans la bibliothèque.")
            return
        n = 1
        while current:
            print(f"Le livre {n} ==> nom :{current.titre}, genre : {current.genre}, l'auteur : {current.auteur}, status : {current.statut}.")
            current = current.next
            n += 1

    def supprimer_livre(self):
        titre = input("Titre du livre à supprimer : ")
        current = self.head
        previous = None
        while current:
            if current.titre == titre:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                print(f"Le livre \"{titre}\" a été supprimé.")
                return
            previous = current
            current = current.next
        print("Livre non trouvé!!!.")

    def afficher_livres_disponibles(self):
        current = self.head
        n = 1
        if not current:
            print("\n*** Pas de livre disponible!!! ***")
        else:
            print("\n==== Les livre disponibles ====")
            while current:
                if current.statut == "Disponible":
                    print(f"le livre {n} ==> nom : {current.titre}")
                    n += 1
                current = current.next
        


class PileEmprunts:
    def __init__(self,liste_bibliotheque):
        self.pile = []
        self.historique = []
        self.liste_bibliotheque = liste_bibliotheque  

    def emprunter_livre(self):
        titre = input("Titre du livre emprunté : ")
        
        current = self.liste_bibliotheque.head
        livre_trouve = False
        while current:
            if current.titre == titre and current.statut == "Disponible":
                livre_trouve = True
                break
            current = current.next
        
        if livre_trouve:
            date = datetime.now()
            self.pile.append((titre, date))
            self.historique.append((titre, date))
            print(f"Emprunt enregistré : {titre} ({date})")
            
            current.statut = "Emprunté"
        else:
            print("\n*** Le livre n'est pas disponible ou n'existe pas!!! ***")

    def retourner_livre(self):
        if self.pile:
            livre = self.pile.pop()
            print(f"Livre retourné : {livre[0]}")
            
            # Recherche du livre dans la liste pour remettre son statut à "Disponible"
            current = self.liste_bibliotheque.head
            while current:
                if current.titre == livre[0]:
                    current.statut = "Disponible"
                    break
                current = current.next
        else:
            print("\n*** Aucun emprunt à retourner!!! ***")

    def afficher_livres_emprenter(self):
        if not self.pile:
            print("\n*** Aucun emprunt enregistré!!! ***")
            return
        print("Les livres emprunts :")
        for titre, date in reversed(self.pile):
            print(f"{titre} emprunté le {date}")

    def afficher_historique_emprenter(self):
        if self.historique == []:
            print("\n*** Aucun historique a afficher!!! ***")
        else:
            for titre, date in reversed(self.historique):
                print(f"{titre} emprunté le {date}")


class Noeud:
    def __init__(self, livre):
        self.livre = livre
        self.gauche = None
        self.droite = None

class ArbreBibliotheque:
    def __init__(self):
        self.racine = None

    def ajouter(self, livre):
        if self.racine is None:
            self.racine = Noeud(livre)
        else:
            courant = self.racine
            while True:
                if livre.titre.lower() < courant.livre.titre.lower() :
                    if courant.gauche is None:
                        courant.gauche = Noeud(livre)
                        break
                    courant = courant.gauche
                else:
                    if courant.droite is None:
                        courant.droite = Noeud(livre)
                        break
                    courant = courant.droite
    
        print(f"Livre ajouté dans l'arbre : {livre.titre}")

    def rechercher(self):
        titre = input("Titre du livre à rechercher : ")
        courant = self.racine

        while courant:
            if titre == courant.livre.titre:
                print(f"Livre trouvé => titre : {courant.livre.titre} auteur : {courant.livre.auteur} genre : {courant.livre.genre} status : {courant.livre.statut}")
                return
            if titre < courant.livre.titre:
                courant = courant.gauche
            else:
                courant = courant.droite

        print("\n*** Livre non trouvé !!! ***")


    def afficher_ordre_alphabetique(self):
        courant = self.racine
        pile = []

        print("Livres triés par ordre alphabétique :")

        while pile or courant:
            if courant:
                pile.append(courant)
                courant = courant.gauche
            else:
                courant = pile.pop()
                print(f"{courant.livre.titre} - {courant.livre.auteur} ({courant.livre.genre}) [{courant.livre.statut}]")
                courant = courant.droite


# Exécution du programme
bibliotheque = ListeLivres()
historique_emprunts = PileEmprunts(bibliotheque)
arbre_biblio = ArbreBibliotheque()

while True:
    print("\n=================== MENU ========================")
    print("1. Ajouter un livre")
    print("2. Supprimer un livre")
    print("3. Afficher les livres")
    print("4. Emprunter un livre")
    print("5. Retourner un livre")
    print("6. Afficher les livres disponibles")
    print("7. Afficher les livres emprenter")
    print("8. Afficher l'historique d'empenter")
    print("9. Rechercher un livre")
    print("10. Afficher les livres triés")
    print("0. Quitter")
    choix = input("Choisissez une option : ")

    if choix == "1":
        bibliotheque.ajouter_livre(arbre_biblio)
    elif choix == "2":
        bibliotheque.supprimer_livre()
    elif choix == "3":
        bibliotheque.afficher_livres()
    elif choix == "4":
        historique_emprunts.emprunter_livre()
    elif choix == "5":
        historique_emprunts.retourner_livre()
    elif choix == "6":
        bibliotheque.afficher_livres_disponibles()
    elif choix == "7":
        historique_emprunts.afficher_livres_emprenter()
    elif choix == "8":
        historique_emprunts.afficher_historique_emprenter()
    elif choix == "9":
        arbre_biblio.rechercher()
    elif choix == "10":
        arbre_biblio.afficher_ordre_alphabetique()
    elif choix == "0":
        break
    else:
        print("Option invalide, réessayez.")
