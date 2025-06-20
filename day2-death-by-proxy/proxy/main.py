from flask import Flask, request, make_response, render_template
from flask.json import jsonify
import random
import requests

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = ''.join([chr(random.randint(65,125)) for i in range(60)])

RM_HOST = "day2-backend"

@app.route("/")
def home():
    r = requests.get(f"http://{RM_HOST}:15000/listanimals")
    return render_template("home.html", animals=r.json())


@app.route("/getanimal")
def listAnimals():
    animal = request.args.get("animal", '')
    r = requests.get(f"http://{RM_HOST}:15000/animals/{animal}")
    return jsonify(r.json())

if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=5000, debug=True)
