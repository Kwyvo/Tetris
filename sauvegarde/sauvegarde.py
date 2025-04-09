import json

def recup_donnees(plateau,coord_piece_placer,score,nb_ligne_suppr,niveau,mode_de_jeu):

    """
    Fonction qui récupère les données de la partie dans un dictionnaire
    """

    return {
        "plateau": [[elt if elt!= 1 else 0 for elt in plateau[i]]for i in range(len(plateau))],
        "coord_p": coord_piece_placer,
        "score": score,
        "lignes": nb_ligne_suppr,
        "lvl": niveau,
        "gamemode": mode_de_jeu
    }

def stocker_donnees(dico,fichier):

    """
    Fonction qui stocke les données récupérées par la méthode recup_donnees() dans un fichier json 
    """

    with open(f"sauvegarde/{fichier}","w") as fichier:
        json.dump(dico,fichier)



def charger_donnees(fichier):

    """
    Fonction qui renvoie les données du fichier json (dictionnaire)
    """

    with open(f"sauvegarde/{fichier}", "r") as fichier_save:
        dico = json.load(fichier_save)
    return dico

def recup_donnees_para(vitesse,hauteurFenetre,largeurFenetre):

    """
    Fonction qui récupère les données des parametres dans un dictionnaire
    """

    return {
        "vitesse": vitesse,
        "dimension_fen": (hauteurFenetre,largeurFenetre)
    }

