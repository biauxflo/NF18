#!/usr/bin/env python3
import psycopg2


def getConnection():
    return psycopg2.connect("host=localhost dbname=projetGroupe1 user=utilisateur_projet password=groupe1sujet4")



