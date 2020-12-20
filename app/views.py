import random
from flask import Flask
from flask import request, render_template
# from app import OmikuziContent
# from app import db_session
# coding: utf-8
app = Flask(__name__)
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
    title = request.form["title"]
    body = request.form["body"]
    content = OmikuziContent(title,body)
    db_session.add(content)
    db_session.commit()
    return self_omikuzi()

@app.route("/self_omikuzi",methods=["POST","GET"])
def self_omikuzi():
    omikuzi = OmikuziContent.query.all()
    if request.method == "POST":
        b = random.choice(omikuzi)
        return render_template("self-result.html", b=b)
    return 'bad request!', 400

if __name__ == "__main__":
    app.run(debug=True)