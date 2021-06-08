<h1> NF18 : Projet </h1>

*BIAUX Florestan - DE LAUBIER Augustin - GORET Maxime - YE Shilang*

<h2>MLD</h2>

```
salle(#numero : int, #batiment :string not NULL, type : {'salle de cours', 'bureau', 'amphitheatre'}, nbPersonne : int not NULL)

association(#nom : string, description : string, mail : string NOT NULL, dateCrea: Date not NULL, siteWeb: string, categorie: string, numeroSalle=>salle)

membre(#role:{'president', 'tresorier', 'membre'}, #nomAssociation=>association, #CIN=>universitaire) *mais categorie == etudiant*

personne(#id : int, nom : string, prenom : string);

universitaire(#personne=> personne, CIN : int UNIQUE not NULL, categorie: {'etudiant', 'enseignant', 'administratif', 'technique'}) with CIN local key

personneExterieure(#personne=> personne, numeroTelephone : int UNIQUE not NULL, organismeAffiliation : string NOT NULL) with numeroTelephone local key

role(#role: string, #CIN=>universitaire, #nomSpectacle=>spectacle)

spectacle(#nom : string, duree : int not NULL, compositeur : string , anneeParution : date, genreConcert : string , auteur : string , typeTheatre : string, genreStandUp : {'spectacle comique', 'debat', 'table ronde', NULL}, typeSpectacle : {'concert', 'stand-up', 'piece de theatre'}, association=>association)

billet(dateCreation : Date NOT NULL , #personne=>personne, #categorie=>categorieBillet, tarif : int not NULL)

seance(#id : int, date : Date, nomSpectacle=>spectacle, numeroSalle=>salle)

categorieBillet(#nom : string, nbrPlace : int not NULL)
```

<h2>Note de clarification</h2>

<h3>Modélisation de la Base de Données</h3>

Le principe de cette BDD est de modéliser un système associatif tel que l'on peut le voir à l'UTC, qui contient:
- la liste des étudiants, du personnel (enseignant et technique) ainsi que des personnes extérieures participant aux évènements,
- la liste des associations, les étudiants les composant,
- la liste des salles servant de salle de réunions aux associations ou encore de salle de spectacle pour les évènements organisées par les associations,
- La liste des spectacles organisées par les associations, ainsi que la liste des séances affiliées à ceux-ci.
- La liste des billets achetés par les personnes pour les séances des spectacles. 

<h3> Explicitation des objets énoncés dans l'UML </h3>
<h4>Salle :</h4>

La classe salle respecte toutes les contraintes de l’énoncé. 

**Attributs :**
- numéro (obligatoire) que l’on défini comme clé primaire
- bâtiment (obligatoire)
- type (obligatoire)
- nbpersonne (obligatoire)



<h4>Association :</h4>
	
La classe association possède les caractéristiques énoncées dans le texte, ce qui nous donne :

**Attribut :**
- nom de l’association (clé primaire),
- description de l’association (obligatoire),
- adresse email de l’association (obligatoire),
- date de création de l’association, (obligatoire)
- site web éventuel,
- catégorie de l’association (obligatoire),
Cette relation est associée à la classe salle pour avoir des précisions sur les lieux de réunions. 



<h4>Membre :</h4>

La classe membre est un classe d’association entre Universitaires et Association qui décrit l’adhésion des étudiants aux associations.

**Attribut :**
- role du membre dans l’association (President, Trésorier ou membre) en clé primaire,
Une contrainte sera à faire pour qu’uniquement les étudiants puissent adhérer aux associations. L’étudiant concerné ainsi que l’association feront office également de clé primaire pour identifier chaque rôle.



<h4>Personne :</h4>

Il s’agit d’une classe abstraite qui sert à regrouper les différentes catégories de personnes, les universitaires et les personnes extérieures à l’université.

**Attribut :**
- nom(obligatoire),
- prénom(obligatoire),
Ces attributs ne font pas offices de clé primaires, étant donné que deux personnes peuvent avoir le même couple nom/prénom. On a donc une clé artificielle id faisant office de clé primaire. Nous avons fait le choix de la clé artificielle par soucis d'optimisation. En effet, on observe qu'il faut que Billet ait une clé étrangère sur Personne, et les classes filles de personne également. 



<h4>Universitaire :</h4>

La classe universitaire est une classe fille de la classe personne. Elle permet de simplifier la relation entre les différents acteurs et les spectacles en respectant la consigne de l’énoncé.

**Attributs :**
- CIN comme clé primaire,
- Catégorie (obligatoire) qui est une énumération de possibilité pour correspondre aux catégories de l’énoncé,
L'existence de cette classe permet d'éviter la redondance en créant de multiples classes correspondant aux catégories de l'énoncé.



<h4>Personne extérieure :</h4>

