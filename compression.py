#
# Définition des différentes fonctions de ce fichier
#
def compressData(data : str) :
    """compression RLE de data"""
    assert(data.isdigit()==False)
    C = ""
    couleur = data[0]
    nbr = 1
    for i in range(1,len(data)):
        # on a toujours la même couleur qui se répète aussi, on la compte.
        if data[i]==couleur:
            nbr =nbr +1
        else:
            # on change de couleur. On stocke alors la couleur puis la lettre.
            # optimisation au lieu d'écrire 1A on écrit simplement A
            if nbr==1:
                C=C+couleur
                couleur = data[i]
                nbr = 1
            else:
                C=C+str(nbr)+couleur
                couleur = data[i]
                nbr = 1
    #gestion du dernier caractère compressé de la chaine à la fin du document 
    if nbr==1:
        C=C+couleur
    else:
        C=C+str(nbr)+couleur
    return C


def decompressData(data : str) :
    """décompression RLE de data"""
    S =""
    nbr =0
    for i in range(0, len(data)):
        # si c'est un chiffre, on le rajoute au nombre
        if data[i].isdigit():
            nbr = nbr *10 + int(data[i])
        else:
            # on tombe sur une couleur
            if nbr !=0 :
                # rappel python : 'A'*3 donne 'AAA'
                couleur = data[i]*nbr
            else :
                # on est sur le cas ou il y a juste une lettre, nbr=0 
                couleur = data[i]
            nbr=0
            S= S + couleur
    return S



# print(compressData("BBBBBWBWBBBBWBBBBWBBBBBWWWWWWWW"))
# print(compressData("BBBBBWW"))

# import random

# print("Séance de tests compression/décompression")

# for _ in range(500):
#     test = ""
#     for _ in range(500):
#         test = test + random.choice("WB")
#     tested = decompressData(compressData(test))
#     if tested !=test:
#         print(test)

# print("fin de séance de tests")