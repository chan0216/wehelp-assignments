from flask import request , redirect, url_for,Blueprint
signup_blueprint = Blueprint('signup', __name__)
@signup_blueprint.route("/signup",methods=["POST","GET"])
def signup():
    from app import mydb
    if request.method == "POST":
        mycursor = mydb.cursor()
        name=request.form["name"]
        username=request.form["username"]
        password=request.form["password"]
        mycursor.execute("SELECT username FROM member WHERE username=%s", (username,))
        checkUsername = mycursor.fetchone()
        if checkUsername is not None:
            return redirect(url_for("error.error",message="帳號已經被註冊"))
        elif name=="" or username=="" or password=="":
            return redirect(url_for("error.error",message="請輸入完整"))
        else:
            mycursor.execute("INSERT INTO member (name, username, password) VALUES (%s, %s, %s)",
            (name,username,password))
            mydb.commit()
            mycursor.close()
            return redirect("/")