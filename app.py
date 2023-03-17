from flask import Flask, render_template, request

# Create an app instance
app = Flask(__name__)


# Requests (HTTP requests)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        date = request.form["date"]
        occupation = request.form["occupation"]
        print(first_name)
        print(last_name)
        print(email)
        print(date)
        print(occupation)

    return render_template("index.html")


# Run the flask app
app.run(debug=True, port=5001)
