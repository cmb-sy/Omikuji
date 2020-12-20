from flask import Flask,render_template
import random
from flask import Flask, request
from random import randint

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

if __name__ == "__main__":
    app.run(debug=True)