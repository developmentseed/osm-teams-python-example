from flask import Flask, url_for, session, render_template, redirect
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = "!secret"
app.config.from_object("config")

CONF_URL = "https://auth.mapping.team/hyauth/.well-known/openid-configuration"
oauth = OAuth(app)
oauth.register(
    name="teams",
    server_metadata_url=CONF_URL,
    client_kwargs={"scope": "openid offline"},
)


@app.route("/")
def index():
    user = session.get("user")
    access_token = session.get("access_token")
    uid = session.get("uid")
    picture = session.get("picture")
    return render_template(
        "index.html", user=user, access_token=access_token, uid=uid, picture=picture
    )


@app.route("/login")
def login():
    redirect_uri = url_for("auth", _external=True)
    return oauth.teams.authorize_redirect(redirect_uri)


@app.route("/auth")
def auth():
    token = oauth.teams.authorize_access_token()
    session["uid"] = token["userinfo"]["sub"]
    session["user"] = token["userinfo"]["preferred_username"]
    session["picture"] = token["userinfo"]["picture"]
    session["access_token"] = token["access_token"]
    return redirect("/")


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")
