from flask import Flask, render_template, request

app = Flask(__name__, template_folder=r"C:\Users\Himaja\Documents\project1\project1\templates")

@app.route("/")
def home():    
    return render_template('index.html')

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    password = request.form.get("password")    
    return render_template("register.html", name=name, password=password)


if __name__ == '__main__': 
    app.run()
