from flask import Flask,request,jsonify
import re
app=Flask(__name__)

def is_valid_email(email):
    pattern=r'^[A-Za-z0-9./%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern,email) is not None

@app.route("/register",methods=['POST'])
def register():
    data=request.get_json()
    name=data.get('name','')
    email=data.get('email','')
    
    if not name or not email:
        return jsonify({
            "success":False, "status_code":400,
            "message":"Validation Error",
            "errors":{
                "name":"Name is required" if not name else None,
                "email":"Email is required" if not email else None
            }
        }),400
        
    if not is_valid_email(email):
        return jsonify({
            "success":False,"status_code":400,
            "message":"Validation error",
            "errors":{"email":"Invalid email format"}
        }),400
        
    return jsonify({
        "success":True,"status_code":201,
        "message":f"User {name} has registered successfully",
        "data":{"name":name, "email":email}
    })

if __name__=='__main__':
    app.run(debug=True)