La classe personne extérieure correspond à toute personne ne faisant pas partie de l’université UTX. Cette classe est une classe fille de la classe Personne elle hérite donc des attributs de celle-ci.

**Attributs (non-hérités) :**
- numéro de téléphone en clé primaire, 
- organisme auquel elle est affiliée,(obligatoire)



<h4>Spectacle :</h4>

La classe spectacle est une classe abstraite qui peut être une pièce de théâtre, un concert ou un stand-up. 

**Attributs :**
- Nom du spectacle en clé primaire,
- durée spécifique en minutes(obligatoire),



<h4>Rôle :</h4>

Il s’agit de la classe permettant de traduire l’association entre les “Universitaires” et les Spectacles, qui permet d’indiquer le rôles du participant dans le spectacle.

**Attribut :**
- Role du participant dans le spectacle en clé primaire,
On identifiera chaque rôle ici par l’ajout de clé étrangère qui feront office de clé primaire (clés primaires d’universitaire et clé primaire de spectacle).



<h4>Concert :</h4>

La classe concert est une classe fille de la classe Spectacle. Elle hérite donc de ses attributs . On garde ici comme clé le nom du spectacle.

**Attributs :**
- Compositeur (obligatoire)
- Année de parution (obligatoire)
- Genre (obligatoire)



<h4>Pièce de théâtre :</h4>

La pièce de théâtre est une classe fille de la classe Spectacle. Elle hérite donc de ses attributs. On garde ici comme clé le nom du spectacle.

**Attributs (non-hérités) :**
- Auteur (obligatoire),
- Date de parution (obligatoire),
- type de la pièce (obligatoire),
On peut également songer à avoir la date de parution et l’auteur en clé primaire dans le cas où il y a une réédition d’une pièce de théâtre, cependant on suppose ici que le nom du spectacle inclura ce genre d’information et identifiera à lui seul le spectacle.



<h4>Stand-up :</h4>

La classe Stand-up est une classe fille de la classe Spectacle. 

**Attribut :**
- genre du spectacle (comique, débat, table ronde)(obligatoire),



<h4>Séance :</h4>

Il s’agit de la classe traduisant la représentation d’un spectacle dans une certaine salle, elle constitue donc un intermédiaire entre ces deux classes.

**Attribut :**
- date de la séance,(obligatoire)
On note également que les clés étrangères associées à la salle et au spectacle feront office de clés primaires également pour identifier de manière unique la séance.



<h4>Catégorie-Billet :</h4>

La classe Catégorie_Billet permet la décomposition des billets en plusieurs catégorie. Elle permet ainsi à une personne d’acheter des billets dans des catégories spécifiques en exprimant une contrainte. Ex : un étudiant achète une place de la catégorie “place étudiante”, une personne extérieure devra acheter une place “place extérieur” et ainsi de suite. 

**Attribut :**
- Nom de la catégorie, en clé primaire,
- tarif lié à la catégorie,(obligatoire)
- Nombre de places pouvant être vendues dans cette catégorie(obligatoire)
Il est à noter que chacuns des spectacles auront des catégories avec des tarifs et des nombres de places pour cette catégorie uniques à leur spectacle. On pourra ajouter donc en clé étrangère et primaire les clés primaires de la séance. 



<h4>Billet :</h4>

Il s’agit de la classe qui va de pair avec Catégorie_billet, et qui permet ici de rajouter une couche d’identification de l’utilisateur qui ne peut pas être inclus dans la classe Catégorie_billet. Elle est également dépendante du cycle de vie de cette classe car elle nécessite l’appartenance à une catégorie de billet qui indique le tarif par exemple.  L’utilisateur indique sur son billet la catégorie et le spectacle, et obtient le prix grâce à la classe Catégorie. 

**Attribut :**
- nom de la personne achetant la place,(obligatoire)
- prénom de la personne achetant la place,(obligatoire)
- date de création du billet, (obligatoire)

<h3>Rôle et Libertés de l'Utilisateur</h3>
Le principe est ici de donner le moindre droit à l'utilisateur, afin d'éviter toute insécurité au sein de la Base de données.

**Etudiant**

Si l'utilisateur est un étudiant, il peut effectuer les actions suivantes :
- s'inscrire ou/et créer une association, (=> Modification de la Base de donnée au niveau de la classe Association)
- Affilier une salle de Réunion à son association dans le cas où il possède les droits, (=> Modification de la Base de donnée au niveau de la classe Association et Salle),
- participer à un spectacle avec un certain rôle (=> Modification de la Base au niveau de la classe Rôle)
- Acheter un ou plusieurs billet pour un spectacle  (=> Modification de la Base de donnée au niveau de la classe Billet)

**Personnel**

Si l'utilisateur est un membre du personnel technique ou enseignant, il peut effectuer les actions suivantes :
- participer à un spectacle avec un certain rôle (=> Modification de la Base au niveau de la classe Rôle)
- Acheter un ou plusieurs billet pour un spectacle  (=> Modification de la Base de donnée au niveau de la classe Billet)

