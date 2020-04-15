from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET"])
def register():
    name = request.form.get("name")
    password = request.form.get("password")
    return render_template("register.html", name=name, password=password)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

