Voici un mode d'emploi pour utiliser Neo4J, construire la base de donnée et la visualisation de données.


On suppose que l'on utilise un ordinateur du Cremi avec python 2.7, virtualenv, pip, chromimium

On suppose que l'on travaille dans un dossier appelé test-panamas et que tous les fichiers de l'archive s'y trouveront après dézippage.

1) Désarchiver l'archive comme suit dans un dossier de votre répertoire en créant un fichier où tout mettre :

par exemple: mkdir test-panamas
dézipper panamas.zip dans test-panamas:
cd test-panamas
déplacer panamas.zip depuis son emplacement actuel jusque dans test-panamas

unzip panamas.zip

2) Executer le script prerequis.sh depuis test-panamas:

./prerequis.sh

3) Modifier le fichier Addresses.csv comme suit:

Ouvrir un éditeur de texte le chemin depuis le fichier test-panamas est panamas/neo4j/import/Addresses.csv

Dans le fichier csv Addresses.csv à la ligne 124 786 : 
"11F.-2, No. 102, GUANGFU S. RD., XINYI DISTRICT, Taipei City 110, Taiwan, R.O.C \",,The Offshore Leaks data is current through 2010,TWN,Taiwan,242192,Offshore Leaks

Enlever le backslash sur l'adresse entre guillements.

4) Activer neo4j depuis test-panamas:
panamas/neo4j/bin/neo4j start

5) Executer le script import-data.sh depuis test-panamas:
./import-data.sh

Ce script importe les données csv dans neo4j


Pour afficher la petite application web:

1) activer l'environnement virtuel depuis test-panamas:

Taper dans un terminal:

cd panamas/flaskproject
. venv/bin/activate

2) activer les fonctionnalités expérimentales de javascript dans chromium dans les flags.

3) Executer app.py comme suit:

python app.py

4) Ouvrir chromium et taper l'url afficher après l'execution de précédente quelque chose semblable à ceci:

http://127.0.0.1:5000/

5) Ajouter les parties suivante selon le bon vouloir à la fin de l'url. 


