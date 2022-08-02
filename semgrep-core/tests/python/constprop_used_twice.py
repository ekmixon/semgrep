import flask
from flask import response as r

app = flask.Flask()

somevar = True

@app.route("/admin")
def admin():
    return r.set_cookie(
        "sessionid",
        "RANDOM-UUID",
        secure=somevar,
        httponly=somevar,
        samesite="Lax",
    )
