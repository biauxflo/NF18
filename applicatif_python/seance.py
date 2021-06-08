import room
import spectacle
import ticket


def insertSeance(cur):
    seanceJson = '['
    date = input("Quelle est la date de la seance ? FORMAT : YYYY-MM-DD ")
    room.printRoom(cur)
    numeroSalle = input("Quelle numero de salle ? ")
    batimentSalle = input("Dans quel batiment ? ")
    heure = input("Saisissez l'heure de la séance : HH:MM ")
    print("CREATION DE CATEGORIE DE BILLET")
    catBilletJson = ticket.insertCatBillet()
    seanceJson += '{"date" :"' + date + '" , "numeroSalle" :"' + numeroSalle + '", "batimentSalle":"' + batimentSalle + '", "categorieBillets": "' + catBilletJson + '"}'
    choix = 0
    while choix != 2:
        choix = int(input("Quel choix voulez-vous faire ?\n 1 - Insérer une nouvelle séance \n 2 - Retourner au menu\n"))
        if choix == 1:
            seanceJson += ','
            date = input("Quelle est la date de la seance ? FORMAT : YYYY-MM-DD ")
            room.printRoom(cur)
            numeroSalle = input("Quelle numero de salle ? ")
            batimentSalle = input("Dans quel batiment ? ")
            catBilletJson = ticket.insertCatBillet()
            seanceJson += '{"date" :"' + date + '" , "numSalle" :"' + numeroSalle + '", "batimentSalle":"' + batimentSalle + '", "categorieBillets": ' + catBilletJson + '}'
    seanceJson += ']'
    return seanceJson


def printSeance(cur):
    sql = "SELECT * FROM v_seances"
    cur.execute(sql)
    print("[Nom du Spectacle] | date | heure | Spectacle | numéro de Salle | Bâtiment")
    raw = cur.fetchone()
    while raw:
        print("[" + str(raw[0]) + "] " + str(raw[1]) + " " + str(raw[2]) + " " + str(raw[3]) + " " + str(raw[4]))
        raw = cur.fetchone()
    end = input("Finis ?")
