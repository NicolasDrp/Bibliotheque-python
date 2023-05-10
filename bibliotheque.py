livre = [
    {
        "Titre": "Batman",
        "Auteur": "Kelkun"
    },
    {
        "Titre": "Akhy potter",
        "Auteur": "JK kholings"
    }
]

# Fonction qui permet à l'utilisateur d'afficher les livres disponnible
def afficher_livres():
    for i in livre:
        print(i["Titre"]+" : "+i["Auteur"])

# Fonction qui permet à l'utilisateur d'ajouter un livre à la bibliotheque
def ajouter_livre(titre, auteur):
    livre.append({"Titre": titre,
                  "Auteur": auteur})

# Fonction qui permet à l'utilisateur de supprimer un livre de la bibliotheque
def supprimer_livre(titre):
    for i in livre:
        if i["Titre"].lower() == titre.lower():
            livre.remove(i)

# Fonction qui permet à l'utilisateur de rechercher un livre dans la bibliotheque a partir de son titre
def Rechercher_livre_titre(titre):
    for i in livre:
        if i["Titre"].lower() == titre.lower():
            print(i["Titre"]+" : "+i["Auteur"])

# Fonction qui permet à l'utilisateur de trier les livres de la bibliotheque a partir de leurs titres
def Trier_livre_titre():
    longueur = len(livre)
    for i in range(longueur):
        for j in range(longueur-i-1):
            if livre[j]["Titre"] > livre[j+1]["Titre"]:
                livre[j], livre[j+1] = livre[j+1], livre[j]

    print(f"Tri des livres par titre: {livre}")

# Fonction qui permet à l'utilisateur de trier les livres de la bibliotheque a partir de leurs auteurs
def Trier_livre_auteur():
    longueur = len(livre)
    for i in range(longueur):
        for j in range(longueur-i-1):
            if livre[j]["Auteur"] > livre[j+1]["Auteur"]:
                livre[j], livre[j+1] = livre[j+1], livre[j]

    print(f"Tri des livres par auteur: {livre}")

# Fonction qui permet à l'utilisateur de choisir si il veut continuer ou arreter le programme
def choix_menu():
    choix = 0
    while choix < 1 or choix > 2:
        print("___________________________________________________________________")
        print("|----------------------Choisissez une option----------------------|")
        print("|-------------------1) Retrourner au menu principal---------------|")
        print("|-------------------2) Arrêter le programme-----------------------|")
        print("|_________________________________________________________________|")
        choix = int(input())
        if choix == 1:
            menu()


# Fonction principal qui permet à l'utilisateur de choisir quel action il veut effectuer
def menu():

    choix = 0
    while choix < 1 or choix > 5:
        print("___________________________________________________________________")
        print("|----------------------Choisissez une option----------------------|")
        print("|-------------------1) Afficher tout les livres-------------------|")
        print("|-------------------2) Ajouter un livre---------------------------|")
        print("|-------------------3) Supprimer un livre-------------------------|")
        print("|-------------------4) Rechercher un livre------------------------|")
        print("|-------------------5) Trier les livres---------------------------|")
        print("|_________________________________________________________________|")

        choix = int(input())

    match choix:
        case 1:
            afficher_livres()
            choix_menu()
        case 2:
            titre = input("Nom du livre:")
            auteur = input("Auteur du livre:")
            ajouter_livre(titre, auteur)
            choix_menu()
        case 3:
            titre = input("Nom du livre que vous souhaitez supprimer:")
            supprimer_livre(titre)
            choix_menu()
        case 4:
            titre = input("Nom du livre que vous souhaitez rechercher:")
            Rechercher_livre_titre(titre)
            choix_menu()
        case 5:
            choix = 0
            while choix < 1 or choix > 2:
                choix = int(input("Voulez-vous trier par :\n1) Titre\n2) Auteur"))
                if choix == 1:
                    Trier_livre_titre()
                else:
                    Trier_livre_auteur()
            choix_menu()


menu()
