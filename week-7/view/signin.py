from flask import request , redirect, url_for,session,Blueprint
import public 
signin_blueprint = Blueprint('signin', __name__)
mydb=public.db
@signin_blueprint.route("/signin",methods=["POST","GET"])
def signin():
    if request.method == "POST":
        mycursor = mydb.cursor(dictionary = True)
        username=request.form["username"]
        password=request.form["password"]
        mycursor.execute("SELECT name,username,password FROM member WHERE username=%s and password=%s", (username,password))
        member_value= mycursor.fetchone()
        if member_value is not None:
            session["name"]=member_value["name"]
            session["username"]=member_value["username"]
            return redirect(url_for("member.member"))
        return redirect(url_for("error.error",message="帳號或密碼輸入錯誤"))