from flask import Flask, render_template

# Create an app instance
app = Flask(__name__)

# Requests (HTTP requests)
@app.route("/")
def index():
    return render_template("index.html")


# Run the flask app
app.run(debug=True, port=5001)
