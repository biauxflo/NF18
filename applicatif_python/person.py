def insertPerson(cur):
    nom = input("Entrer le nom.")
    pre = input("Entrer le prénom")
    typePerson = -1
    print("Personnel/Etudiant de l'UTX ou personne extérieure ?\n 1 - Université\n 2 - Extérieure")
    while typePerson != 1 & typePerson != 2:
        typePerson = int(input("Choix de type"))

    if typePerson == 1:
        CIN = input("Entrer le CIN de la personne")
        print("Quel est le type de la personne ?\n 1 - Etudiant,\n2 - Personnel technique,\n 3 - Personnel enseignant \n 4 - Personnel administratif")
        typeUni = 0
        while typeUni < 1 | typeUni > 4:
            typeUni = int(input("Choix ?"))
        if typeUni == 1:
            typeUni = "etudiant"
        if typeUni == 2:
            typeUni = "technique"
        if typeUni == 3:
            typeUni = "enseignant"
        if typeUni == 4:
            typeUni = "administratif"
        sql = "INSERT INTO personne(nom,prenom) VALUES(%s,'%s')" % (nom, pre)
        print(sql)
        cur.execute(sql)
        idPerson = getIdPerson(cur, nom, pre)
        sql = "INSERT INTO universitaire(personne, cin, categorie) VALUES(%s, %s,'%s')" % (idPerson, CIN, typeUni)
        print(sql)
        cur.execute(sql)
    if typePerson == 2:
        tel = ""
        while len(tel) != 10:
            tel = input("N° de tel")
        orgAffiliation = input("Quel est votre organisme d'affiliation ?")
        sql = "INSERT INTO personne(nom,prenom) VALUES(%s,'%s')" % (nom, pre)
        print(sql)
        cur.execute(sql)
        idPerson = getIdPerson(cur, nom, pre)
        sql = "INSERT INTO personneexterieure(personne, numerotelephone, organismeaffiliation) VALUES(%s, %s,'%s')" % (idPerson, tel, orgAffiliation)
        print(sql)
        cur.execute(sql)


def deletePerson(cur):
    printPerson(cur)
    typePers = 0
    print("Dans l'université ou à l'extérieur ?\n 1 - Université, 2 - Extérieur")
    while typePers != 1 & typePers != 2:
        typePers = input("Choix : ")
    idToDelete = input("Quel est l'ID de la personne à supprimer ?")
    if typePers == 1:
        sql = "DELETE FROM universitaire WHERE personne = %s" % idToDelete
        print(sql)
        cur.execute(sql)
    else:
        sql = "DELETE FROM personneexterieure WHERE personne = %s" % idToDelete
        print(sql)
        cur.execute(sql)
    sql = "DELETE FROM personne WHERE id = %s" % idToDelete
    print(sql)
    cur.execute(sql)


def printPerson(cur):
    sql = "SELECT personne.id, personne.nom, personne.prenom, universitaire.cin, universitaire.categorie " \
          "FROM Personne, universitaire WHERE personne.id = universitaire.personne;"
    cur.execute(sql)
    print("Personne travaillant à l'UTX")
    print("[id] nom prénom CIN categorie")
    raw = cur.fetchone()
    while raw:
        print("[" + str(raw[0]) + "] " + raw[1] + " " + str(raw[2]) + " " + str(raw[3]) + " " + str(raw[4]))
        raw = cur.fetchone()


    sql = "SELECT personne.id, personne.nom, personne.prenom, personneexterieure.numerotelephone, personneexterieure.organismeaffiliation" \
          " FROM Personne, personneexterieure WHERE personne.id = personneexterieure.personne;"
    cur.execute(sql)
    print("Personne extérieure à l'UTX")
    print("[id] nom prénom Telephone Organisme d'affiliation")
    raw = cur.fetchone()
    while raw:
        print("[" + str(raw[0]) + "] " + raw[1] + " " + str(raw[2]) + " " + str(raw[3]) + " " + str(raw[4]))
        raw = cur.fetchone()


def editPerson(cur):
    printPerson(cur)
    typePers = 0
    print("Dans l'université ou à l'extérieur ?\n 1 - Université, 2 - Extérieur")
    while typePers != 1 & typePers != 2:
        typePers = int(input("Choix : "))
    idToEdit = input("Quel est l'ID de la personne à modifier ?")
    newName = input("Quel est le nouveau nom ?")
    newFirstName = input("Quel est le nouveau Prénom ?")
    if typePers == 1:
        newCIN = input("Entrez le CIN de la personne à supprimer :")
        print("Quel est le type de la personne ?\n 1 - Etudiant,\n2 - Personnel technique,\n 3 - Personnel enseignant \n "
              "4 - Personnel administratif")
        newTypeUni = 0
        while newTypeUni < 1 | newTypeUni > 4:
            newTypeUni = int(input("Choix ?"))
        if newTypeUni == 1:
            newTypeUni = "etudiant"
        if newTypeUni == 2:
            newTypeUni = "technique"
        if newTypeUni == 3:
            newTypeUni = "enseignant"
        if newTypeUni == 4:
            newTypeUni = "administratif"
        sql = "UPDATE universitaire SET cin = '%s', categorie= '%s' WHERE personne = %s" % (newCIN, newTypeUni, idToEdit)
        print(sql)
        cur.execute(sql)
    else:
        newTel = ""
        while len(newTel) != 10:
            newTel = input("N° de tel")
        newOrgAffiliation = input("Quel est votre organisme d'affiliation ?")
        sql = "UPDATE personneexterieure SET numerotelephone = '%s', organismeaffiliation = '%s' WHERE personne = '%s'" \
              % (newTel, newOrgAffiliation, idToEdit)
        print(sql)
        cur.execute(sql)
    sql = "UPDATE personne SET nom='%s', prenom='%s' WHERE id = %s" % (newName, newFirstName, idToEdit)
    print(sql)
    cur.execute(sql)


def getIdPerson(cur, nom, prenom):
    sql = "SELECT * FROM Personne WHERE nom = '%s' AND prenom = '%s'" % (nom, prenom)
    cur.execute(sql)
    raw = cur.fetchone()
    idPersonne = ""
    while raw:
        idPersonne = str(raw[0])
    return idPersonne
