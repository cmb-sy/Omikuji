import random
from flask import Flask
from flask import request, render_template
from app.models import OmikuziContent
from app import db, app
from flask import (
    render_template, request,
    abort, redirect, url_for,
    flash
)

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

@app.route("/add",methods=["POST"])
def post():
    main_title = request.form["title"]
    omikuzicontent = OmikuziContent()
    omikuzicontent.main_title = main_title
    db.session.add(omikuzicontent)
    db.session.commit()
    return redirect(url_for('self_omikuzi'))

@app.route("/self_omikuzi",methods=["POST","GET"])
def self_omikuzi():
    omikuzicontent = OmikuziContent()
    omikuzi_main_title = omikuzicontent.main_title
    if request.method == "POST":
        return render_template("self-result.html", omikuzi_title=omikuzi_main_title)
    return 'bad request!', 400

if __name__ == "__main__":
    app.run(debug=True)