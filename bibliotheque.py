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


def ajouter_livre(titre,auteur):
    livre.append({"Titre": titre,
        "Auteur": auteur})

def supprimer_livre(titre):
    for i in livre:
        if i["Titre"] == titre:
            livre.remove(i)

def Rechercher_livre_titre(titre):
    for i in livre:
        if i["Titre"].lower() == titre.lower():
            print(i["Titre"]+" : "+i["Auteur"])

def Trier_livre_titre():
    longueur = len(livre)
    for i in range(longueur):
        for j in range(longueur-i-1):
            if livre[j]["Titre"] > livre[j+1]["Titre"] :
                livre[j], livre[j+1] = livre[j+1], livre[j]

    print(f"Tri du tableau par titre: {livre}")

def Trier_livre_auteur():
    longueur = len(livre)
    for i in range(longueur):
        for j in range(longueur-i-1):
            if livre[j]["Auteur"] > livre[j+1]["Auteur"] :
                livre[j], livre[j+1] = livre[j+1], livre[j]

    print(f"Tri du tableau par auteur: {livre}")

choix = int(input())

def menu():
    match choix:
        case 1:
             afficher_livres()
        case 2:
            titre = input("Nom du livre:")
            auteur = input("Auteur du livre:")
            ajouter_livre(titre,auteur)
        case 3:
            titre = input("Nom du livre que vous souhaitez supprimer:")
            supprimer_livre(titre)
        case 4:
            titre = input("Nom du livre que vous souhaitez rechercher:")
            Rechercher_livre_titre(titre)
        case 5:
            Trier_livre_titre()
            Trier_livre_auteur()