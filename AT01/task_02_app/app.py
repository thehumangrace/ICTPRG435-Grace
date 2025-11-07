#!/usr/bin/env python3

#SLE-ALE Calculator
#Name: Grace Garrett
#Date:16/10/2025
#Date Last Modified: 04/11/2025

from flask import Flask, render_template, request

app = Flask(__name__)

#This will define the class of the risk calculator
class RiskCalculator:
    def __init__(self, title):
        self.title = title
        self.asset_value = ""
        self.exposure_value = ""
        self.aro = ""
        self.sle = ""
        self.ale = ""
        self.error = ""

    def calculate_risk(self):
        try:
            #This will convert input values into floats
            av = float(self.asset_value)
            ev = float(self.exposure_value)
            aro_val = float(self.aro)
    
            # This will check for negative values
            if av < 0 or ev < 0 or aro_val < 0:
                self.sle = ""
                self.ale = ""
                self.error = "Bummer! No negative numbers allowed. Try again, pal!"
                return
    
            # This will check if exposure value exceeds 100%
            if ev > 100:
                self.sle = ""
                self.ale = ""
                self.error = "Bummer! Exposure value can't be more than 100%. Try again, pal!"
                return
    
            #This will calculate the Single Loss Expectancy (SLE)
            self.sle = av * (ev / 100)
    
            #This will calculate the Annualised Loss Expectancy: ALE
            self.ale = self.sle * aro_val
    
            # This will format to 2 decimal places
            self.sle = f"{self.sle:.2f}"
            self.ale = f"{self.ale:.2f}"
            #This will clear any previously written errors
            self.error = ""  
    
        #The SLE and ALE resets if the input is incorrect
        except (ValueError, TypeError):
            self.sle = ""
            self.ale = ""
            self.error = "Bummer! Those digits don't compute. Try again, pal!"

# This defines the route for the home page and gets input
@app.route("/", methods=["GET", "POST"])
def render_root():
    if request.method == "GET":
        return render_template("template.html", data=calculator)
    elif request.method == "POST":
        calculator.asset_value = request.form.get("asset_value")
        calculator.exposure_value = request.form.get("exposure_value")
        calculator.aro = request.form.get("aro")

    #This calculates the input
        calculator.calculate_risk()
        return render_template("template.html", data=calculator)
    else:
        return "Invalid request method!"

# This defines the route for clearing the calculator
@app.route("/clear")
def clear_calculator():
    calculator.asset_value = ""
    calculator.exposure_value = ""
    calculator.aro = ""
    calculator.sle = ""
    calculator.ale = ""
    calculator.error = ""
    return render_template("template.html", data=calculator)


calculator = RiskCalculator("SLE-ALE Calculator")

#This makes Flask run
app.run(host="0.0.0.0", port=8080, debug=True)