from flask import request ,Blueprint,json,session

import public 
api_blueprint = Blueprint('api', __name__)
mydb=public.db
@api_blueprint.route("members",methods=["GET"])
def searchapi():
        username=request.args.get("username")
        mycursor = mydb.cursor(dictionary = True)
        mycursor.execute("SELECT name,username,id FROM member WHERE username=%s", (username,))
        member_value= mycursor.fetchone()
        return {"data":member_value}

@api_blueprint.route("member",methods=["POST"])
def changeapi():
        if 'name' in session :
                data = json.loads(request.data)
                newname=data["name"]
                username=session["username"]
                mycursor = mydb.cursor()
                sql = "UPDATE member SET name = %s WHERE username = %s"
                val = (newname,username)
                mycursor.execute(sql, val)
                session.pop('name', None) 
                session["name"]=newname
                mydb.commit()
                mycursor.close()
                return {"ok":"true"}
                
        else:
                return {"error":"true"}