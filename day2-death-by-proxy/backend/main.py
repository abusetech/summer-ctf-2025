from flask import Flask, request, make_response
from flask.json import jsonify
import random

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = ''.join([chr(random.randint(65,125)) for i in range(60)])

ANIMAL_DICT = {
    "Aardvark" : "Contains two \"A\"s!",
    "Badger" : "Probably doesn't care about these facts",
    "Coyote" : "Don't sell them dynamite",
    "Camel" : "Often found in deserts. Found significantly less frequently in desserts",
    "Cricket" : "Chirrrrrrrrrrrp",
    "Dingo" : "A wild dog",
    "Elephant" : "They're pretty big",
    "Ferret" : "Good luck holding onto one",
    "Gecko" : "Amphibious",
}

@app.route("/")
def home():
    resp = make_response("Hey! You shouldn't be connecting to this service except via the proxy (it's not part of the challenge)")
    return resp

@app.route("/secretapi")
def secret():
    return jsonify({"secret":'Octopi have three hearts (You got the flag!)'})

@app.route("/listanimals")
def listAnimals():
    return jsonify(list(ANIMAL_DICT.keys()))

@app.route("/animals/<string:animal>")
def getAnimal(animal=''):
    if animal in ANIMAL_DICT:
        ret = {animal : ANIMAL_DICT[animal]}
        return jsonify(ret)
    else:
        return jsonify({"error" : "animal not found"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=15000, debug=True)
