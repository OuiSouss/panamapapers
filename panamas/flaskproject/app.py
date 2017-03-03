from flask import Flask, render_template, json, url_for, request
from neo4j.v1 import GraphDatabase, basic_auth

app = Flask(__name__)

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

def temp():
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

@app.route("/neo")
def connect_neo4j():
    driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "neo"))
    session = driver.session()
    result = session.run("match (n:Intermediary) return count(n) as nombre")
    session.close()
    res = 0
    for rec in result:
        res = rec["nombre"]
    return str(res)

def count_intermediaries(driver):
    session = driver.session()
    result = session.run("match (n:Intermediary) return count(n) as nombre")
    session.close()
    res = 0
    for rec in result:
        res = rec["nombre"]
    return res

def count_addresses(driver):
    session = driver.session()
    result = session.run("match (n:Address) return count(n) as nombre")
    session.close()
    res = 0
    for rec in result:
        res = rec["nombre"]
    return res

def count_entities(driver):
    session = driver.session()
    result = session.run("match (n:Entity) return count(n) as nombre")
    session.close()
    res = 0
    for rec in result:
        res = rec["nombre"]
    return res

def count_officers(driver):
    session = driver.session()
    result = session.run("match (n:Officer) return count(n) as nombre")
    session.close()
    res = 0
    for rec in result:
        res = rec["nombre"]
    return res

@app.route("/neo_graph")
def neo_graph():
    driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "neo"))
    nb_intermediaries = count_intermediaries(driver)
    nb_addresses = count_addresses(driver)
    nb_entities = count_entities(driver)
    nb_officers = count_officers(driver)
    data ={
        "Addresses": nb_addresses,
        "Entities": nb_entities,
        "Intermediaries": nb_intermediaries,
        "Officers": nb_officers}
    return render_template("panama-visu.html", data = data)

@app.route("/histo_countries")
def get_countries_data():
    driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "neo"))
    session = driver.session()

    countries_array = ['South Africa', 'Liechtenstein', 'Monaco', 'Belgium', 'Lebanon', 'Switzerland', 'Malaysia', 'Spain', 'United Kingdom', 'Jersey', 'France', 'Luxembourg', 'Taiwan', 'Estonia', 'Mexico', 'Argentina', 'Guernsey', 'United States', 'Venezuela', 'Hong Kong', 'Panama', 'Saudi Arabia', 'Germany', 'Kuwait', 'Poland', 'Brazil', 'Turkey', 'Egypt', 'Canada', 'Portugal', 'Russia', 'Isle of Man', 'Malta', 'Hungary', 'Israel', 'Greece', 'Philippines', 'Italy', 'China', 'Gibraltar', 'Bahamas', 'Honduras', 'Australia', 'Austria', 'Sweden', 'Slovenia', 'Uruguay', 'Thailand', 'Ecuador', 'Colombia', 'United Arab Emirates', 'Peru', 'Czech Republic']

    data ={}
    for country1 in countries_array:
        s = 0
        i = countries_array.index(country1)
        for country2 in countries_array:
            result = session.run("MATCH (n:Country)-[r]->(m:Country) WHERE (n.country = '" + country1 + "' and m.country = '" + country2 + "') RETURN r.cpt_interaction as inter")
            for r in result:
                s += r["inter"]
        print i
        if country1 == 'United Kingdom':
            country1 = 'UK'
        data[country1] = s
    session.close()
    return render_template("countries-visu.html", data = data)


if __name__ == "__main__" :
    app.run()
