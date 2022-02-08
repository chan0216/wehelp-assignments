from decouple import config
import mysql.connector
from flask import Flask,redirect,render_template,session
from view.error import error_blueprint
from view.signin import signin_blueprint
from view.signup import signup_blueprint
from view.signout import signout_blueprint
from view.member import member_blueprint
app = Flask(__name__,template_folder="templates")
app.register_blueprint(error_blueprint)
app.register_blueprint(signin_blueprint)
app.register_blueprint(signup_blueprint)
app.register_blueprint(signout_blueprint)
app.register_blueprint(member_blueprint)
app.secret_key=config("secret_key")

mydb = mysql.connector.connect(
  host=config('host',default=''),
  database=config('database',default=''),
  user=config('user',default=''),
  password=config('password',default='')
)

@app.route("/")
def index():
    if('name' in session):
        return redirect("/member/")
    return render_template("index.html")
    
if __name__ == '__main__':
    app.debug = True
    app.run(port=3000)