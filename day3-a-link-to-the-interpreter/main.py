from flask import Flask, render_template, request, redirect, g
import sqlite3
import random
import re

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = ''.join([chr(random.randint(65,125)) for i in range(60)])

def init():
    with app.app_context():
        db=getDB()
        db.cursor().execute("CREATE TABLE IF NOT EXISTS urls(id INTEGER PRIMARY KEY, url TEXT);")
        db.cursor().execute("INSERT INTO urls VALUES(NULL, \"/\")")
        db.commit()

def getDB():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect("db.sqlite3")
    return db

def getURL():
    db=getDB()
    cur = db.cursor()
    res = cur.execute("SELECT url FROM urls WHERE id = 1;")
    return res.fetchone()[0]

def updateURL(url):
    db=getDB()
    cur = db.cursor()
    ctx = cur.execute("UPDATE urls SET url = ? WHERE id = 1;", [str(url)])
    db.commit()


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def home():
    return render_template("home.html", link_url=getURL())

@app.route("/setlink", methods = ["POST"])
def setlink():
    newURL = request.form["url"]
    print(f"newURL: {newURL}")
    if re.match("[a-zA-Z]+://",newURL):
        updateURL(newURL)
        return redirect("/")
    else:
        return "Invalid URL", 400

if __name__ == "__main__": 
    init()
    app.run(host="0.0.0.0", port=5000, debug=True)
