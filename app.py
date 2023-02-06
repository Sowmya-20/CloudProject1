import os

from flask import Flask,render_template,flash, redirect,url_for,session,logging,request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cc_db.db'
db = SQLAlchemy(app)
UPLOAD_FOLDER = '/Files/Original/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


class user(db.Model):
    username = db.Column(db.String(80), primary_key=True)
    email = db.Column(db.String(120))
    password = db.Column(db.String(80))
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login",methods=["GET", "POST"])
def login():
    if request.method == "POST":
        uname = request.form["uname"]
        passw = request.form["passw"]

        login = user.query.filter_by(username=uname, password=passw).first()

        if login is not None:
            return redirect(url_for("info", uname=uname))
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        uname = request.form['uname']
        mail = request.form['mail']
        passw = request.form['passw']
        fname = request.form['fname']
        lname = request.form['lname']

        register = user(username=uname, email=mail, password=passw, firstname=fname, lastname=lname)
        db.session.add(register)
        db.session.commit()

        return redirect(url_for("login"))
    return render_template("register.html")

@app.route('/<uname>/info')
def info(uname):
    details = user.query.filter_by(username=uname).first()
    return render_template("info.html", data=details)

@app.route('/<uname>/uploader', methods = ['GET', 'POST'])
def upload_file(uname):
   if request.method == 'POST':
      f = request.files['file']
      print(os.path)
      print(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
      return redirect(url_for("info"))

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
