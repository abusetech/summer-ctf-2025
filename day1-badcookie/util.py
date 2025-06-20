import flask_jwt_extended
import jwt

def getJWTValue(tok, key):
    if not tok:
        return None
    decoded = jwt.decode(tok, options={"verify_signature": False})
    print(decoded)
    return decoded["sub"][key]