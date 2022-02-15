from flask import redirect,session,Blueprint
signout_blueprint = Blueprint('signout', __name__)
@signout_blueprint.route("/signout",methods=["GET"])
def signout():
    session.pop('name', None)
    session.pop('username', None)
    return redirect("/")