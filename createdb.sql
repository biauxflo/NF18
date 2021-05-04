DROP TABLE IF EXISTS salle CASCADE;DROP TABLE IF EXISTS  association CASCADE;DROP TABLE IF EXISTS  membre CASCADE;
DROP TABLE IF EXISTS  personne CASCADE;DROP TABLE IF EXISTS  universitaire CASCADE;DROP TABLE IF EXISTS  personneExterieure CASCADE;
DROP TABLE IF EXISTS  role CASCADE;DROP TABLE IF EXISTS  spectacle CASCADE;DROP TABLE IF EXISTS  billet CASCADE;DROP TABLE IF EXISTS  seance CASCADE;
DROP TABLE IF EXISTS  categorieBillet CASCADE;
DROP TYPE IF EXISTS type_salle;DROP TYPE IF EXISTS cat;DROP TYPE IF EXISTS role_asso;DROP TYPE  IF EXISTS genre_standup;DROP TYPE IF EXISTS typeSpectacle;
DROP user if exists utilisateur_projet;

CREATE USER utilisateur_projet with password 'groupe1sujet4';
GRANT ALL PRIVILEGES ON DATABASE projetGroupe1 to utilisateur_projet;
CREATE TYPE type_salle AS ENUM ('salle de cours', 'bureau', 'amphitheatre');
CREATE TABLE Salle (
   numero INTEGER,
   batiment VARCHAR(20),
   type type_salle,
   nbPersonne INTEGER NOT NULL,
   PRIMARY KEY (numero, batiment)
);

CREATE TABLE association(
    nom VARCHAR(25) PRIMARY KEY,
    description VARCHAR(250),
    mail VARCHAR(25) NOT NULL,
    dateCrea DATE NOT NULL,
    siteWeb VARCHAR(25),
    categorie VARCHAR(25),
    numeroSalle INT,
    batimentSalle VARCHAR(20),
    FOREIGN KEY (numeroSalle,batimentSalle) REFERENCES salle(numero,batiment) ON DELETE CASCADE
);

CREATE TABLE Personne(
     id SERIAL,
     nom VARCHAR(30),
     prenom VARCHAR(30),
     PRIMARY KEY (id)
);

CREATE TYPE cat AS ENUM ('etudiant', 'enseignant', 'administratif', 'technique');
CREATE TABLE universitaire (
    personne INTEGER,
    CIN INTEGER UNIQUE NOT NULL,
    categorie cat,
    PRIMARY KEY (personne),
    FOREIGN KEY (personne) REFERENCES Personne(id) ON DELETE CASCADE
);

CREATE TABLE PersonneExterieure (
    personne INTEGER,
    numeroTelephone INTEGER UNIQUE NOT NULL,
    organismeAffiliation VARCHAR(30),
    PRIMARY KEY (personne),
    FOREIGN KEY (personne) REFERENCES Personne(id) ON DELETE CASCADE
);


CREATE TYPE role_asso AS ENUM('president', 'tresorier', 'membre');
CREATE TABLE membre (
    role role_asso,
    nomAssociation VARCHAR(25),
    CIN INT,
    PRIMARY KEY(role, nomAssociation, CIN),
    FOREIGN KEY (nomAssociation) REFERENCES association(nom) ON DELETE CASCADE,
    FOREIGN KEY (CIN) REFERENCES universitaire(CIN) ON DELETE CASCADE
);

/*PREMIER ARRET*/
CREATE TYPE genre_standup AS ENUM('spectacle comique', 'debat', 'table ronde', 'NULL');
CREATE TYPE typeSpectacle AS ENUM('concert', 'stand-up', 'piece de theatre');
CREATE TABLE spectacle (
    nom VARCHAR(25) PRIMARY KEY,
    duree TIME NOT NULL,
    compositeur VARCHAR(50),
    anneeParution DATE,
    genreConcert VARCHAR(25),
    auteur VARCHAR(25),
    typeTheatre VARCHAR(25),
    genreStandUp genre_standup,
    association VARCHAR(25),
    FOREIGN KEY (association) REFERENCES association(nom) ON DELETE CASCADE
);


CREATE TABLE role(
    role VARCHAR(25),
    CIN INT,
    nomSpectacle VARCHAR(25),
    PRIMARY KEY(role, CIN, nomSpectacle),
    FOREIGN KEY (CIN) REFERENCES universitaire(CIN) ON DELETE CASCADE,
    FOREIGN KEY (nomSpectacle) REFERENCES spectacle(nom) ON DELETE CASCADE
);

CREATE TABLE seance(
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    nomSpectacle VARCHAR(25),
    numeroSalle INTEGER,
    batimentSalle VARCHAR(20),
    FOREIGN KEY (nomSpectacle) REFERENCES spectacle(nom) ON DELETE CASCADE,
    FOREIGN KEY (numeroSalle,batimentSalle) REFERENCES salle(numero, batiment) ON DELETE CASCADE
);

CREATE TABLE CategorieBillet(
    nom VARCHAR(25),
    nbrPlace INT NOT NULL,
    PRIMARY KEY(nom)
);

CREATE TABLE Billet(
    dateCreation DATE NOT NULL,
    personne INTEGER,
    tarif INTEGER NOT NULL,
    categorie VARCHAR(25),
    seance INT,
    PRIMARY KEY (personne, categorie),
    FOREIGN KEY (personne) REFERENCES Personne (id) ON DELETE CASCADE,
    FOREIGN KEY (categorie) REFERENCES categorieBillet (nom) ON DELETE CASCADE,
    FOREIGN KEY (seance) REFERENCES Seance(id) ON DELETE CASCADE
);