# -*- coding: utf-8 -*-
# Welcome to our L3-projet-techno application about panama papers . This will give you a
# guided tour around creating our application using Flask-Bootstrap and other package.
# From Amélie Risi, Chloe Pathé, Lucas Vivas
#
# To run this application yourself, please activate virtualennv first in flaskproject folder:
#   $ . venv/bin/activate
# Then, install its requirements first:
#
#   $ pip install -r sample_app/requirements.txt
#
# Then, you can actually run the application.
#
#   $ pyton app.py
#
# Afterwards, point your browser to http://localhost:5000, then check out the
# source.
from flask import Flask, render_template, json, url_for, request, flash, Blueprint, redirect, jsonify
from neo4j.v1 import GraphDatabase, basic_auth
from flask_bootstrap import Bootstrap
from flask_appconfig import AppConfig
from flask_debug import Debug


frontend = Blueprint("app", __name__)
def create_app(configfile=None):
    app = Flask(__name__)
    AppConfig(app)
    Bootstrap(app)
    Debug(app)
    app.register_blueprint(frontend)
    app.config["BOOTSTRAP_SERVE_LOCAL"] = True
    return app

app = create_app()
global driver,session

driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "neo"))
session = driver.session()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello/<name>")
def hello(name):
    return "hello " + name

@app.route("/hello2")
def hello2():
    name = request.args.get('name', 's')
    return "hello " + name

@app.route ("/histo")
def histo():
    return app.send_static_file("panama-visu.html")

@app.route("/data.json")
def data():
    return app.send_static_file("data.json")

@app.route("/histo_temp")

def histo_temp():
    f = open("static/data.json")
    data = json.load(f)
    return render_template("panama-visu.html", data=data)

@app.route("/data/count/<type>")
def data_count(type):
    f = open("static/data.json")
    data = json.load(f)
    if type in data :
        return "Nombre de noeuds de " + type + " = " + str(data[type])
    else:
        return "Type not specify or type doesn't exist in data"

@app.route("/count_test_neo")
def count_test_neo():
    result = session.run("match (n:Intermediary) return count(n) as nombre")
    res = 0
    for rec in result:
        res = rec["nombre"]
    return str(res)


def count_type(driver, n_type):
    result = session.run("match (n:%s) return count(n) as nombre"%n_type)
    res = 0
    for rec in result:
        res = rec["nombre"]
    return res

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

@app.route("/histo__count_countries")
def histo_count_countries():
    countries_array = ['South Africa', 'Liechtenstein', 'Monaco', 'Belgium', 'Lebanon', 'Switzerland', 'Malaysia', 'Spain', 'United Kingdom', 'Jersey', 'France', 'Luxembourg', 'Taiwan', 'Estonia', 'Mexico', 'Argentina', 'Guernsey', 'United States', 'Venezuela', 'Hong Kong', 'Panama', 'Saudi Arabia', 'Germany', 'Kuwait', 'Poland', 'Brazil', 'Turkey', 'Egypt', 'Canada', 'Portugal', 'Russia', 'Isle of Man', 'Malta', 'Hungary', 'Israel', 'Greece', 'Philippines', 'Italy', 'China', 'Gibraltar', 'Bahamas', 'Honduras', 'Australia', 'Austria', 'Sweden', 'Slovenia', 'Uruguay', 'Thailand', 'Ecuador', 'Colombia', 'United Arab Emirates', 'Peru', 'Czech Republic']

    data ={}
    for country1 in countries_array:
        s = 0
        i = countries_array.index(country1)
        for country2 in countries_array:
            result = session.run("MATCH (n:Country3)-[r]->(m:Country3) WHERE (n.country = '" + country1 + "' and m.country = '" + country2 + "') RETURN r.cpt_int as inter")
            for r in result:
                s += r["inter"]
        print i
        if country1 == 'United Kingdom':
            country1 = 'UK'
        data[country1] = s
    return render_template("countries-visu.html", data = data)

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

def kparmisn(k,n):
    return fact(n)/(fact(k)*fact(n-k))

@app.route("/graph_countries")
def graph_countries():
    countries_array = ['South Africa', 'Liechtenstein', 'Monaco', 'Belgium', 'Lebanon', 'Switzerland', 'Malaysia', 'Spain', 'United Kingdom', 'Jersey', 'France', 'Luxembourg', 'Taiwan', 'Estonia', 'Mexico', 'Argentina', 'Guernsey', 'United States', 'Venezuela', 'Hong Kong', 'Panama', 'Saudi Arabia', 'Germany', 'Kuwait', 'Poland', 'Brazil', 'Turkey', 'Egypt', 'Canada', 'Portugal', 'Russia', 'Isle of Man', 'Malta', 'Hungary', 'Israel', 'Greece', 'Philippines', 'Italy', 'China', 'Gibraltar', 'Bahamas', 'Honduras', 'Australia', 'Austria', 'Sweden', 'Slovenia', 'Uruguay', 'Thailand', 'Ecuador', 'Colombia', 'United Arab Emirates', 'Peru', 'Czech Republic']

    number_of_countries = len(countries_array)
    print(number_of_countries)
    data = {}
    data['nodes'] = [{}] * number_of_countries
    data['links'] = [{}] * kparmisn(2,number_of_countries)

    x = 0

    for i,country1 in enumerate(countries_array):
        data['nodes'][i] = {'id': country1}
        for j in range(i+1,number_of_countries):
            s = 0
            country2 = countries_array[j]
            exist = False
            result = session.run("MATCH (n:Country3)-[r]->(m:Country3) WHERE (n.country = '" + country1 + "' and m.country = '" + country2 + "') or (n.country = '" + country2 + "' and m.country = '" + country1 + "') RETURN r.cpt_int as inter")
            for r in result:
                exist = True
                s += r["inter"]
            data['links'][x] = {'source': country1, 'target': country2, 'value': s}
            x += 1
        print(i)

    return render_template("graph_countries.html", data = data)

@app.route('/graph_pays')
def graph_pays():
    nodes_l = []
    c = []
    data={}
    result_node = session.run("match (n:Country3) return n.country as node")
    for r in result_node :
        nodes_l.append(r["node"])
    data["nodes"] = nodes_l
    result = session.run("MATCH (n:Country3)-[r:interaction]->(m:Country3) RETURN n.country,r.cpt_int,m.country")
    for r in result :
        c.append(r.values())
    data["links"]=c
    return jsonify(data)

session.close()
if __name__ == "__main__" :
    app.run(debug=True)
