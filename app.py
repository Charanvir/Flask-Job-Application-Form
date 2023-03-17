from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()
# Create an app instance
app = Flask(__name__)
# This will guard the appliction from hackers, cookies, and hijacking functionality
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
# Specify which database we are using
app.config[
    "SQLALCHEMY_DATABASE_URI"] = f"mysql://{os.getenv('USERNAME')}:{os.getenv('DB_PASSWORD')}@localhost/{os.getenv('DATABASE')}"
db = SQLAlchemy(app)


class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    date = db.Column(db.Date)
    occupation = db.Column(db.String(80))


# Requests (HTTP requests)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        date = request.form["date"]
        occupation = request.form["occupation"]

        form = Form(first_name=first_name, last_name=last_name, email=email, date=date, occupation=occupation)

        db.session.add(form)
        db.session.commit()
        flash("Your form was submitted successfully!")

    return render_template("index.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        # Run the flask app
        app.run(debug=True, port=5001)
