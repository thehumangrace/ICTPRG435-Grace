# SLE ALE Risk Calculator

A small Flask web app that calculates cyber risk exposure using the Single Loss Expectancy (SLE) and Annualised Loss Expectancy (ALE) formulas. Built as part of my Certificate IV in Cyber Security (ICTPRG435, Write scripts for software applications).

## What SLE and ALE actually mean

Risk analysts use these two formulas to put a dollar figure on the damage a cyber attack could cause:

- **Single Loss Expectancy (SLE)**: how much a single incident would cost. Calculated as Asset Value × Exposure Value.
- **Annualised Loss Expectancy (ALE)**: how much that risk is expected to cost per year. Calculated as SLE × Annualised Rate of Occurrence (ARO).

The app takes an asset value, an exposure percentage, and an ARO, then returns both figures.

## Features

- Calculates SLE and ALE from user input
- Validates input (rejects negative numbers and exposure values over 100%)
- Clear function to reset the form
- Error messages for invalid or non numeric input
- Simple Flask front end, no database required

## Tech stack

Python, Flask

## How it works

The app is built around a `RiskCalculator` class that holds the input values and does the math:

```python
self.sle = av * (ev / 100)
self.ale = self.sle * aro_val
```

Two Flask routes handle everything: one renders the form and processes submissions, the other clears the calculator back to its default state.

## Screenshots

Input and output chart, and desk check results, are in `/screenshots`.

## Project structure

```
sle-ale-risk-calculator/
├── app.py
├── requirements.txt
├── templates/
│   └── template.html
├── static/
│   ├── styles.css
│   ├── cloud_background.jpg
│   ├── web_banner.png
│   ├── dollar_spin.gif
│   ├── dollar_spin_2.gif
│   ├── welcome_to_my_homepage.gif
│   ├── german_shepard.gif
│   ├── german_shepard_2.gif
│   ├── spinning_globe.gif
│   ├── netscape_picture.gif
│   └── hack_the_planet.gif
├── screenshots/
├── corrected_scripts/
└── docs/
```

The `templates` and `static` folders follow Flask's default convention, so `app.py` finds them without any extra configuration.

## Debugging work

Part of this assessment involved taking three broken scripts and correcting every syntax and logic error in them:

- **Application 3a**: fixed a missing colon, a malformed class definition, and swapped a hardcoded pi value for `math.pi`
- **Application 3b**: rebuilt a broken Tkinter GUI, fixed incorrect casing on `tkinter`, and added error handling for invalid input
- **Application 3c**: added input validation loops for hours and pay rate, so the script no longer crashes on bad input

The corrected scripts are in `/corrected_scripts`, and the full debugging log with before and after screenshots is in `/docs`.

## Setup

```bash
git clone https://github.com/thehumangrace/sle-ale-risk-calculator.git
cd sle-ale-risk-calculator
pip install -r requirements.txt
python app.py
```

The app runs at `http://localhost:8080`.

## Project background

Built for the ICTPRG435 unit at The Gordon, October 2025. The original assessment covered application design, pseudocode, a desk check against sample device data, and the debugging work described above. The full assessment report is in `/docs/full_report.md`.
