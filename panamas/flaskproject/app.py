#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Welcome to our L3-projet-techno application about panama papers . This will give you a
 guided tour around creating our application using Flask-Bootstrap and other package.
 From Amélie Risi, Chloe Pathé, Lucas Vivas

 To run this application yourself, please activate virtualennv first in flaskproject folder:
   $ . venv/bin/activate
 Then, install its requirements first:

   $ pip install -r requirements.txt

 Then, you can actually run the application.
   $ python app.py

 Afterwards, point your browser to http://localhost:5000, then check out the
 source.
"""

# TODO: check validation country->country doit renvoyer un script
# FAIT: check validation impossiblité de something->Country et l'inverse
# FAIT: afficher sens des edges
# FAIT: afficher le nom des edges (exemple : http://bl.ocks.org/jhb/5955887)
# FAIT: couleur en fonction des labels (officer, entity ...)
#en plus
# TODO: profondeur de recherche
# TODO: mettre les noms into les nodes


from flask import Flask, render_template, json, url_for, request, flash, Blueprint, redirect, jsonify
from neo4j.v1 import GraphDatabase, basic_auth
from flask_bootstrap import Bootstrap
from flask_appconfig import AppConfig
from flask_debug import Debug
from form import SignupForm, TestForm, CountryForm

frontend = Blueprint("app", __name__)
"""
    Création de l'application Flask
    Initialisation de Bootstrap, Debug,
"""
def create_app(configfile=None):
    app = Flask(__name__)
    AppConfig(app)
    Bootstrap(app)
    Debug(app)
    app.register_blueprint(frontend)
    app.config["BOOTSTRAP_SERVE_LOCAL"] = True
    app.secret_key = 'myverylongsecretkey'
    return app

app = create_app()

global driver,session

driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "neo"))
session = driver.session()

"""
    :return: index.html page d'accueil
"""
@app.route("/")
def index():
    return render_template("index.html")

"""
    :param name: string enter dans l'url
    :return: affiche la string
"""
@app.route("/hello/<name>")
def hello(name):
    return "hello " + name

"""
    :return: hello s dans le cas de défault sinon
    hello quelquechose si url=  hello2?name=moi
"""
@app.route("/hello2")
def hello2():
    name = request.args.get('name', 's')
    return "hello " + name

"""
    :return: un histo qui est sur panama-visu.html dans le dossier static
"""
@app.route ("/histo")
def histo():
    return app.send_static_file("panama-visu.html")

"""
    :return: envoi le fichier data qui sera utilisé par la route histo
"""
@app.route("/data.json")
def data():
    return app.send_static_file("data.json")

"""
    :return: retourne panama-visu.html du dossier template après avoir chargé
    le fichier data.json en static
"""
@app.route("/histo_temp")

def histo_temp():
    f = open("static/data.json")
    data = json.load(f)
    return render_template("panama-visu.html", data=data)

"""
    :param type: string présent dans le json data
    :return: affiche un message selon le type entrer dans l'url
    un message de non trouvé sinon
"""
@app.route("/data/count/<type>")
def data_count(type):
    f = open("static/data.json")
    data = json.load(f)
    if type in data :
        return "Nombre de noeuds de " + type + " = " + str(data[type])
    else:
        return "Type not specify or type doesn't exist in data"

"""
    :return: nombre d'intermediaire trouvé dans la base de donnée
"""
@app.route("/count_test_neo")
def count_test_neo():
    result = session.run("match (n:Intermediary) return count(n) as nombre")
    res = 0
    for rec in result:
        res = rec["nombre"]
    return str(res)

"""
    :param driver: accès via GraphDatabase à notre base de donnée Neo4j
    :param n_type: string nom d'un label de la base de donnée
    :return: nombre de noeud du type n_type
"""
def count_type(driver, n_type):
    result = session.run("match (n:%s) return count(n) as nombre"%n_type)
    res = 0
    for rec in result:
        res = rec["nombre"]
    return res

"""
    :return: rend la page panama-visu avec templating
    data correspond à un dictionaire avec le nombre de noeud de chaque types
"""
@app.route("/histo_count_neo")
def histo_count_neo():

    nb_intermediaries = count_type(driver, "Intermediary")
    nb_addresses = count_type(driver, "Address")
    nb_entities = count_type(driver, "Entity")
    nb_officers = count_type(driver, "Officer")
    data ={
        "Addresses": nb_addresses,
        "Entities": nb_entities,
        "Intermediaries": nb_intermediaries,
        "Officers": nb_officers}
    return render_template("panama-visu.html", data = data)

"""
    :return: vue countries.hmtl histogramme nombre des interactions entre les pays de notre liste
"""
@app.route("/histo_count_countries")
def histo_count_countries():
    countries_array = ['South Africa', 'Liechtenstein', 'Monaco', 'Belgium', 'Lebanon', 'Switzerland', 'Malaysia', 'Spain', 'United Kingdom', 'Jersey', 'France', 'Luxembourg', 'Taiwan', 'Estonia', 'Mexico', 'Argentina', 'Guernsey', 'United States', 'Venezuela', 'Hong Kong', 'Panama', 'Saudi Arabia', 'Germany', 'Kuwait', 'Poland', 'Brazil', 'Turkey', 'Egypt', 'Canada', 'Portugal', 'Russia', 'Isle of Man', 'Malta', 'Hungary', 'Israel', 'Greece', 'Philippines', 'Italy', 'China', 'Gibraltar', 'Bahamas', 'Honduras', 'Australia', 'Austria', 'Sweden', 'Slovenia', 'Uruguay', 'Thailand', 'Ecuador', 'Colombia', 'United Arab Emirates', 'Peru', 'Czech Republic']

    data ={}
    for country1 in countries_array:
        s = 0
        i = countries_array.index(country1)
        for country2 in countries_array:
            result = session.run("MATCH (n:Country)-[r]->(m:Country) WHERE (n.country = '" + country1 + "' and m.country = '" + country2 + "') RETURN r.cpt_int as inter")
            for r in result:
                s += r["inter"]
        print i
        if country1 == 'United Kingdom':
            country1 = 'UK'
        data[country1] = s
    return render_template("countries-visu.html", data = data)

"""
    :return: vue de visualisation avec d3 du graphe d'interaction des pays
