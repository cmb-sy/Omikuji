import random
from app.models import OmikuziTitle,User,OmikuziContent
from app import db, app
from flask import (
    render_template, request,session,
    abort, redirect, url_for,flash, Flask)
from hashlib import sha256
from app import key

omikuzi_list = ["大吉","中吉","小吉","吉","半吉","末吉","凶","大凶"]

@app.route("/plus",methods=["POST"])
def plus():
    m = User.query.filter_by().first()
    m.balance += 500
    db.session.add(m)
    db.session.commit()
    return render_template("main.html",m=m)

@app.route("/job")
def job():
    return render_template("job.html")

@app.route("/job/thxmam")
def thxmam():
    #500円追加する処理
    return render_template("thxmam.html")

@app.route("/job/NYsgreet")
def NYsgreet():
    #3000円追加する処理
    return render_template("NYsgreet.html")

@app.route("/job/oosoji")
def oosoji():
    sukima_okane = [500, 1000, 2000, 5000]
    okane = random.choice(sukima_okane)
    #okaneの中身を追加する処理
    return render_template("oosoji.html", okane=okane)

@app.route("/job/nengajo")
def nengajo():
    tousen_okane = [1000, 2000, 3000, 5000]
    tousen = random.choice(tousen_okane)
    #tousenの中身を追加する処理
    return render_template("nengajo.html", tousen=tousen)

@app.route("/job/hatsuhinode")
def hatushinode():
    #1000円追加する処理
    return render_template("hatsuhinode.html")

@app.route("/job/hatsuyume")
def hatsuyume():
    kingakus = [0, 2000]
    kingaku = random.choice(kingakus)
    if kingaku == 0:
        kekka = "悪い夢だった。お金は増えない。"
    else:
        #2000円追加する処理
        kekka = "良い夢だった。2000円増えた。"
    return render_template("hatsuyume.html", kekka=kekka)

@app.route("/",methods=["POST","GET"])
def first():
    if "user_name" in session:
        return redirect(url_for("main"))
    else:
        return redirect(url_for("top",status="logout"))

@app.route("/index",methods=["POST","GET"])
def index():
    if request.method == "POST":
        # a = random.choice(omikuzi_list)
        # if a == "大吉":
        #     mov = '/static/videos/daikichi_f.mp4'
        # elif a == "吉":
        #     mov = '/static/videos/kiti_f.mp4'
        # elif a == "中吉":
        #     mov = '/static/videos/tyu_f.mp4'
        # elif a == "小吉":89
        #     mov = '/static/videos/sho_f.mp4'
        # elif a == "半吉":
        #     mov = '/static/videos/han_f.mp4'
        # elif a == "末吉":
        #     mov = '/static/videos/sue_f.mp4'
        # elif a == "凶":
        #     mov = '/static/videos/kyo_f.mp4'
        # elif a == "大凶":
        #     mov = '/static/videos/daikyo_f.mp4'
        # else:
        #     raise Exception('Error!')
        pay = int(request.form['money'])
        if pay <= 100:
            mov =  '/static/videos/daikyo_f.mp4'
        elif 100 < pay and pay <=200:
            mov = '/static/videos/kyo_f.mp4'
        elif 200 < pay and pay <=400:
            mov = '/static/videos/sue_f.mp4'
        elif 400 < pay and pay <=800:
            mov = '/static/videos/han_f.mp4'
        elif 800 < pay and pay <=1600:
            mov = '/static/videos/sho_f.mp4'
        elif 1600 < pay and pay <= 3200:
            mov = '/static/videos/tyu_f.mp4'
        else:
            mov = '/static/videos/daikichi_f.mp4'
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






@app.route("/main")
def main():
    m = User.query.filter_by().first()
    return render_template("main.html",m=m)



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
            return redirect(url_for("main"))
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
        balance = 0
        hashed_password = sha256((user_name + password + key.SALT).encode("utf-8")).hexdigest()
        user = User(user_name, hashed_password, balance)
        db.session.add(user)
        db.session.commit()
        session["user_name"] = user_name
        return redirect(url_for("main"))

@app.route("/logout")
def logout():
    session.pop("user_name", None)
    return redirect(url_for("top",status="logout"))

if __name__ == "__main__":
    app.run(debug=True)