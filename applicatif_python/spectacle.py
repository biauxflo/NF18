import association
import person
import seance

def insertSpectacle(cur):
    nomSpectacle = input("Quel est le nom du spectacle ? ")
    dureeSpectacle = input("Quel est la durée du Spectacle ? Format HH:MM:SS ")
    association.printAsso(cur)
    nomAsso = input("Quel est le nom de l'association gérant ce spectacle ? ")
    print("Quel type de spectacle voulez vous ajouter ? \n 1 - Concert \n 2 - Théâtre \n 3 - Stand-Up")
    typeSpectacle = -1
    while typeSpectacle < 1 or typeSpectacle > 3:
        typeSpectacle = int(input("Choix : "))
    if typeSpectacle == 1:
        typeSpectacle = "concert"
        compositeur = input("Qui est le compositeur ? ")
        anneeParution = input("Quelle est l'année de parution ? FORMAT: YYYY-MM-DD ")
        genreConcert = input("Quel est le genre de musique jouée ? ")
        print("CREATION DE SEANCES : ")
        seancesJson = seance.insertSeance(cur)
        sql = "INSERT INTO spectacle(nom, duree, typespectacle, compositeur,anneeparution,genreconcert, association, seances) " \
              "VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" \
              % (nomSpectacle, dureeSpectacle, typeSpectacle, compositeur, anneeParution, genreConcert, nomAsso, seancesJson)
        print(sql)
        cur.execute(sql)
    if typeSpectacle == 2:
        typeSpectacle = "piece de theatre"
        auteur = input("Qui est l'auteur de cette pièce ? ")
        dateParution = input("Quand est paru cette pièce ? FORMAT YYYY-MM-DD ")
        typePiece = input("Quel est le genre de cette pièce: ")
        print("CREATION DE SEANCES : ")
        seancesJson = seance.insertSeance(cur)
        sql = "INSERT INTO spectacle(nom, duree, typespectacle, anneeparution, auteur, typetheatre, association, seances) VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" \
              % (nomSpectacle, dureeSpectacle, typeSpectacle, dateParution, auteur, typePiece, nomAsso, seancesJson)
        print(sql)
        cur.execute(sql)
    if typeSpectacle == 3:
        typeSpectacle = "stand-up"
        genreStandUp = 0
        print("Quel est le genre de ce stand-up ?\n 1 - spectacle comique \n 2 - debat \n 3 - table ronde \n 4 - Aucun des 3")
        while genreStandUp < 1 or genreStandUp > 4:
            genreStandUp = int(input("Choix : "))
        if genreStandUp == 1:
            genreStandUp = "spectacle comique"
        if genreStandUp == 2:
            genreStandUp = "debat"
        if genreStandUp == 3:
            genreStandUp = "table ronde"
        if genreStandUp == 4:
            genreStandUp = "NULL"
        print("CREATION DE SEANCES : ")
        seancesJson = seance.insertSeance(cur)
        sql = "INSERT INTO spectacle(nom, duree, typespectacle, genrestandup, association, seances) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" \
              % (nomSpectacle, dureeSpectacle, typeSpectacle, genreStandUp, nomAsso, seancesJson)
        print(sql)
        cur.execute(sql)


def deleteSpectacle(cur):
    printSpectacle(cur)
    nomSpectacle = input("Quel est le nom du spectacle à supprimer ?")
    sql = "DELETE FROM spectacle WHERE nom = '%s'" % nomSpectacle
    print(sql)
    cur.execute(sql)
    return 0


def printSpectacle(cur):
    sql = "SELECT * FROM SPECTACLE GROUP BY nom, typespectacle"
    cur.execute(sql)
    print("nom, duree, compositeur, annee, parution, genre du concert, auteur, genre de la pièce, genre du Stand-up, association gérante")
    raw = cur.fetchone()
    while raw:
        print(str(raw[0]) + ", " + str(raw[1]) + "," + str(raw[2]) + "," + str(raw[3]) + "," + str(raw[4]) + ", " + str(raw[5])
              + "," + str(raw[6]) + "," + str(raw[7]) + "," + str(raw[8]) + "," + str(raw[9]))
        raw = cur.fetchone()
    end = input("Finis ?")


