from bucket import downloadResult

#initialisation du dictionnaire avec les resultats deja existant sur le bucket
dico = downloadResult()

# Enregistre les reponses et retourne le dictionnaire complété
def response(Tableau):
    for res in Tableau: 
        if (isIn(res[0])):
            if (res[1] == "oui"):
                dico[res[0]][0]+=1
            else:
                dico[res[0]][1]+=1
        else:
            if (res[1] == "oui"):
                dico.update({res[0]:[1,0]})
            else:
                dico.update({res[0]:[0,1]})

    return dico

# retourne true si la photo a déjà des résultats enregistrés, false sinon
def isIn(id):
    for i in dico.keys():
        if i == id:
            return True
    return False

# Retourne un tableau associant les réponses des 4 photos avec leurs noms
def creationRes(responses,ids) :
    res = []
    for k in range(4) :
        res.append([ids[k],responses[k]])
    return res