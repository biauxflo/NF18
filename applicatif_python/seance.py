import room
import spectacle


def insertSeance(cur):
    date = input("Quelle est la date de la seance ? FORMAT : YYYY-MM-DD ")
    room.printRoom(cur)
    numeroSalle = input("Quelle numero de salle ? ")
    batimentSalle = input("Dans quel batiment ? ")
    spectacle.printSpectacle(cur)
    nomSpectacle = input("Quel est le nom du spectacle concerné ? ")
    sql = "INSERT INTO seance(date, nomSpectacle, numerosalle, batimentsalle) VALUES('%s', '%s', %s, '%s')" \
          % (date, nomSpectacle, numeroSalle, batimentSalle)
    print(sql)
    cur.execute(sql)


def deleteSeance(cur):
    printSeance(cur)
    idToDelete = input("Quelle est l'Id de la séance à supprimer ? ")
    sql = "DELETE FROM seance WHERE id = %s" % idToDelete
    print(sql)
    cur.execute(sql)


def printSeance(cur):
    sql = "SELECT * FROM seance"
    print(sql)
    cur.execute(sql)
    print("[Id] | date | Spectacle | numéro de Salle | Bâtiment")
    raw = cur.fetchone()
    while raw:
        print("[" + str(raw[0]) + "] " + str(raw[1]) + " " + str(raw[2]) + " " + str(raw[3]) + " " + str(raw[4]))
        raw = cur.fetchone()
    end = input("Finis ?")


def editSeance(cur):
    printSeance(cur)
    idSeance = input("Quel est l'Id de la seance que vous souhaitez modifiez ? ")
    date = input("Quelle est la date de la seance FORMAT YYYY-MM-DD ")
    room.printRoom(cur)
    numeroSalle = input("Quelle numero de salle ? ")
    batimentSalle = input("Dans quel batiment ? ")
    spectacle.printSpectacle(cur)
    nomSpectacle = input("Quel est le nom du spectacle concerné ? ")
    sql = "UPDATE seance SET date = '%s', nomspectacle = '%s', numerosalle = %s,batimentsalle = '%s' WHERE id = %s" \
          % (date, nomSpectacle, numeroSalle, batimentSalle, idSeance)
    print(sql)
    cur.execute(sql)

