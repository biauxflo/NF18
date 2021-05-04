def insertRoom(cur):
    num = input("Entrer le numero de salle.")
    batiment = input("Entrer le nom du batiment.")
    print("Quel est le type de la salle ?\n 1 - Amphithéâtre,\n2 - Salle de Cours,\n 3 - Bureau ")
    type_bat = 0
    while type_bat < 1 | type_bat > 3:
        type_bat = input("Choix ?")
    if type_bat == 1:
        type_bat = "amphitheatre"
    if type_bat == 2:
        type_bat = "salle de cours"
    if type_bat == 3:
        type_bat = "bureau"
    nbPersonne = input("Combien de personne au maximum dans la salle ?")
    sql = "INSERT INTO Salle(numero,batiment,type,nbPersonne) VALUES(%s,'%s','%s',%s)" % (
        num, batiment, type_bat, nbPersonne)
    print(sql)
    cur.execute(sql)


def deleteRoom(cur):
    num = input("Entrer le numero de la salle à supprimer.")
    batiment = input("Entrer le nom du batiment de cette salle.")
    sql = "DELETE FROM Salle WHERE numero = %s AND batiment = '%s'" % (num, batiment)
    print(sql)
    cur.execute(sql)


def printRoom(cur):
    sql = "SELECT * FROM salle GROUP BY numero,batiment ORDER BY batiment,numero;"
    cur.execute(sql)
    print("[N° de salle] batiment (type de salle) {Nombre de personne max}")
    raw = cur.fetchone()
    while raw:
        print("[" + str(raw[0]) + "] " + raw[1] + " " + "(" + str(raw[2]) + ")" + "{" + str(raw[3]) + "}")
        raw = cur.fetchone()


def editRoom(cur):
    printRoom(cur)
    num = input("Numéro de la salle à modifier")
    batiment = input("Nom du batiment à modifier")
    new_num = input("Entrer le numero de salle.")
    new_batiment = input("Entrer le nom du batiment.")
    print("Quel est le type de la salle ?\n 1 - Amphithéâtre,\n2 - Salle de Cours,\n 3 - Bureau ")
    new_type_bat = 0
    while new_type_bat < 1 | new_type_bat > 3:
        type_bat = input("Choix ?")
    new_nbPersonne = input("Combien de personne au maximum dans la salle ?")
    sql = "UPDATE Salle SET numero= %s, batiment = '%s', type = '%s', nbpersonne = %s WHERE numero = %s and batiment = %s" % \
          (new_num, new_batiment, new_type_bat, new_nbPersonne, num, batiment)
    print(sql)
    cur.execute(sql)

