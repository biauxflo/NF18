#!/usr/bin/env python3
import connection_db
import command
import person
import association
import room
import seance
import spectacle
import ticket
import os


def screenClear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        os.system('export TERM=xterm')
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')


if __name__ == '__main__':
    conn = connection_db.getConnection()
    cur = conn.cursor()
    choix = 0
    while choix != 36:
        screenClear()
        print("MENU : choix de l'action à réaliser :\n1 - Ajouter une personne,\n2 - Supprimer une personne "
              "inscrite\n3 - Afficher les personnes inscrites\n4 - Modifier les infos d'une personne \n5 - Ajouter une association\n"
              "6 - Supprimer une association\n7 - Afficher les associations\n8 - Modifier les infos d'une associations \n9 - Ajouter une Salle\n"
              "10 - Supprimer une Salle\n11 - Modifier les informations d'une salle\n12 - Afficher les salles  \n13 - Ajouter un spectacle\n"
              "14 - Supprimer un spectacle\n15 - Modifier un spectacle\n16 - Afficher les spectacles \n17 - Ajouter une séance\n"
              "18 - Supprimer une séance\n19 - Modifier une séance\n20 - Afficher les séances \n21 - Ajouter un billet\n"
              "22 - Supprimer un Billet\n23 - Modifier un billet\n24 - Afficher les billets \n25 - Insérer un membre \n"
              "26 - Supprimer un membre \n27 - Afficher les membres \n28 - Ajouter une catégorie de billet \n29 - Supprimer une catégorie "
              "de billet \n30 - Modifier un catégorie de billet \n31 - Afficher les catégories de billet \n32 - Ajouter un role dans un spectacle \n"
              "33 - Supprimer un role dans un spectacle \n34 - Afficher les roles dans des spectacles \n35 - Modifier le rôle de quelqu'un \n"
              "36 - Quitter")
        choix = int(input("Choix ? "))
        if choix == 1:
            person.insertPerson(cur)
            conn.commit()
        if choix == 2:
            person.deletePerson(cur)
            conn.commit()
        if choix == 3:
            person.editPerson(cur)
            conn.commit()
        if choix == 4:
            person.printPerson(cur)
            conn.commit()
        if choix == 5:
            association.insertAsso(cur)
            conn.commit()
        if choix == 6:
            association.deleteAsso(cur)
            conn.commit()
        if choix == 7:
            association.editAsso(cur)
            conn.commit()
        if choix == 8:
            association.printAsso(cur)
            conn.commit()
        if choix == 9:
            room.insertRoom(cur)
            conn.commit()
        if choix == 10:
            room.deleteRoom(cur)
            conn.commit()
        if choix == 11:
            room.editRoom(cur)
            conn.commit()
        if choix == 12:
            room.printRoom(cur)
            conn.commit()
        if choix == 13:
            spectacle.insertSpectacle(cur)
            conn.commit()
        if choix == 14:
            spectacle.deleteSpectacle(cur)
            conn.commit()
        if choix == 15:
            spectacle.editSpectacle(cur)
            conn.commit()
        if choix == 16:
            spectacle.printSpectacle(cur)
            conn.commit()
        if choix == 17:
            seance.insertSeance(cur)
            conn.commit()
        if choix == 18:
            seance.deleteSeance(cur)
            conn.commit()
        if choix == 19:
            seance.editSeance(cur)
            conn.commit()
        if choix == 20:
            seance.printSeance(cur)
            conn.commit()
        if choix == 21:
            ticket.insertBillet(cur)
            conn.commit()
        if choix == 22:
            ticket.deleteBillet(cur)
            conn.commit()
        if choix == 23:
            ticket.editBillet(cur)
            conn.commit()
        if choix == 24:
            ticket.printBillet(cur)
            conn.commit()
        if choix == 25:
            association.insertMembre(cur)
            conn.commit()
        if choix == 26:
            association.deleteMembre(cur)
            conn.commit()
        if choix == 27:
            association.printMembre(cur)
            conn.commit()
        if choix == 28:
            ticket.insertCatBillet(cur)
            conn.commit()
        if choix == 29:
            ticket.deleteCatBillet(cur)
            conn.commit()
        if choix == 30:
            ticket.editCatBillet(cur)
            conn.commit()
        if choix == 31:
            ticket.printCatBillet(cur)
            conn.commit()
        if choix == 32:
            spectacle.insertRole(cur)
            conn.commit()
        if choix == 33:
            spectacle.deleteRole(cur)
            conn.commit()
        if choix == 34:
            spectacle.printRole(cur)
            conn.commit()
        if choix == 35:
            spectacle.editRole(cur)
            conn.commit()
        if choix == 36:

            conn.close()
            print("Fin du Programme")
