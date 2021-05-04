def insert_asso(cur, sql_salle=None):
    nom = input("Entrer le nom de l'association.")
    description = input("Entrer la description de l'association.")
    mail = input("Entrer l'adresse mail de l'association.")
    DateCrea = input("Entrer la date de céation de l'association.")
    siteWeb = input("Entrer l'adresse du site Web de l'association")
    categorie = input("Entrez la catégorie de l'asso")
    print("Voici les salles disponibles\n\n")
    sql_salle = "SELECT * FROM salle GROUP BY numero,batiment ORDER BY batiment,numero;"
    cur.execute(sql_salle)
    print("[N° de salle] batiment (type de salle) {Nombre de personne max}")
    raw = cur.fetchone()
    while raw:
        print("[" + str(raw[0]) + "] " + raw[1] + " " + "(" + str(raw[2]) + ")" + "{" + str(raw[3]) + "}")
        raw = cur.fetchone()

    numsalle = input("Entrez le numero de la salle que vous souhaitez occuper")
    batsalle = input("Entrez le batiment de la salle que vous souhaitez occuper")
    print("Vous avez entrez un mauvais numéro de Salle.")
    sql = "INSERT INTO association(nom,description,mail,dateCrea,siteWeb,categorie,numeroSalle,batimentSalle) VALUES('%s','%s','%s',%s,'%s','%s',%s,%s)" % (
        nom, description, mail, DateCrea, siteWeb, categorie, numsalle, batsalle)
    print(sql)
    cur.execute(sql)


def delete_asso(cur):
    nom = input("Entrer le nom de l'association à supprimer.")
    sql = "DELETE FROM association WHERE nom = %s " % (nom)
    print(sql)
    cur.execute(sql)


def print_asso(cur):
    sql = "SELECT * FROM association GROUP BY nom,categorie ORDER BY categorie,nom;"
    cur.execute(sql)
    print("nom | catégorie | descriptiion | mail | date de création | site Web | numero de la salle | batiment")
    raw = cur.fetchone()
    while raw:
        print(raw[0] + "|" + raw[1] + "|" + raw[3] + "|" + str(raw[4]) + "|" + raw[5] + "|" + str(raw[6]) + "|" + raw[7])
        raw = cur.fetchone()


def edit_asso(cur):
    print_asso(cur)
    nom = input("Nom de l'asso à modifier")
    new_nom = input("Entrer le nom de l'association.")
    new_description = input("Entrer la description de l'association.")
    new_mail = input("Entrer l'adresse mail de l'association.")
    new_date = input("Entrer la date de céation de l'association.")
    new_site = input("Entrer l'adresse du site Web de l'association")
    new_cat = input("Entrez la catégorie de l'asso")
    print("Voici les salles disponibles\n\n")
    sql_salle = "SELECT * FROM salle GROUP BY numero,batiment ORDER BY batiment,numero;"
    cur.execute(sql_salle)
    print("[N° de salle] batiment (type de salle) {Nombre de personne max}")
    raw = cur.fetchone()
    while raw:
        print("[" + str(raw[0]) + "] " + raw[1] + " " + "(" + str(raw[2]) + ")" + "{" + str(raw[3]) + "}")
        raw = cur.fetchone()
    new_numsalle = input("Entrez le numero de la salle que vous souhaitez occuper")
    new_batsalle = input("Entrez le batiment de la salle que vous souhaitez occuper")

    sql = "UPDATE association SET nom= '%s', description = '%s', mail = '%s', datecrea = %s, siteWeb = '%s', categorie = '%s', numerosalle = %s, batimentsalle = '%s' WHERE nom = '%s'" % \
          (new_nom, new_description, new_mail, new_date, new_site, new_cat, new_numsalle, new_batsalle, nom)
    print(sql)
    cur.execute(sql)

def insert_membre(cur):
    print("Quel est rôle ?\n 1 - Président,\n 2 - Tresorier,\n 3 - Membre")
    role = 0
    while role < 1 | type_bat > 3:
        type_bat = input("Choix ?")
    if type_bat == 1:
        type_bat = "president"
    if type_bat == 2:
        type_bat = "tresorier"
    if type_bat == 3:
        type_bat = "membre"
    print_asso(cur)
    nomAsso = input("Entrer le nom de l'association")
    print("Voici la liste des étudiants : \n")
    sqlaffetu = "SELECT personne.id, personne.nom, personne.prenom, universitaire.cin, universitaire.categorie " \
          "FROM Personne, universitaire WHERE personne.id = universitaire.personne and universitaire.categorie = 'etudiant';"
    cur.execute(sqlaffetu)
    print("[id] nom prénom CIN categorie")
    raw = cur.fetchone()
    while raw:
        print("[" + str(raw[0]) + "] " + raw[1] + " " + str(raw[2]) + " " + str(raw[3]) + " " + str(raw[4]))
        raw = cur.fetchone()
    CIN = input("Entrer le numero CIN de l'étudiant")
    sql = "INSERT INTO membre(role,nomassociation,cin) VALUES ('%s','%s',%s) " % (role,nomAsso,CIN)
    print(sql)
    cur.execute(sql)

def delete_membre(cur):
    print_membre(cur)
    num_cin = input("Entrez le numero cin de l'etudiant à supprimer")
    role = input("Entre le role de l'étudiant à supprimer")
    sql = "DELETE FROM membre WHERE nomassociation = '%s' and cin = %s and role = %s" %(nomAssociation,num_cin,role)




def print_membre(cur):
    nomAsso = input("Entrer le nom de l'association dont vous souhaitez afficher les membres")
    print("Voici les membres de cette association")
    sqlaff = "SELECT p.nom, p.prenom, u.cin, m.role FROM membre as m  JOIN universitaire as u ON m.cin = u.cin JOIN Personne as p ON u.personne = p.id WHERE m.nomassociation = '%s'" %(nomAsso)
    print("nom prénom CIN role")
    raw = cur.fetchone()
    while raw:
        print(raw[0] + " " + str(raw[1]) + " " + str(raw[2]) + " " + str(raw[3]))
        raw = cur.fetchone()