from _datetime import datetime
import person
import seance


def insertCatBillet(cur):
    nom = input("Entrer le nom de la catégorie : ")
    nbPlace = input("Entrer le nombre de place disponibles : ")
    sql = "INSERT INTO CategorieBillet(nom,nbrPlace) VALUES('%s',%s)" % (
        nom, nbPlace)
    print(sql)
    cur.execute(sql)



def deleteCatBillet(cur):
    printCatBillet(cur)
    nom = input("Entrer le nom de la catégorie à supprimer : ")
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
    end = input("Finis ?")


def editCatBillet(cur):
    printCatBillet(cur)
    cat = input("Entrer le nom de la catégorie à modifier : ")
    nom = input("Entrer le nom de la catégorie : ")
    nbrPlace = input("Entrer le nombre de place pour la seance : ")
    sql = "UPDATE CategorieBillet SET nom= '%s', nbrplace = %s WHERE nom= '%s'" % (nom, nbrPlace, cat)
    cur.execute(sql)


def getNumberTicket(cur, cat):
    sql = "SELECT COUNT(*) FROM billet WHERE categorie='" + cat + "'"
    cur.execute(sql)
    row = cur.fetchone()
    return int(row[0])


def isAvailable(cur, cat):
    sql = "SELECT nbrPlace FROM categoriebillet WHERE nom = '" + cat + "'"
    cur.execute(sql)
    row = cur.fetchone()
    nbrPlace = int(row[0])
    if nbrPlace >= getNumberTicket(cur, cat):
        return "true"
    else:
        return "false"


def editCatBillet(cur):
    printCatBillet(cur)
    nom = input("Entrer le nom de la catégorie à modifier : ")
    new_nom = input("Entrer le nouveau nom de la catégorie : ")
    new_nbPlace = input("Entrer le nombre de place disponibles : ")
    sql = "UPDATE CategorieBillet SET nom = '%s', nbrPlace = %s WHERE nom = '%s'" % \
          (new_nom, new_nbPlace, nom)
    print(sql)
    cur.execute(sql)


def insertBillet(cur):
    now = datetime.now()
    date = now.strftime("%Y-%m-%d %H:%M:%S")
    person.printPerson(cur)
    buyer = input("Entrer l'id de la personne achetant le billet : ")
    tarif = input("Entrer le tarif de la place : ")
    printCatBillet(cur)
    cat = input("Entrer le nom de la catégorie : ")
    if isAvailable(cur, cat) == "false":
        print("Catégorie plus disponible : ")
        return 1
    seance.printSeance(cur)
    seanceTargetted = input("Entrer l'id de la séance souhaitée : ")
    sql = "INSERT INTO billet(datecreation, personne, tarif, categorie, seance) VALUES ('%s', '%s', %s, '%s', %s)" % \
          (date, buyer, tarif, cat, seanceTargetted)
    print(sql)
    cur.execute(sql)


def deleteBillet(cur):
    print("Voici les billets :")
    printBillet(cur);
    print("Voici les séances :")
    seance.printSeance(cur)
    date = input("Entrez la date d'achat du billet : ")
    person.printPerson(cur)
    personId = input("Entrer l'id de la personne concernée : ")
    sql = "DELETE FROM billet WHERE datecreation = '%s' AND personne = %s" % (date, personId)
    cur.execute(sql)


def printBillet(cur):
    sql = "SELECT * FROM billet GROUP BY seance,datecreation,personne,tarif, categorie"
    cur.execute(sql)
    print("[date] IdAcheteur tarif Catégorie idSeance")
    raw = cur.fetchone()
    while raw:
        print("[" + str(raw[0]) + "] " + str(raw[1]) + " " + str(raw[2]) + " " + str(raw[3]) + " " + str(raw[4]))
        raw = cur.fetchone()
    end = input("Finis ?")



def editBillet(cur):
    printBillet(cur)
    seance.printSeance(cur)
    dateEdited = input("Entrer la date d'Achat du billet concerné : ")
    person.printPerson(cur)
    personID = input("Entrer l'ID de la personne concernée : ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    person.printPerson(cur)
    buyer = input("Entrer l'id de la personne achetant le billet : ")
    tarif = input("Entrer le tarif de la place : ")
    printCatBillet(cur)
    cat = input("Entrer le nom de la catégorie : ")
    if isAvailable(cur, cat) == "false":
        print("Catégorie plus disponible")
        return 1
    seance.printSeance(cur)
    seanceTargetted = input("Entrer l'id de la séance souhaitée :")
    sql = "UPDATE billet SET datecreation= '%s', personne = %s, tarif = %s, categorie = '%s', seance = %s WHERE personne = %s AND datecreation = '%s'" % \
          (date, buyer, tarif, cat, seanceTargetted, personID, dateEdited)
    print(sql)
    cur.execute(sql)