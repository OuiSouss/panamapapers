#!/bin/bash

#creation dossier pour le projet
mkdir panamas
cd panamas

#recupération des données des panamas papers
wget https://cloudfront-files-1.publicintegrity.org/offshoreleaks/data-csv.zip#_ga=1.219142096.879855386.1479914266


#téléchargement de neo4j
wget https://neo4j.com/artifact.php?name=neo4j-community-3.0.7-unix.tar.gz -O neo4j.tar.gz

#installation de neo4j
tar -xf neo4j.tar.gz
mv neo4j-community-3.0.7/* neo4j #add '/*' because before you just moved the folder
rm -r neo4j-community-3.0.7 #remove empty folder

#dézipper data
unzip -j data-csv.zip -d neo4j/import

#delete all the zip files
rm data-csv.zip
rm neo4j.tar.gz

#Partie pour l'utilisation de flask
#si vous êtes sur une machine du cremi python 2.7 , pip et virtualenv sont déjà installé
#Voici ce qu'il faut faire pour travailler avec flask

mkdir flaskproject
cd flaskproject
virtualenv venv
. venv/bin/activate
#installation de Flask dans l'environnement
pip install Flask
#installation du driver neo4j dans l'environnement afin de l'utiliser pour la visualisation
pip install neo4j-driver

#Mise en place des dossiers pour flask
mkdir static
mkdir templates
cp ../../app.py .
cp ../../data.json ./static
cp ../../panama-visu.html ./static
cp ../../panama-visu.html ./templates
