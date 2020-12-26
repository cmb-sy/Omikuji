import random
from app.models import OmikuziTitle,User,OmikuziContent
from app import db, app
from flask import (
    render_template, request,session,
    abort, redirect, url_for,flash, Flask)
from hashlib import sha256
from app import key

omikuzi_list = ["大吉","中吉","小吉","吉","半吉","末吉","凶","大凶"]

@app.route("/",methods=["POST","GET"])
def first():
    if "user_name" in session:
        name = session["user_name"]
        return render_template("main.html",name=name)
    else:
        return redirect(url_for("top",status="logout"))

@app.route("/job")
def job():
    return render_template("job.html")

@app.route("/index",methods=["POST","GET"])
def index():
    if request.method == "POST":
        a = random.choice(omikuzi_list)
        if a == "大吉":
            mov = '/static/videos/daikichi_f.mp4'
        elif a == "吉":
            mov = '/static/videos/kiti_f.mp4'
        elif a == "中吉":
            mov = '/static/videos/tyu_f.mp4'
        elif a == "小吉":
            mov = '/static/videos/sho_f.mp4'
        elif a == "半吉":
            mov = '/static/videos/han_f.mp4'
        elif a == "末吉":
            mov = '/static/videos/sue_f.mp4'
        elif a == "凶":
            mov = '/static/videos/kyo_f.mp4'
        elif a == "大凶":
            mov = '/static/videos/daikyo_f.mp4'
        else:
            raise Exception('Error!')
        return render_template("result.html",a=mov)
    return render_template("index.html")

@app.route("/add",methods=["POST"])
def add():
    main_title = request.form["main_title"]
    # title = request.form["title"]
    # content = request.form["content"]
    omikuzititles = OmikuziTitle(main_title)
    # omikuzicontents = OmikuziContent(title,content)
    # omikuzititles.append(omikuzicontents)
    db.session.add(omikuzititles)
    db.session.commit()
    return self_omikuzi()

@app.route("/self_omikuzi",methods=["POST"])
def self_omikuzi():
        omikuzi_main_title = OmikuziTitle.query.all()
        return render_template("self.html", omikuzi_main_title=omikuzi_main_title)


@app.route("/top")
def top():
    status = request.args.get("status")
    return render_template("top.html",status=status)


@app.route("/login",methods=["post"])
def login():
    user_name = request.form["user_name"]
    user = User.query.filter_by(user_name=user_name).first()
    if user:
        password = request.form["password"]
        hashed_password = sha256((user_name + password + key.SALT).encode("utf-8")).hexdigest()
        if user.hashed_password == hashed_password:
            session["user_name"] = user_name
            return redirect(url_for("index"))
        else:
            return redirect(url_for("top",status="wrong_password"))
    else:
        return redirect(url_for("top",status="user_notfound"))


@app.route("/newcomer")
def newcomer():
    status = request.args.get("status")
    return render_template("newcomer.html",status=status)


@app.route("/registar",methods=["post"])
def registar():
    user_name = request.form["user_name"]
    user = User.query.filter_by(user_name=user_name).first()
    if user:
        return redirect(url_for("newcomer",status="exist_user"))
    else:
        password = request.form["password"]
        hashed_password = sha256((user_name + password + key.SALT).encode("utf-8")).hexdigest()
        user = User(user_name, hashed_password)
        db.session.add(user)
        db.session.commit()
        session["user_name"] = user_name
        return redirect(url_for("index"))

@app.route("/logout")
def logout():
    session.pop("user_name", None)
    return redirect(url_for("top",status="logout"))

if __name__ == "__main__":
    app.run(debug=True)