
INSERT INTO Salle(numero,batiment,type,nbPersonne) VALUES(18,'BF','salle de cours', 30);
INSERT INTO Salle(numero,batiment,type,nbPersonne) VALUES(121,'BF','salle de cours', 40);
INSERT INTO Salle(numero,batiment,type,nbPersonne) VALUES(20,'PG','amphitheatre',300);

INSERT INTO Personne(nom, prenom) VALUES('Jean','Dupont');
INSERT INTO Personne(nom,prenom) VALUES('Victor', 'Martin');

INSERT INTO Association (nom, description, mail, dateCrea, siteWeb, categorie, numeroSalle, batimentSalle) VALUES ('DBS City','Evènement','bigN@dbs.com','1800-11-09','google.com','Vol',18,'BF');
INSERT INTO Association (nom, description, mail, dateCrea, siteWeb, categorie, numeroSalle, batimentSalle) VALUES ('Festufric','Evènement','assopaumee@oula.com','1500-10-09','Ohbeh.com','Hola',20,'PG');
INSERT INTO Association (nom, description, mail, dateCrea, siteWeb, categorie, numeroSalle, batimentSalle) VALUES ('Eturaclette','Restauration','manger@manger.com','2021-04-09','OhMiam.com','Yiha',121,'BF');
INSERT INTO universitaire(personne,CIN,categorie) VALUES(1,987456,'etudiant');
INSERT INTO PersonneExterieure(personne,numeroTelephone,organismeAffiliation) VALUES(2,0777777777,'CompiCity');

INSERT INTO membre(role,nomAssociation,CIN) VALUES('president','DBS City', 987456);

INSERT INTO Spectacle (nom, duree, typeSpectacle, compositeur, anneeParution, genreConcert,association, seances) VALUES
                      ('Vol de spectacle','05:04:00', 'concert','bigN','2021-03-11','Techno', 'DBS City',
                       '[{"date":"2021-10-05",
                         "numSalle": 18,
                         "batimentSalle":"BF",
                         "categorieBillets": [{
                            "nom" : "Plein Pot",
                            "nbPersonne" : "150"
                         },
                         {
                            "nom" : "Peu cher",
                            "nbPersonne" : "1"
                         }]}]');

INSERT INTO Billet(dateCreation, personne, tarif, categorie, seance) VALUES('2021-04-20', 1, 20, 'Plein pot', 1);
/*INSERT INTO Seance(date,nomSpectacle,numeroSalle,batimentSalle) VALUES('2021-10-05','Vol de spectacle',18,'BF');

INSERT INTO CategorieBillet(nom,nbrPlace) VALUES('Plein pot', 150);*/
