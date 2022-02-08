from flask import request , redirect, url_for,session,Blueprint
signin_blueprint = Blueprint('signin', __name__)
@signin_blueprint.route("/signin",methods=["POST","GET"])
def signin():
    if request.method == "POST":
        from app import mydb
        mycursor = mydb.cursor()
        username=request.form["username"]
        password=request.form["password"]
        mycursor = mydb.cursor()
        mycursor.execute("SELECT username,password FROM member WHERE username=%s and password=%s", (username,password))
        member_value= mycursor.fetchone()
        if member_value is not None:
            mycursor.execute("SELECT name FROM member WHERE username=%s", (username,))
            name_value=mycursor.fetchone()
            session["name"]=name_value[0]
            return redirect(url_for("member.member"))
        return redirect(url_for("error.error",message="帳號或密碼輸入錯誤"))