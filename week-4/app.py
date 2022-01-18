from flask import Flask, request , redirect, url_for,render_template,session

app = Flask(__name__)
app.secret_key="privacy123"
user={"username":"test","password":"test"}

@app.route("/signin",methods=["POST","GET"])
def signin():
    if(request.method == "POST"):
        username=request.form.get("username")
        password=request.form.get("password")
        if username==user["username"] and password == user["password"]:
            session["user"] = "username"
            return redirect("/member/")
        elif username=="" or password=="":
            return redirect(url_for("error",message="請輸入帳號、密碼"))
    return redirect(url_for("error",message="帳號、或密碼輸入錯誤"))

@app.route("/")
def index():
    if('user' in session):
        return redirect("/member/")
    return render_template("index.html")

@app.route("/member/")
def menber():
    if('user' not in session):
       return redirect("/")
    return render_template("member.html")

@app.route("/error/")
def error():
    message=request.args.get("message")
    return  render_template("error.html",string=message)

@app.route("/signout",methods=["GET"])
def signout():
    session.pop('user', None)
    return redirect("/")
    
app.run(port=3000)