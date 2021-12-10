from flask import Flask , request
from flask.wrappers import Response
from controllers.user_controller import UserController
import json

app = Flask("__name__")

# 測試用 API
@app.route("/")
def main():
    return "Hello World"

@app.route("/user",methods=["POST"])
def register():
    return UserController.register(request)

@app.route("/user",methods=["GET"])
def get_user():
    return UserController.get_user(request)

@app.route("/user", methods=["DELETE"])
def delete_user():
    return UserController.unregister(request)

if __name__ == "__main__":
    app.run()