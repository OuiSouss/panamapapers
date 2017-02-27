from flask import Flask, render_template, json, url_for, request
from neo4j.v1 import GraphDatabase, basic_auth

app = Flask(__name__)

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

@app.route("/neo_graph")
def neo_graph():

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

session.close()
if __name__ == "__main__" :
    app.run()