**Personne extérieure à l'UTX**

Si l'utilisateur est extérieure à l'UTX, il peut effectuer les actions suivantes :
- Acheter un ou plusieurs billet pour un spectacle  (=> Modification de la Base de donnée au niveau de la classe Billet)


<h2>Installlation en local et test du Projet</h2>

<h3>Installation et configuration de la Base de donnée</h3>

Tout d'abord, il faut créer la base de donnée et retenir son nom, pour cela on effectue la commande suivante : 

```
createdb <nomBDD>
psql nomBDD
```

Ensuite pour créer les différentes tables, il faut tout d'abord copier/coller le contenu du fichier createdb.sql dans le terminal PostgreSQL puis effectuer la même étape avec le contenu du fichier insertData.sql pour le remplissage.

Pour enfin relier le projet à sa base de donnée, il suffit de remplacer les champs '#' en face de **dbname**, **user**, **password** du fichier **connection_db.py** à la ligne 6 qui est la suivante : 

```
return psycopg2.connect("host=localhost dbname=# user=# password=#")
```

<h3>Lancement et test du projet</h3>

Pour cela, il suffit de se placer dans le dossier **applicatif_python** et d'exécuter la commande suivante :

```python3 menu.py```

Un menu propose alors les différents choix qui vous sont proposés, à vous de choisir. 

<h3>Résolution de bug</h3>

Dans le cas où il est indiqué que la bibliothèque psycopg2 est inconnue, avec l'erreur suivante : 

```ModuleNotFoundError: No module named 'psycopg2'```

Il suffit d'installer le module psycopg2 avec la commande suivante : 

```pip3 install psycopg2-binary```

Pour activer l'envirronement virtuel et lancer le projet, il suffit de lancer les commandes suivantes :

- Sous système UNIX : 

``` 
cd ../
source venv/bin/activate 
```

- Sous Windows, après s'être placé dans le fichier principal : 

```
venv\Scripts\activate
```

<h2>Deuxième rendu de projet : Etude de la normalisation, des dépendances fonctionnelles, et de la conversion de données en NoSQL</h2>

<h3>Tables étudiées</h3>

<h4>Salle : </h4> (#numero : int, #bâtiment :string not NULL, type : {'salle de cours', 'bureau', 'amphithéâtre'}, nbPersonne : int not NULL)
<h4>Association : </h4> (#nom : string, description : string, mail : string NOT NULL, dateCrea: Date not NULL, siteWeb: string, categorie: string, numeroSalle=>salle)
<h4>Spectacle : </h4> (#nom : string, duree : int not NULL, compositeur : string , anneeParution : date, genreConcert : string , auteur : string , typeTheatre : string, genreStandUp : {'spectacle comique', 'débat', 'table ronde', NULL}, typeSpectacle : {'concert', 'stand-up', 'piece de theatre'}, association=>association)
<h4>Séance : </h4> (#id : int, date : Date, nomSpectacle=>spectacle, numeroSalle=>salle)

<h3>Etude des dépendance fonctionnelles de ces tables </h3>

- **Salle :** (numéro, bâtiment) => type, nbPersonne
- **Séance :** id => spectacle, numéro, bâtiment, date
- **Association :**  nom => description, mail, dateCrea, siteWeb, catégorie, numéro, bâtiment
- **Spectacle :** nom => duree, compositeur, anneeParution, genreConcert, auteur, typeTheatre, genreStandUp, typeSpectacle, association

<h3>Formes Normales </h3>

Les classes salles, association, spectacle et séance ne contiennent que des attributs atomiques. Elles sont donc 1NF.

Les classes associations, séances et spectacle sont forcément 2NF car 1NF et que la clé ne possède qu’un attribut. En ce qui concerne la classe salle, elle est également 2NF car ses deux attributs non-clés type et nbPersonne ne sont pas déterminés par une sous partie de la clé.

Les classes associations, séance , spectacle et salle sont 3NF car 2NF et que leurs attributs n'appartenant à aucune clé candidate ne dépend directement que de clés candidates.

<h3>Passage de données en NoSQL (JSon et PostgreSQL)</h3>

Nous avons décidé de passer les séances ainsi que les catégories de billet en attribut JSon de la table spectacle. En effet, il semblerait logique que lors de l'ajout d'un spectacle donné, il faille déclarer la date ainsi que la localisation des différentes séances, ainsi que les différentes catégories de billet que l'on pourrait trouver lors de cette séance.
On a donc dans un tuple spectacle un tableau de json de séances contenant également en plus de ses attributs un tableau de json de catégorie de billets. 
Les modifications à notifier sont dans les fichiers insertData.sql, createdb.sql, seance.sql, seance.py et spectacle.py. Nous avons par ailleurs adapter les différents fichiers qui sont touchés par ces modifications.

