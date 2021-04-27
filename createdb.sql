DROP TABLE salle CASCADE;DROP TABLE association CASCADE;DROP TABLE membre CASCADE;DROP TABLE personne CASCADE;DROP TABLE universitaire CASCADE;DROP TABLE personneExterieure CASCADE;DROP TABLE role CASCADE;DROP TABLE spectacle CASCADE;DROP TABLE billet CASCADE;DROP TABLE seance CASCADE;DROP TABLE categorieBillet CASCADE;
DROP TYPE type_salle;DROP TYPE cat;DROP TYPE role_asso;DROP TYPE genre_standup;DROP TYPE typeSpectacle;
CREATE TYPE type_salle AS ENUM ('salle de cours', 'bureau', 'amphitheatre');
CREATE TABLE Salle (
   numero INTEGER,
   batiment VARCHAR(20) NOT NULL,
   type type_salle,
   nbPersonne INTEGER NOT NULL,
   PRIMARY KEY (numero)
);

CREATE TABLE association(
    nom VARCHAR(25) PRIMARY KEY,
    description VARCHAR(250),
    mail VARCHAR(25) NOT NULL,
    dateCrea DATE NOT NULL,
    siteWeb VARCHAR(25),
    categorie VARCHAR(25),
    numeroSalle INT,
    FOREIGN KEY (numeroSalle) REFERENCES salle(numero)
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
    FOREIGN KEY (personne) REFERENCES Personne(id)
);

CREATE TABLE PersonneExterieure (
    personne INTEGER,
    numeroTelephone INTEGER UNIQUE NOT NULL,
    organismeAffiliation VARCHAR(30),
    PRIMARY KEY (personne),
    FOREIGN KEY (personne) REFERENCES Personne(id)
);


CREATE TYPE role_asso AS ENUM('president', 'tresorier', 'membre');
CREATE TABLE membre (
    role role_asso,
    nomAssociation VARCHAR(25),
    CIN INT,
    PRIMARY KEY(role, nomAssociation, CIN),
    FOREIGN KEY (nomAssociation) REFERENCES association(nom),
    FOREIGN KEY (CIN) REFERENCES universitaire(CIN)
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
    FOREIGN KEY (association) REFERENCES association(nom)
);


CREATE TABLE role(
    role VARCHAR(25),
    CIN INT,
    nomSpectacle VARCHAR(25),
    PRIMARY KEY(role, CIN, nomSpectacle),
    FOREIGN KEY (CIN) REFERENCES universitaire(CIN),
    FOREIGN KEY (nomSpectacle) REFERENCES spectacle(nom)
);

CREATE TABLE seance(
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    nomSpectacle VARCHAR(25),
    numeroSalle INTEGER,
    FOREIGN KEY (nomSpectacle) REFERENCES spectacle(nom),
    FOREIGN KEY (numeroSalle) REFERENCES salle(numero)
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
    FOREIGN KEY (personne) REFERENCES Personne (id),
    FOREIGN KEY (categorie) REFERENCES categorieBillet (nom),
    FOREIGN KEY (seance) REFERENCES Seance(id)
);