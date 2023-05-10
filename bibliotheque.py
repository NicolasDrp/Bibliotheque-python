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


def afficher_livres():
    for i in livre:
        print(i["Titre"]+" : "+i["Auteur"])


def ajouter_livre(titre, auteur):
    livre.append({"Titre": titre,
                  "Auteur": auteur})


def supprimer_livre(titre):
    for i in livre:
        if i["Titre"].lower() == titre.lower():
            livre.remove(i)


def Rechercher_livre_titre(titre):
    for i in livre:
        if i["Titre"].lower() == titre.lower():
            print(i["Titre"]+" : "+i["Auteur"])


def Trier_livre_titre():
    longueur = len(livre)
    for i in range(longueur):
        for j in range(longueur-i-1):
            if livre[j]["Titre"] > livre[j+1]["Titre"]:
                livre[j], livre[j+1] = livre[j+1], livre[j]

    print(f"Tri des livres par titre: {livre}")


def Trier_livre_auteur():
    longueur = len(livre)
    for i in range(longueur):
        for j in range(longueur-i-1):
            if livre[j]["Auteur"] > livre[j+1]["Auteur"]:
                livre[j], livre[j+1] = livre[j+1], livre[j]

    print(f"Tri des livres par auteur: {livre}")


def choix_menu():
    choix = 0
    while choix < 1 or choix > 5:
        choix = int(input("Retourner au menu?\n1) Oui\n2) Non"))
        if choix == 1:
            menu()


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

        choix = int(input("fais choix"))

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
            choix = int(input("Voulez-vous trier par :\n1) Titre\n2) Auteur"))

            Trier_livre_titre()
            Trier_livre_auteur()
            choix_menu()


menu()
