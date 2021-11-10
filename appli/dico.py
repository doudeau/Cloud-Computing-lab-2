from bucket import downloadResult

dico = downloadResult()

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

def isIn(id):
    for i in dico.keys():
        if i == id:
            return True
    return False

def creationRes(responses,ids) :
    res = []
    for k in range(4) :
        res.append([ids[k],responses[k]])
    return res