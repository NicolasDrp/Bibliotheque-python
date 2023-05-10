livre = [
    {
        "Titre": "Batman",
        "Auteur": "Alfredo"
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
        if titre.lower() in i["Titre"].lower():
            print(i["Titre"]+" : "+i["Auteur"])

# Fonction qui permet à l'utilisateur de trier les livres de la bibliotheque a partir de leurs titres ou leurs auteurs


def Trier_livre_type(type):
    longueur = len(livre)
    for i in range(longueur):
        for j in range(longueur-i-1):
            if livre[j][type] > livre[j+1][type]:
                livre[j], livre[j+1] = livre[j+1], livre[j]

    print(f"Tri des livres par {type} :")
    afficher_livres()

# Fonction qui permet à l'utilisateur de choisir si il veut continuer ou arreter le programme


def choix_menu():
    choix = 0
    while choix == 0 or choix < 1 or choix > 2:
        try:
            print("___________________________________________________________________")
            print("|----------------------Choisissez une option----------------------|")
            print("|-------------------1) Retrourner au menu principal---------------|")
            print("|-------------------2) Arrêter le programme-----------------------|")
            print("|_________________________________________________________________|")
            choix = int(input())
            if choix == 1:
                menu()
        except:
            print("Veuillez rentrer un chiffre valide")


# Fonction principal qui permet à l'utilisateur de choisir quel action il veut effectuer
def menu():

    choix = 0
    while choix ==0 or choix < 1 or choix > 5:
        try:
            print("___________________________________________________________________")
            print("|----------------------Choisissez une option----------------------|")
            print("|-------------------1) Afficher tout les livres-------------------|")
            print("|-------------------2) Ajouter un livre---------------------------|")
            print("|-------------------3) Supprimer un livre-------------------------|")
            print("|-------------------4) Rechercher un livre------------------------|")
            print("|-------------------5) Trier les livres---------------------------|")
            print("|_________________________________________________________________|")
            choix = int(input())
        except:
            print("Veuillez rentrer un chiffre valide")


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
                choix = int(
                    input("Voulez-vous trier par :\n1) Titre\n2) Auteur"))
                if choix == 1:
                    Trier_livre_type("Titre")
                else:
                    Trier_livre_type("Auteur")
            choix_menu()


menu()