"""
@app.route('/graph_pays')
def graph_pays():
    nodes_l = []
    c = []
    data={}
    result_node = session.run("match (n:Country) return n.country as node")
    for r in result_node :
        nodes_l.append({'id': r["node"]})
    data["nodes"] = nodes_l
    result = session.run("MATCH (n:Country)-[r:interaction]->(m:Country) RETURN n.country,r.cpt_int,m.country")
    for r in result :
        c.append({'source': r[0], 'target': r[2], 'value': r[1]})
    data["links"]=c
    return render_template("graph_countries.html", data=data)

"""
    :return: [GET] vue select.html à la première demande du formulaire
             [POST] vue submit.form si form validé sinon select.html
"""
@app.route('/form', methods=['GET', 'POST'])
def form():
    form = TestForm(request.form)
    f ={}
    if request.method == 'POST':
        name = form.name.data
        label_d = form.label_d.data
        label_f = form.label_f.data
        check = form.check.data
        if form.validate_on_submit():
            """
                formulaire validé donc on a vérifié si ce sont les bons champs pour envoyer une requête
                si depart ou arrivée est country et qu'un autre champ est sélectionné
                pas de requête possible
                si deux country, formulaire dynamique et on rend une vue spécifique à des pays
                si autres on rend une vue par rapport au champs name rempli
            """

            if ((label_d == "Country" or label_f == "Country") and label_d != label_f):                
                flash("Please, don't try to give a Country -> other or reverse situation, it will not work","danger")
                return redirect(url_for('form'))
            if (label_d == "Country" and label_d == label_f):
                return redirect(url_for('form_country'))
            f["label_d"] = label_d
            f["name"] = name
            f["label_f"] = label_f
            f["check"] = check
            return form_submit(f)
        else:
            flash("Not validate", "danger")
            return render_template('select.html', form=form)
    return render_template('select.html', form=form)

"""
    :param form: dictionnaire avec les champs du formulaire
    :return: vue submit avec data les données nécessaire pour créer un graph d3 si des données on été trouvée
"""
def form_submit(form):
    link_l = []
    node_l = []
    data = {}
    lis = []
    if (form["check"] == True):
        result = session.run("match (o:" + form["label_d"] + ") where o.name = \""
                         + form["name"]+ "\" match (o)-[r] - (c:"
                         + form["label_f"] + ") return o,r,c")
    else:
        result = session.run("match (o:" + form["label_d"] + ") where toLower(o.name) contains \""
                         + form["name"].lower() + "\" match (o)-[r] - (c:"
                         + form["label_f"] + ") return o,r,c")
    for r in result :
        labels_r0 = []
        labels_r2 = []
        for s in r[0].labels:
            labels_r0.append(s)
        for s in r[2].labels:
            labels_r2.append(s)
        labels_r0 = labels_r0[1]
        labels_r2 = labels_r2[1]
        print(labels_r0, labels_r2)
        link_l.append({'source' : r[0]["name"], 'target' : r[2]["name"], 'values' : r[1].type})
        if r[0]["name"] not in lis:
            lis.append(r[0]["name"])
            node_l.append({"id" : r[0]["name"], 'label': labels_r0 })
        if r[2]["name"] not in lis :
            lis.append(r[2]["name"])
            node_l.append({"id" : r[2]["name"], 'label' : labels_r2})
    data["nodes"] = node_l
    data["links"] = link_l
    if (len(node_l) == 0):
        messages = "What you wanted was not find in our database. Maybe it does not exist"
        flash(messages, 'warning')
        return redirect(url_for("form"))
    messages = "Yes, we found something for you"
    flash(messages, 'success')
    return render_template("submit.html", data=data)

@app.route('/form_country', methods = ['GET', 'POST'])
def form_country():
    form = CountryForm(request.form)
    f = {}
    if request.method == 'POST':
        countrya = form.countrya.data
        countryb = form.countryb.data
        value = form.value.data
        result = session.run("match (n:Country {country:\""+countrya+"\"}), (m:Country {country:\""+countryb+"\"}) match p = shortestPath((n)-[*.."+str(value)+"]-(m)) return nodes(p) , relationships(p)")
        data = {}
        list_l = []
        node_l = []
        links_l = []
        noe_l = []

        for r in result:
            list_l = r[1]
            node_l = r[0]

        for i in list_l:
            links_l.append(i)
        for j in node_l:
            noe_l.append(j)
        print(links_l, noe_l)
        list_l=[]
        node_l = []
        for i in noe_l:
            node_l.append({"id": i["country"]})
        for i in range(len(node_l) - 1):
            list_l.append({"source" : noe_l[i]["country"], "target" : noe_l[i+1]["country"]})
        j= 0
        for i in links_l:
            list_l[j]["value"] = i["cpt_int"]
            j += 1
            
        if (len(node_l) == 0):
            flash("Nothing found. Try to give a number to the deep higher or change countries selected","warning")
            return redirect(url_for("form_country"))
        data["nodes"]= node_l
        data["links"] = list_l
        flash("Yes, we found something for you. Take a look to shortest path","success")
        return render_template("sub_graph_countries.html", data = data)
    return render_template("form_country.html", form= form)

#session.close()
if __name__ == "__main__" :
    app.run(debug=True)
