#!/usr/bin/Python3

#Import the Flask framework
from flask import Flask, render_template, request

#Initialise the Flask app
app = Flask(__name__)

#create a route for the home page (root)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    celsius = request.form.get("celsius")
    f = (float(celsius) * 9/5) + 32
    return render_template("result.html", fahrenheit=f, celsius=celsius)

#Create a route for the /about page
app.run(host="0.0.0.0", port=8080, debug=True)