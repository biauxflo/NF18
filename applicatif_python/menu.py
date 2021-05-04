#!/usr/bin/env python3
import connection_db
import init_projet
import command


if __name__ == '__main__':
    choix = 0
    while choix != 2:
        print("MENU : Est-ce votre première execution du logiciel ? :\n1 - OUI"+"\n2 - NON")
        choix = int(input("Choix ? "))
        if choix == 1:
            init_projet.createdb()
        if choix != 1:
            choix = 2
    conn = connection_db.getConnection()
    print(conn)

    cur = conn.cursor()
    choix = 0
    while choix != 5:
        command.screen_clear()
        print("MENU : choix de l'action à réaliser :\n1 - Ajouter une personne,\n2 - Supprimer une personne "
              "inscrite\n3 - Afficher les personnes inscrites population \n4 - Ajouter une association\n5 - Quitter")
        choix = int(input("Choix ? "))
        if choix == 1:
            conn.commit()
            conn.close()
            print("Fin du Programme")
        if choix == 2:
            conn.commit()
            conn.close()
            print("Fin du Programme")
        if choix == 3:
            conn.commit()
            conn.close()
            print("Fin du Programme")
        if choix == 4:
            conn.commit()
            conn.close()
            print("Fin du Programme")
        if choix == 5:
            conn.commit()
            conn.close()
            print("Fin du Programme")
