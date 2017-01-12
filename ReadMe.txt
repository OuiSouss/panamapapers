Mode d'emploi


Introduction

Ce mode d'emploi sert à construire la base de données avec Neo4j en utilisant les données des panamas papers. De plus, nous pourrons aussi visualiser un histogramme grâce à un connexion à la base de donnée et le framework Flask.
Pré-requis

Tout d'abord, il faut être en possession des données utiles pour le projet qui se trouvent : https://cloudfront-files-1.publicintegrity.org/offshoreleaks/data-csv.zip#_ga=1.110058316.879855386.1479914266

De plus, il faut être en possession des logiciels nécessaire, correctement installés. Donc, nous supposerons que ceci est le cas pour :

    Neo4j
    python 2.7
    virtualenv
    pip
    chromium
    Flask 

Enfin, ayant fait ce projet grâce à des systèmes unix, je ne garanti pas la compatibilité sur un autre système d'exploitation.
Configuration

Après avoir récupérer les données et les avoir dé-zipper, il faut les placées dans un dossier nommé import. De plus, pour visualiser les données en histogramme, il faut télécharger les données utiles que j'ai joint dans l'archive c'est à dire data.json, et panama-visu.html. Il faut mettre dans le dossier du projet flask où l'environnement virtuel est installé les dossiers static et templates ainsi que le fichier app.py qui nous permettra de visualiser les données.


Pré-traitement

Avant de pouvoir importer les données dans Neo4j, il faut effectuer des pré-traitement dans le fichier Addresses.csv. Avec un éditeur de texte tel que gedit, il faut enlever un \ sur la ligne 124 786 présent dans l'adresse juste avant un guillemet.


Import des données dans Neo4j

Tout d'abord, lancer neo4j avec la commande bin/neo4j start, à l'adresse url localhost précisée se connecter, ensuite il faut lancer le script d'import de la façon suivante en se plaçant d'abord dans le dossier import de neo4j:

../bin/neo4j-shell -file ../../../script_cypher_import.cypher

Il est important de vérifier et modifier le chemin que j'ai mis selon où vous avez placer ce fichier cypher.

Si tout s'est bien passé vous devriez pouvoir visualiser les données importer grâce au browser de neo4j.


Application web

Pour visualiser l'histogramme, il faut activer l'environnement virtuel comme suit en se plaçant dans le dossier du projet où l'environnement est installé:

. venv/bin/activate

venv correspond au nom du dossier de l'environnement virtuel.

Ensuite, il faut activer les fonctionnalités expérimentales de javascript dans les flags du navigateur chromium. Sur chrome, il se trouve qu'il faut faire la même chose et normalement l'application fonctionne identiquement. Néanmoins, je ne garantis pas que l'application fonctionnera sur un autre navigateur.

Voici la commande à lancer pour mettre en route l'application :

python app.py

pour visualiser les histogramme tester les routes suivantes (à ajouter dans l'url après le localhost:5000):

    /histo : affichage en statique
    /histo_temp : affichage en templating
    /neo : un premier test de conexion avec neo4j
    /neo_graph : affichage avec connexion

Si sur l'étape 3 et 4, il y a un problème essayez de lancer neo4j en parallèle et connecter vous.


N'ayant pas fini mon script pour l'import des arêtes, je ne le joins pas au rendu. J'essayerai d'en avoir un fonctionnel pour la rentrée avec du retard. 
