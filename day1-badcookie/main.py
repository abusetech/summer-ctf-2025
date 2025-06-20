from flask import Flask, request, make_response
from flask_jwt_extended import create_access_token, JWTManager
import random
import util

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = ''.join([chr(random.randint(65,125)) for i in range(60)])

GUEST_IDENTITY = {
    "username" : "guest",
    "isAdmin" : False
}

JWTManager(app)

@app.route("/")
def home():
    token = create_access_token(GUEST_IDENTITY)
    resp = make_response("Bet you can't access /admin!")
    resp.set_cookie('token',token)
    return resp

@app.route("/admin")
def admin():
    token = request.cookies.get('token')
    if util.getJWTValue(token, "isAdmin"):
        return 'You got the flag!'
    else:
        return 'Unauthorized',401

if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=5000, debug=True)
