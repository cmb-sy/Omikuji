import random
from app.models import OmikuziTitle,User,OmikuziContent
from app import db, app
from flask import (
    render_template, request,session,
    abort, redirect, url_for,flash, Flask)
from hashlib import sha256
from app import key

pre_money = 0

@app.route("/job")
def job():
    return render_template("job.html")

@app.route("/job/thxmam",methods=["POST","GET"])
def thxmam():
    #500円追加する処理
    if request.method == "POST":
        m = User.query.filter().order_by(User.id.desc()).first()
        m.balance += 500
        db.session.add(m)
        db.session.commit()
        return render_template("main.html",m=m)
    else:
        return render_template("thxmam.html")

@app.route("/job/NYsgreet",methods=["POST","GET"])
def NYsgreet():
    #3000円追加する処理
    if request.method == "POST":
        m = User.query.filter().order_by(User.id.desc()).first()
        m.balance += 3000
        db.session.add(m)
        db.session.commit()
        return render_template("main.html",m=m)
    return render_template("NYsgreet.html")

@app.route("/job/oosoji",methods=["POST","GET"])
def oosoji():
    sukima_okane = [500, 1000, 2000, 5000]
    okane = random.choice(sukima_okane)
    global pre_money
    #okaneの中身を追加する処理
    if request.method == "POST":
        m = User.query.filter().order_by(User.id.desc()).first()
        m.balance += pre_money
        db.session.add(m)
        db.session.commit()
        return render_template("main.html",m=m)
    pre_money = okane
    return render_template("oosoji.html", okane=okane)

@app.route("/job/nengajo",methods=["POST","GET"])
def nengajo():
    tousen_okane = [1000, 2000, 3000, 5000]
    tousen = random.choice(tousen_okane)
    #tousenの中身を追加する処理
    global pre_money
    #okaneの中身を追加する処理
    if request.method == "POST":
        m = User.query.filter().order_by(User.id.desc()).first()
        m.balance += pre_money
        db.session.add(m)
        db.session.commit()
        return render_template("main.html",m=m)
    pre_money = tousen
    return render_template("nengajo.html", tousen=tousen)

@app.route("/job/hatsuhinode",methods=["POST","GET"])
def hatushinode():
    #1000円追加する処理
    if request.method == "POST":
        m = User.query.filter().order_by(User.id.desc()).first()
        m.balance += 1000
        db.session.add(m)
        db.session.commit()
        return render_template("main.html",m=m)
    return render_template("hatsuhinode.html")

@app.route("/job/hatsuyume",methods=["POST","GET"])
def hatsuyume():
    kingakus = [0, 2000]
    kingaku = random.choice(kingakus)
    if kingaku == 0:
        kekka = "悪い夢だった。お金は増えない。"
    else:
        #2000円追加する処理
        if request.method == "POST":
            m = User.query.filter().order_by(User.id.desc()).first()
            m.balance += 2000
            db.session.add(m)
            db.session.commit()
            return render_template("main.html",m=m)
        kekka = "良い夢だった。2000円増えた。"
    return render_template("hatsuyume.html", kekka=kekka)

@app.route("/",methods=["POST","GET"])
def first():
    if "user_name" in session:
        m = User.query.filter_by(user_name="user_name").first()
        return render_template("main.html", m=m)
    else:
        return redirect(url_for("top",status="logout"))

@app.route("/index",methods=["POST","GET"])
def index():
    if request.method == "POST":
        try:
            pay = int(request.form['money'])
        except ValueError:
            content = "正しい金額を入力してください"
            return render_template("index.html", content=content)
        m = User.query.filter_by().first()
        m.balance -= pay
        if m.balance < 0:
            content = "お金が足りません"
            return render_template("index.html", content=content)
        else:
            db.session.add(m)
            db.session.commit()
            if pay <= 100:
                mov = '/static/videos/daikyo_f.mp4'
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
            elif 3200 < pay and pay <= 6400:
                mov = '/static/videos/kiti_f.mp4'
            else:
                mov = '/static/videos/dikichi_f.mp4'
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
            m = User.query.filter_by(user_name="user_name").first()
            return render_template("main.html", m=m)
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
        user = User(user_name, hashed_password, balance=0)
        user.balance = 0
        db.session.add(user)
        db.session.commit()
        session["user_name"] = user_name
        m = User.query.filter_by(user_name=user_name).first()
        return render_template("main.html", m=m)

@app.route("/logout")
def logout():
    session.pop("user_name", None)
    return redirect(url_for("top",status="logout"))

if __name__ == "__main__":
    app.run(debug=True)