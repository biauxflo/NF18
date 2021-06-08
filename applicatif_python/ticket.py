from _datetime import datetime
import person
import seance
import room


def insertCatBillet():
    choix = 0
    catBilletJson = '['
    nom = input("Entrer le nom de la catégorie : ")
    nbPlace = input("Entrer le nombre de place disponibles : ")
    catBilletJson += '{"nom" : "' + nom + '", "nbPersonne": "' + nbPlace + '"}'
    while choix != 2:
        choix = int(input(
            "Que voulez vous faire ? \n 1 - Entrez une nouvelle catégorie \n 2 - Retour à la création des séances\n"))
        if choix == 1:
            catBilletJson += ','
            nom = input("Entrer le nom de la catégorie : ")
            nbPlace = input("Entrer le nombre de place disponibles : ")
            catBilletJson += '{"nom" : "' + nom + '", "nbPersonne": "' + nbPlace + '"}'
    catBilletJson += ']'
    return catBilletJson


def printCatBillet(cur):
    sql = "SELECT * FROM v_catbillet"
    cur.execute(sql)
    print("nom du spectacle | nom | nombre de place")
    raw = cur.fetchone()
    while raw:
        print(raw[0] + "|" + str(raw[1]) + "|" + str(raw[2]))
        raw = cur.fetchone()
    end = input("Finis ?")


def getNumberTicket(cur, cat):
    sql = "SELECT COUNT(*) FROM billet WHERE categorie='" + cat + "'"
    cur.execute(sql)
    row = cur.fetchone()
    return int(row[0])


def isAvailable(cur, cat):
    sql = "SELECT nbPersonne FROM v_catbillet WHERE nom = '" + cat + "'"
    cur.execute(sql)
    row = cur.fetchone()
    nbrPlace = int(row[0])
    if nbrPlace >= getNumberTicket(cur, cat):
        return "true"
    else:
        return "false"


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
    if room.getAvailable(cur, seanceTargetted) == "false":
        print("Erreur : Salle pleine.")
        return 1
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
