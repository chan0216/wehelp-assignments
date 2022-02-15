from flask import request ,render_template,Blueprint
error_blueprint = Blueprint('error', __name__)
@error_blueprint.route("/error/")
def error():
    message=request.args.get("message")
    return  render_template("error.html",string=message)
