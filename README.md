NOTE DE CLARIFICATION PROJET DE NF18 : Maxime GRORET, Florestan BIAUX, Shilang YE, Augustin de LAUBIER



Salle :

La classe salle respecte toutes les contraintes de l’énoncé. 

Attributs :
- numéro (obligatoire) que l’on défini comme clé primaire
- bâtiment (obligatoire)
- type (obligatoire)
- nbpersonne (obligatoire)



Association :
	
La classe association possède les caractéristiques énoncées dans le texte, ce qui nous donne :

Attribut :
- nom de l’association (clé primaire),
- description de l’association (obligatoire),
- adresse email de l’association (obligatoire),
- date de création de l’association, (obligatoire)
- site web éventuel,
- catégorie de l’association (obligatoire),
Cette relation est associée à la classe salle pour avoir des précisions sur les lieux de réunions. 



Membre :

La classe membre est un classe d’association entre Universitaires et Association qui décrit l’adhésion des étudiants aux associations.

Attribut :
- role du membre dans l’association (President, Trésorier ou membre) en clé primaire,
Une contrainte sera à faire pour qu’uniquement les étudiants puissent adhérer aux associations. L’étudiant concerné ainsi que l’association feront office également de clé primaire pour identifier chaque rôle.



Personne :

Il s’agit d’une classe abstraite qui sert à regrouper les différentes catégories de personnes, les universitaires et les personnes extérieures à l’université.

Attribut : 
- nom(obligatoire),
- prénom(obligatoire),
Ces attributs ne font pas offices de clé primaires, étant donné que deux personnes peuvent avoir le même couple nom/prénom. On va donc chercher les clés primaires dans les attributs non-hérités (CIN et numéro de téléphone).



Universitaire :

La classe universitaire est une classe fille de la classe personne. Elle permet de simplifier la relation entre les différents acteurs et les spectacles en respectant la consigne de l’énoncé.

Attributs :
- CIN comme clé primaire,
- Catégorie (obligatoire) qui est une énumération de possibilité pour correspondre aux catégories de l’énoncé,
L'existence de cette classe permet d'éviter la redondance en créant de multiples classes correspondant aux catégories de l'énoncé.



Personne extérieure :

La classe personne extérieure correspond à toute personne ne faisant pas partie de l’université UTX. Cette classe est une classe fille de la classe Personne elle hérite donc des attributs de celle-ci.

Attributs (non-hérités) :
- numéro de téléphone en clé primaire, 
- organisme auquel elle est affiliée,(obligatoire)



Spectacle :

La classe spectacle est une classe abstraite qui peut être une pièce de théâtre, un concert ou un stand-up. 

Attributs :
- Nom du spectacle en clé primaire,
- durée spécifique en minutes(obligatoire),



Rôle :

Il s’agit de la classe permettant de traduire l’association entre les “Universitaires” et les Spectacles, qui permet d’indiquer le rôles du participant dans le spectacle.

Attribut :
- Role du participant dans le spectacle en clé primaire,
On identifiera chaque rôle ici par l’ajout de clé étrangère qui feront office de clé primaire (clés primaires d’universitaire et clé primaire de spectacle).



Concert :

La classe concert est une classe fille de la classe Spectacle. Elle hérite donc de ses attributs . On garde ici comme clé le nom du spectacle.

Attributs :
- Compositeur (obligatoire)
- Année de parution (obligatoire)
- Genre (obligatoire)



Pièce de théâtre :

La pièce de théâtre est une classe fille de la classe Spectacle. Elle hérite donc de ses attributs. On garde ici comme clé le nom du spectacle.

Attributs (non-hérités) :
- Auteur (obligatoire),
- Date de parution (obligatoire),
- type de la pièce (obligatoire),
On peut également songer à avoir la date de parution et l’auteur en clé primaire dans le cas où il y a une réédition d’une pièce de théâtre, cependant on suppose ici que le nom du spectacle inclura ce genre d’information et identifiera à lui seul le spectacle.



Stand-up :

La classe Stand-up est une classe fille de la classe Spectacle. 

Attribut :
- genre du spectacle (comique, débat, table ronde)(obligatoire),



Séance :

Il s’agit de la classe traduisant la représentation d’un spectacle dans une certaine salle, elle constitue donc un intermédiaire entre ces deux classes.

Attribut : 
- date de la séance,(obligatoire)
On note également que les clés étrangères associées à la salle et au spectacle feront office de clés primaires également pour identifier de manière unique la séance.



Catégorie-Billet :

La classe Catégorie_Billet permet la décomposition des billets en plusieurs catégorie. Elle permet ainsi à une personne d’acheter des billets dans des catégories spécifiques en exprimant une contrainte. Ex : un étudiant achète une place de la catégorie “place étudiante”, une personne extérieure devra acheter une place “place extérieur” et ainsi de suite. 

Attribut :
- Nom de la catégorie, en clé primaire,
- tarif lié à la catégorie,(obligatoire)
- Nombre de places pouvant être vendues dans cette catégorie(obligatoire)
Il est à noter que chacuns des spectacles auront des catégories avec des tarifs et des nombres de places pour cette catégorie uniques à leur spectacle. On pourra ajouter donc en clé étrangère et primaire les clés primaires de la séance. 



Billet :

Il s’agit de la classe qui va de pair avec Catégorie_billet, et qui permet ici de rajouter une couche d’identification de l’utilisateur qui ne peut pas être inclus dans la classe Catégorie_billet. Elle est également dépendante du cycle de vie de cette classe car elle nécessite l’appartenance à une catégorie de billet qui indique le tarif par exemple.  L’utilisateur indique sur son billet la catégorie et le spectacle, et obtient le prix grâce à la classe Catégorie. 

Attribut : 
- nom de la personne achetant la place,(obligatoire)
- prénom de la personne achetant la place,(obligatoire)
- date de création du billet, (obligatoire)