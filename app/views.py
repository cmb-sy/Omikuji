import random
from app.models import OmikuziTitle
from app import db, app
from flask import (
    render_template, request,
    abort, redirect, url_for,flash, Flask)

omikuzi_list = ["大吉","中吉","小吉","吉","半吉","末吉","凶","大凶"]

@app.route("/",methods=["POST","GET"])
def main():
    return render_template("main.html")

@app.route("/index",methods=["POST","GET"])
def index():
    if request.method == "POST":
        a = random.choice(omikuzi_list)
        return render_template("result.html",a=a)
    return render_template("index.html")

@app.route("/add",methods=["POST","GET"])
def post():
    main_title = request.form["title"]
    omikuzititle = OmikuziTitle()
    omikuzititle.main_title = main_title
    db.session.add(omikuzititle)
    db.session.commit()
    return redirect(url_for('self_omikuzi'))

@app.route("/self_omikuzi",methods=["POST","GET"])
def self_omikuzi():
    if request.method == "GET":
        #POSTならエラー
        omikuzititle = OmikuziTitle()
        omikuzi_main_title = omikuzititle.main_title
        return render_template("self.html", omikuzi_title=omikuzi_main_title)
    return render_template("self.html")

if __name__ == "__main__":
    app.run(debug=True)