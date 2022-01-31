from flask import Flask, request, jsonify

app = Flask(__name__)

FAKE_DATABASE = []
count = 0

# CREATE
@app.route("/register", methods=["POST"])
def post():
  u = request.json["username"]
  f = request.json["fname"]
  l = request.json["lname"]
  e = request.json["email"]
  p = request.json["password"]
  global count
  count+=1
  user_object = {
    "id": count,
    "username": u,
    "fname": f,
    "lname": l,
    "email": e,
    "password": p
  }
  FAKE_DATABASE.append(user_object)
  return jsonify(user_object)

# READ
@app.route("/users", methods=["GET"])
def get_users():
  return jsonify(FAKE_DATABASE)

# UPDATE
@app.route("/user/<int:id>", methods=["PATCH"])
def patch_user(id):
  for u in FAKE_DATABASE:
    if u["id"] == id:
      u["username"] = request.json["username"]
    return jsonify(u) 

# DELETE
@app.route("/user/<int:id>", methods=["DELETE"])
def delete_user(id):
  for u in FAKE_DATABASE:
    if u["id"] == id:
      FAKE_DATABASE.remove(u)
  
  return f"user with ID {id} deleted"


if __name__ == '__main__':
  app.run(
    debug=True, 
    port=3000, 
    host="0.0.0.0"
  )


