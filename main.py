from flask import Flask, redirect, render_template, url_for, request
import json, time
from datetime import datetime

app = Flask(__name__)

class Data:
    def __init__(self):
        self.data = self.load()

    def load(self) -> dict:  # type: ignore
        try:
            with open("data.json", "r") as ff:
                return json.load(ff)
        except:
            return {}

    def save(self):
        with open("data.json", "w") as ff:
            json.dump(self.data, ff, indent=4)


dataobj = Data()

@app.route("/", methods=["GET", "POST"])
def visitor_welcome():
    return render_template("visitor_welcome.html")


@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():
    cor = ""
    if request.method == "POST":
        user = {
            "sname": request.form.get("sname"),
            "mname": request.form.get("mname"),
            "lname": request.form.get("lname"),
            "usrn": request.form.get("usrn"),
            "pswd": request.form.get("pswd"),
            "cpswd": request.form.get("cpswd"),
        }
        dataobj.data["user"] = user
        dataobj.save()
    return render_template("sign_in.html", cor=cor)


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    return "wassup everyone 😄"

if __name__ == "__main__":
    app.run(dedug=True)