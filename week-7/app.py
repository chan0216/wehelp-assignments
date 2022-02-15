import public 
from decouple import config
from flask import Flask,redirect,render_template,session
from view.error import error_blueprint
from view.signin import signin_blueprint
from view.signup import signup_blueprint
from view.signout import signout_blueprint
from view.member import member_blueprint
from accont.api import api_blueprint
app = Flask(__name__,template_folder="templates")
app.register_blueprint(error_blueprint)
app.register_blueprint(signin_blueprint)
app.register_blueprint(signup_blueprint)
app.register_blueprint(signout_blueprint)
app.register_blueprint(member_blueprint)
app.register_blueprint(api_blueprint,url_prefix='/api')
app.secret_key=config("secret_key")
app.config['JSON_AS_ASCII'] = False
mydb=public.db

@app.route("/")
def index():
    if 'name' in session:
        return redirect("/member/")
    return render_template("index.html")
    
if __name__ == '__main__':
    app.debug = True
    app.run(port=3000)