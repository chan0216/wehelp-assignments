from flask import redirect,render_template,session,Blueprint
member_blueprint = Blueprint('member', __name__)
@member_blueprint.route("/member/")
def member():
    if 'name' not in session:
       return redirect("/")
    name=session["name"]
    return render_template("member.html",name=name)