import os;
def createdb():
    os.system("pg_ctl -s -D /usr/local/var/postgres stop")
    os.system("pg_ctl -s -D /usr/local/var/postgres start")
    os.system("dropdb projetGroupe1")
    os.system("createdb projetGroupe1")
    os.system("psql projetGroupe1 -f ../createdb.sql")
