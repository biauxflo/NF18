def insertAsso(cur, sql_salle=None):
    nom = input("Entrer le nom de l'association : ")
    description = input("Entrer la description de l'association : ")
    mail = input("Entrer l'adresse mail de l'association : ")
    DateCrea = input("Entrer la date de céation de l'association : ")
    siteWeb = input("Entrer l'adresse du site Web de l'association : ")
    categorie = input("Entrez la catégorie de l'association : ")
    print("Voici les salles disponibles : \n\n")
    sql_salle = "SELECT * FROM salle GROUP BY numero,batiment ORDER BY batiment,numero;"
    cur.execute(sql_salle)
    print("[N° de salle] batiment (type de salle) {Nombre de personne max}")
    raw = cur.fetchone()
    while raw:
        print("[" + str(raw[0]) + "] " + raw[1] + " " + "(" + str(raw[2]) + ")" + "{" + str(raw[3]) + "}")
        raw = cur.fetchone()

    numsalle = input("Entrez le numero de la salle que vous souhaitez occuper : ")
    batsalle = input("Entrez le batiment de la salle que vous souhaitez occuper : ")
    print("Vous avez entrez un mauvais numéro de Salle : ")
    sql = "INSERT INTO association(nom,description,mail,dateCrea,siteWeb,categorie,numeroSalle,batimentSalle) VALUES('%s','%s','%s','%s','%s','%s',%s,'%s')" % (
        nom, description, mail, DateCrea, siteWeb, categorie, numsalle, batsalle)
    print(sql)
    cur.execute(sql)


def deleteAsso(cur):
    printAsso(cur)
    nom = input("Entrer le nom de l'association à supprimer : ")
    sql = "DELETE FROM association WHERE nom = '%s' " % (nom)
    print(sql)
    cur.execute(sql)


def printAsso(cur):
    sql = "SELECT * FROM association GROUP BY nom,categorie ORDER BY categorie,nom;"
    cur.execute(sql)
    print("nom | catégorie | descriptiion | mail | date de création | site Web | salle de réunion | batiment")
    raw = cur.fetchone()
    while raw:
        print(
            str(raw[0]) + "|" + str(raw[1]) + "|" + str(raw[3]) + "|" + str(raw[4]) + "|" + str(raw[5]) + "|" + str(raw[6]) + "|" + str(raw[7]))
        raw = cur.fetchone()
    end = input("Continuer ?")

def editAsso(cur):
    printAsso(cur)
    nom = input("Nom de l'association à modifier : ")
    new_nom = input("Entrer le nom de l'association : ")
    new_description = input("Entrer la description de l'association : ")
    new_mail = input("Entrer l'adresse mail de l'association : ")
    new_date = input("Entrer la date de céation de l'association : ")
    new_site = input("Entrer l'adresse du site Web de l'association : ")
    new_cat = input("Entrez la catégorie de l'association : ")
    print("Voici les salles disponibles : \n\n")
    sql_salle = "SELECT * FROM salle GROUP BY numero,batiment ORDER BY batiment,numero;"
    cur.execute(sql_salle)
    print("[N° de salle] batiment (type de salle) {Nombre de personne max}")
    raw = cur.fetchone()
    while raw:
        print("[" + str(raw[0]) + "] " + raw[1] + " " + "(" + str(raw[2]) + ")" + "{" + str(raw[3]) + "}")
        raw = cur.fetchone()
    new_numsalle = input("Entrez le numero de la salle que vous souhaitez occuper : ")
    new_batsalle = input("Entrez le batiment de la salle que vous souhaitez occuper : ")

    sql = "UPDATE association SET nom= '%s', description = '%s', mail = '%s', datecrea = '%s', siteWeb = '%s', categorie = '%s', numerosalle = %s, batimentsalle = '%s' WHERE nom = '%s'" % \
          (new_nom, new_description, new_mail, new_date, new_site, new_cat, new_numsalle, new_batsalle, nom)
    print(sql)
    cur.execute(sql)


def insertMembre(cur):
    print("Quel est rôle ?\n1 - Président,\n2 - Tresorier,\n3 - Membre")
    role = 0
    while role < 1 or role > 3:
        role = int(input("Choix ? "))
    if role == 1:
        role = "president"
    if role == 2:
        role = "tresorier"
    if role == 3:
        role = "membre"
    printAsso(cur)
    nomAsso = input("Entrer le nom de l'association : ")
    if role != "membre":
        sql = "SELECT * FROM membre WHERE nomassociation = '%s' AND role = '%s'" % (nomAsso, role)
        cur.execute(sql)
        row = cur.fetchone
        if row:
            print("Le rôle est déjà occupé, veuillez supprimer l'ancienne personne occupant ce rôle de la table ou attendez. ")
            return 1
    print("Voici la liste des étudiants : \n")
    sqlaffetu = "SELECT personne.id, personne.nom, personne.prenom, universitaire.cin, universitaire.categorie " \
                "FROM Personne, universitaire WHERE personne.id = universitaire.personne and universitaire.categorie = 'etudiant';"
    cur.execute(sqlaffetu)
    print("[id] nom prénom CIN categorie")
    raw = cur.fetchone()
    while raw:
        print("[" + str(raw[0]) + "] " + raw[1] + " " + str(raw[2]) + " " + str(raw[3]) + " " + str(raw[4]))
        raw = cur.fetchone()
    CIN = input("Entrer le numero CIN de l'étudiant : ")
    sql = "INSERT INTO membre(role,nomassociation,cin) VALUES ('%s','%s',%s) " % (role, nomAsso, CIN)
    print(sql)
    cur.execute(sql)


def deleteMembre(cur):
    print("Voici les association : ")
    printAsso(cur)
    printMembre(cur)
    nomAssociation = input("Quel est le nom de l'association concernée ? ")
    num_cin = input("Entrez le numero cin de l'etudiant à supprimer : ")
    role = input("Entre le role de l'étudiant à supprimer : ")
    sql = "DELETE FROM membre WHERE nomassociation = '%s' and cin = %s and role = '%s'" % (nomAssociation, num_cin, role)
    print(sql)
    cur.execute(sql)


def printMembre(cur):
    nomAsso = input("Entrer le nom de l'association dont vous souhaitez afficher les membres : ")
    print("Voici les membres de cette association : ")
    sqlaff = "SELECT p.nom, p.prenom, u.cin, m.role FROM membre as m  JOIN universitaire as u ON m.cin = u.cin JOIN Personne as p ON u.personne = p.id WHERE m.nomassociation = '%s'" % nomAsso
    print(sqlaff)
    cur.execute(sqlaff)
    print("nom prénom CIN role")
    raw = cur.fetchone()
    while raw:
        print(raw[0] + " " + str(raw[1]) + " " + str(raw[2]) + " " + str(raw[3]))
        raw = cur.fetchone()
    end = input("Finis ?")
