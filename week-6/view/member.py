from flask import redirect,render_template,session,Blueprint
import public 
member_blueprint = Blueprint('member', __name__)
mydb=public.db1
@member_blueprint.route("/member/")
def member():
    if('name' not in session):
       mydb.close()
       return redirect("/")
    name=session["name"]
    return render_template("member.html",name=name)