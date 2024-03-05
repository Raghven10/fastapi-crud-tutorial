# This file is responsible for the signing, encoding, decoding, and returning JWTs.

import time
import jwt

from decouple import config

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")

### function returning the generated JWTs
def token_response(token:str):
    return {
        "access_token": token,
    }

### function used for signing the JWT string
def signJWT(userID : str):
    payload = {
        "expiry": time.time() + 600,
        "userID": userID
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)

def decodeJWT(token:str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithm= JWT_ALGORITHM)
        return decode_token if decode_token['expiry'] >= time.time() else None
    except:
        return None