#!/usr/bin/env python3
import connection_db
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
    cat = 0
    while cat != 8:
        screenClear()
        cat = int(input("MENU : choix de la catégorie:\n1 - Personne\n2 - Assiciation\n3 - Salle"
              "\n4 - Spectacle\n5 - Séance \n6 - Billet\n7 - Membre\n8 - Quitter\nChoix: "))

        flag = 1
        if cat == 1: #Personne
            while flag == 1:
                screenClear()
                print("Choix de l'action à réaliser:")
                flag = 0
                print("\n1 - Ajouter une personne,\n2 - Supprimer une personne "
                      "inscrite\n3 - Afficher les personnes inscrites\n4 - Modifier les infos d'une personne\n"
                      "5 - Retourner\n")
                choix = int(input("Choix ? "))
                if choix == 1:
                    person.insertPerson(cur)
                    conn.commit()
                elif choix == 2:
                    person.deletePerson(cur)
                    conn.commit()
                elif choix == 3:
                    person.editPerson(cur)
                    conn.commit()
                elif choix == 4:
                    person.printPerson(cur)
                    conn.commit()
                elif choix == 5:
                    flag == 1
                else:
                    print("Choix invalid, réessayez s'il vous plait.\n")
                    flag = 1
        elif cat == 2:#Association
            while flag == 1:
                screenClear()
                print("Choix de l'action à réaliser:")
                flag = 0
                print("\n1 - Ajouter une association\n2 - Supprimer une association\n3 - Afficher les associations"
                      "\n4 - Modifier les infos d'une associations \n5 - Retourner\n")
                choix = int(input("Choix ? "))
                if choix == 1:
                    association.insertAsso(cur)
                    conn.commit()
                elif choix == 2:
                    association.deleteAsso(cur)
                    conn.commit()
                elif choix == 3:
                    association.editAsso(cur)
                    conn.commit()
                elif choix == 4:
                    association.printAsso(cur)
                    conn.commit()
                elif choix == 5:
                    flag == 1
                else:
                    print("Choix invalid, réessayez s'il vous plait.\n")
                    flag = 1
        elif cat == 3:  # Salle
            while flag == 1:
                screenClear()
                print("Choix de l'action à réaliser:")
                flag = 0
                print("\n1 - Ajouter une Salle\n2 - Supprimer une Salle\n3 - Modifier les informations d'une salle"
                      "\n4 - Afficher les salles  \n5 - Retourner\n")
                choix = int(input("Choix ? "))
                if choix == 1:
                    room.insertRoom(cur)
                    conn.commit()
                elif choix == 2:
                    room.deleteRoom(cur)
                    conn.commit()
                elif choix == 3:
                    room.editRoom(cur)
                    conn.commit()
                elif choix == 4:
                    room.printRoom(cur)
                    conn.commit()
                elif choix == 5:
                    flag == 1
                else:
                    print("Choix invalid, réessayez s'il vous plait.\n")
                    flag = 1
        elif cat == 4:  # Spectacle
            while flag == 1:
                screenClear()
                print("Choix de l'action à réaliser:")
                flag = 0
                print("\n1 - Ajouter un spectacle\n2 - Supprimer un spectacle\n"
                      "3 - Modifier un spectacle\n4 - Afficher les spectacles\n"
                      "5 - Ajouter un role dans un spectacle \n6 - Supprimer un role dans un spectacle \n"
                      "7 - Afficher les roles dans des spectacles \n8 - Retourner\n")
                choix = int(input("Choix ? "))
                if choix == 1:
                    spectacle.insertSpectacle(cur)
                    conn.commit()
                elif choix == 2:
                    spectacle.deleteSpectacle(cur)
                    conn.commit()
                elif choix == 3:
                    spectacle.editSpectacle(cur)
                    conn.commit()
                elif choix == 4:
                    spectacle.printSpectacle(cur)
                    conn.commit()
                elif choix == 5:
                    spectacle.insertRole(cur)
                    conn.commit()
                elif choix == 6:
                    spectacle.deleteRole(cur)
                    conn.commit()
                elif choix == 7:
                    spectacle.printRole(cur)
                    conn.commit()
                elif choix == 8:
                    flag == 1
                else:
                    print("Choix invalid, réessayez s'il vous plait.\n")
                    flag = 1
        elif cat == 5:  # Séance
            while flag == 1:
                screenClear()
                print("Choix de l'action à réaliser:")
                flag = 0
                print("\n1 - Ajouter une séance\n2 - Supprimer une séance\n"
                      "3 - Modifier une séance\n4 - Afficher les séances \n5 - Retourner\n")
                choix = int(input("Choix ? "))
                if choix == 1:
                    seance.insertSeance(cur)
                    conn.commit()
                if choix == 2:
                    seance.deleteSeance(cur)
                    conn.commit()
                if choix == 3:
                    seance.editSeance(cur)
                    conn.commit()
                if choix == 4:
                    seance.printSeance(cur)
                    conn.commit()
                elif choix == 5:
                    flag == 1
                else:
                    print("Choix invalid, réessayez s'il vous plait.\n")
                    flag = 1
        elif cat == 6:  # Billet
            while flag == 1:
                screenClear()
                print("Choix de l'action à réaliser:")
                flag = 0
                print("\n1 - Ajouter un billet\n2 - Supprimer un Billet\n3 - Modifier un billet\n"
                      "4 - Afficher les billets \n5 - Ajouter une catégorie de billet \n"
                      "6 - Supprimer une catégorie de billet \n7 - Modifier un catégorie de billet\n"
                      "8 - Afficher les catégories de billet\n9 - Retourner\n")
                choix = int(input("Choix ? "))
                if choix == 1:
                    ticket.insertBillet(cur)
                    conn.commit()
                elif choix == 2:
                    ticket.deleteBillet(cur)
                    conn.commit()
                elif choix == 3:
                    ticket.editBillet(cur)
                    conn.commit()
                elif choix == 4:
                    ticket.printBillet(cur)
                    conn.commit()
                elif choix == 5:
                    ticket.insertCatBillet(cur)
                    conn.commit()
                elif choix == 6:
                    ticket.deleteCatBillet(cur)
                    conn.commit()
                elif choix == 7:
                    ticket.editCatBillet(cur)
                    conn.commit()
                elif choix == 8:
                    ticket.printCatBillet(cur)
                    conn.commit()
                elif choix == 9:
                    flag == 1
                else:
                    print("Choix invalid, réessayez s'il vous plait.\n")
                    flag = 1
        elif cat == 7:  # Membre
            while flag == 1:
                screenClear()
                print("Choix de l'action à réaliser:")
                flag = 0
                print("\n1 - Insérer un membre \n2 - Supprimer un membre \n"
                      "3 - Afficher les membres \n4 - Retourner\n")
                choix = int(input("Choix ? "))
                if choix == 1:
                    association.insertMembre(cur)
                    conn.commit()
                if choix == 2:
                    association.deleteMembre(cur)
                    conn.commit()
                if choix == 3:
                    association.printMembre(cur)
                    conn.commit()
                elif choix == 4:
                    flag == 1
                else:
                    print("Choix invalid, réessayez s'il vous plait.\n")
                    flag = 1
        elif cat == 8:  # Membre
            conn.close()
            print("Fin du Programme")
        else:
            print("Choix invalid, réessayez s'il vous plait.\n")

