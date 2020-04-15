from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/register", methods=["GET"])
def register():
    name = request.form.get("name")
    password = request.form.get("password")
    return render_template("register.html", name=name, password=password)

    