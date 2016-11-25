from flask import Flask, render_template, json
from neo4j.v1 import GraphDatabase, basic_auth

app = Flask(__name__)

@app.route("/")
def index():
    return "Index Page"

@app.route("/hello/<name>")
def hello(name):
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
    return render_template("panama-visu.html", data = data)

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
    driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "7_juliDA"))
    session = driver.session()
    result = session.run("match (n:Intermediary) return count(n) as nombre")
    session.close()
    res = 0
    for rec in result:
        res = rec["nombre"]
    return str(res)

    
if __name__ == "__main__" :
    app.run()
