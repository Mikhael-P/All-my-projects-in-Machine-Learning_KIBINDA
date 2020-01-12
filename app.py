from flask import Flask, jsonify, render_template
from requests import get
import json

application_web = Flask(__name__)

@application_web.route("/group_1_database", methods=["GET"])
def fect_my_data():
    res = get("http://localhost:9200/group_1/_search?size=100")
    data=res.json()
    return jsonify(data)


@application_web.route("/accueil", methods = ["GET"])
def get_home_page():
    return render_template("accueil.html")


@application_web.route("/database_list", methods = ['GET'])
def list_databse():
    return render_template("list_database.html")


# Cette adresse affiche la base de données cinema
@application_web.route("/database_cinema", methods=["GET"])
def view_cinema_database():
    res = get("http://localhost:9200/cinema/films/_search")
    data = json.loads(res.text)
    database = data['hits']['hits']
    return render_template("database_cinema.html", database=database)

@application_web.route("/database_group_1", methods=["GET"])
def view_group_1_database():
    res = get("http://localhost:9200/group_1/_search")
    data = json.loads(res.text)
    database = data['hits']['hits']
    return render_template("database_group_1.html", database=database)

@application_web.route("/database_group_2", methods=["GET"])
def view_group_2_database():
    res = get("http://localhost:9200/group_2/_search")
    data = json.loads(res.text)
    database = data['hits']['hits']
    return render_template("database_group_2.html", database=database)


# Cette application affiche la base de données banque
@application_web.route("/database_bank", methods=["GET"])
def view_bank_database():
    res = get("http://localhost:9200/bank/tiger_bank/_search?size=500")
    data = json.loads(res.text)
    database = data['hits']['hits']
    return render_template("database_bank.html", database=database)

if __name__ == "__main__":
    application_web.run(debug=True)