def editSpectacle(cur):
    printSpectacle(cur)
    nomSpectacle = input("Quel est le nom du spectacle à modifier ? ")
    dureeSpectacle = input("Quel est la durée du Spectacle ? Format HH:MM:SS ")
    association.printAsso(cur)
    nomAsso = input("Quel est le nom de l'association gérant ce spectacle ? ")
    print("Quel type de spectacle ? \n 1 - Concert \n 2 - Théâtre \n 3 - Stand-Up")
    typeSpectacle = -1
    while typeSpectacle < 1 or typeSpectacle > 3:
        typeSpectacle = int(input("Choix : "))
    if typeSpectacle == 1:
        typeSpectacle = "concert"
        compositeur = input("Qui est le compositeur ? ")
        anneeParution = input("Quelle est l'année de parution ? FORMAT: YYYY-MM-DD ")
        genreConcert = input("Quel est le genre de musique jouée ? ")
        sql = "UPDATE Spectacle SET duree = '%s', typespectacle='%s', compositeur='%s', anneeparution = '%s', genreconcert = %s, association = '%s' WHERE nom = %s" \
              % (dureeSpectacle, typeSpectacle, compositeur, anneeParution, genreConcert, nomAsso, nomSpectacle)
        print(sql)
        cur.execute(sql)
    if typeSpectacle == 2:
        typeSpectacle = "piece de theatre"
        auteur = input("Qui est l'auteur de cette pièce ? ")
        dateParution = input("Quand est paru cette pièce ? FORMAT YYYY-MM-DD ")
        typePiece = input("Quel est le genre de cette pièce ? ")
        sql = "UPDATE SPECTACLE SET duree = '%s', typespectacle = '%s', anneeparution = '%s', auteur = '%s', typetheatre = '%s', association = '%s' WHERE nom = '%s'" \
              % (dureeSpectacle, typeSpectacle, dateParution, auteur, typePiece, nomAsso, nomSpectacle)
        print(sql)
        cur.execute(sql)
    if typeSpectacle == 3:
        typeSpectacle = "stand-up"
        genreStandUp = 0
        print("Quel est le genre de ce stand-up ?\n 1 - spectacle comique \n 2 - debat \n 3 - table ronde \n 4 - Aucun des 3")
        while genreStandUp < 1 or genreStandUp > 4:
            genreStandUp = int(input("Choix : "))
        if genreStandUp == 1:
            genreStandUp = "spectacle comique"
        if genreStandUp == 2:
            genreStandUp = "debat"
        if genreStandUp == 3:
            genreStandUp = "table ronde"
        if genreStandUp == 4:
            genreStandUp = "NULL"
        sql = "UPDATE Spectacle SET duree = '%s', typespectacle ='%s', genrestandup = '%s', association = '%s' WHERE nom = '%s'"\
              % (dureeSpectacle, typeSpectacle, genreStandUp, nomAsso, nomSpectacle)
        print(sql)
        cur.execute(sql)


def insertRole(cur):
    role = input("Entrer le nom du role : ")
    person.printUniversitaire(cur)
    idPerson = input("Entrer le CIN de la personne concernée : ")
    printSpectacle(cur)
    spectacleName = input("Entrer le nom du spectacle : ")
    sql = "INSERT INTO role(role, cin, nomspectacle) VALUES ('%s', %s, '%s')" \
          % (role, idPerson, spectacleName)
    cur.execute(sql)


def deleteRole(cur):
    printRole(cur)
    role = input("Entrer le nom du role concerné : ")
    person.printUniversitaire(cur)
    personId = input("Entrer le CIN de la personne concernée : ")
    spectacleName = input("Entrer le nom du spectacle concerné : ")
    sql = "DELETE FROM role WHERE role = '%s' AND CIN = %s AND nomspectacle = '%s'" % (role, personId, spectacleName)
    cur.execute(sql)


def printRole(cur):
    sql = "SELECT role.role, personne.nom, personne.prenom, role.nomspectacle  FROM Role,personne, universitaire " \
          "WHERE role.cin = universitaire.cin AND universitaire.personne = personne.id"
    cur.execute(sql)
    print("Role | Personne de l'université | Nom du Spectacle")
    raw = cur.fetchone()
    while raw:
        print(str(raw[0]) + " | " + str(raw[2]) + " " + str(raw[1]) + " | " + str(raw[3]))
        raw = cur.fetchone()
    end = input("Finis ?")
