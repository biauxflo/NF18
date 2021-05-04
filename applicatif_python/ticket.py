def insertCatBillet(cur):
    nom = input("Entrer le nom de la catégorie")
    nbPlace = input("Entrer le nombre de place disponibles")
    sql = "INSERT INTO CategorieBillet(nom,nbrPlace) VALUES('%s',%s)" % (
        nom, nbPlace)
    print(sql)
    cur.execute(sql)



def deleteCatBillet(cur):
    nom = input("Entrer le nom de la catégorie à supprimer")
    sql = "DELETE FROM CategorieBillet WHERE nom = '%s'" % nom
    print(sql)
    cur.execute(sql)


def printCatBillet(cur):
    sql = "SELECT * FROM CategorieBillet GROUP BY nom,nbrPlace ORDER BY nbrPlace;"
    cur.execute(sql)
    print("nom | nombre de place")
    raw = cur.fetchone()
    while raw:
        print(raw[0] + "|" + str(raw[1]))
        raw = cur.fetchone()


def editCatBillet(cur):
    printCatBillet(cur)
    nom = input("Entrer le nom de la catégorie à modifier")
    new_nom = input("Entrer le nouveau nom de la catégorie")
    new_nbPlace = input("Entrer le nombre de place disponibles")
    sql = "UPDATE CategorieBillet SET nom = '%s', nbrPlace = %s WHERE nom = '%s'" % \
          (new_nom,new_nbPlace,nom)
    print(sql)
    cur.execute(sql)