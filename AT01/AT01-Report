# Programming - AT1

**Grace Garrett | 13260436**

**Write scripts for software applications (22603VIC)**

**October 16, 2025**

## Table of Contents

- [Introduction](#introduction)

- [Project Task 1](#project-task-1)

 - [Written Email Response](#written-email-response)

- [Project Task 2](#project-task-2)

 - [Input-Process-Output Chart](#input-process-output-chart)

 - [Variable List](#variable-list)

 - [English Method (Pseudocode)](#english-method-pseudocode)

 - [Python Code](#python-code)

 - [Desk Check - Summary Table - All Results](#desk-check-summary-table-all-results)

- [Project Task 3](#project-task-3)

 - [Application 3a](#application-3a)

 - [Application 3b](#application-3b)

 - [Application 3c](#application-3c)

- [Project Task 4](#project-task-4)

 - [Debugging Documentation](#debugging-documentation)

- [Conclusion](#conclusion)

- [References](#references)

---

## Introduction

This assessment will demonstrate my ability to design, write, and test Python applications that meet specific user and business requirements. Each project task highlights different aspects of programming, including planning and documentation using pseudocode and Input-process-output charts, to writing clean, functional Python scripts with validation and proper use of commenting. The assessment also focuses on identifying and correcting syntax and logic errors and writing thorough structured debugging documentation. Together, these tasks show how programming principles can be applied to create reliable, user-friendly, and well-documented software solutions.

---

## Project Task 1

### Written Email Response

Good Morning, J.Brin

Please see attached:

1. The developed application (app) you requested
2. All relevant documentation for the developed app
3. The documentation of which Python graphical user interface (GUI) framework and interactive development environment (IDE) was used during development
4. All amended code for Application_3a.py, Application_3b.py and Application_3c.py

If you have any question or queries feel free to send me an email and I will be happy to elaborate.

Regards,

Grace Garrett

Software Consultant

---

## Project Task 2

### Input-Process-Output Chart

| Input                         | Process                                             | Output                                     |
| ----------------------------- | --------------------------------------------------- | ------------------------------------------ |
| Asset Value                   | Multiply: Asset Value × Exposure Value = SLE        | SLE is: *Single Loss Expectancy (SLE)*     |
| Exposure Value                | Multiply: SLE × Annualised Rate of Occurrence = ALE | ALE is: *Annualised Loss Expectancy (ALE)* |
| Annualised Rate of Occurrence |                                                     |                                            |

### Variable List

| Variable       | Type  | Description                                                  |
| -------------- | ----- | ------------------------------------------------------------ |
| asset_value    | Float | How much item cost                                           |
| exposure_value | Float | Percentage of asset value that would be lost if a security incident occurred |
| aro            | Float | The amount of times an incident is expected to occur         |
| sle            | Float | The expected monetary loss from a single incident            |
| ale            | Float | The expected monetary loss annually                          |

### English Method (Pseudocode)

```pseudocode
\\!/usr/bin/env python3
\\SLE-ALE Calculator
\\Name: Grace Garrett
\\Date: 16/10/2025
\\Date Last Modified: 04/11/2025

START PROGRAM SLE-ALE Risk Calculator

CLASS RiskCalculator
    ATTRIBUTES:
        title
        asset_value
        exposure_value
        aro (Annual Rate of Occurrence)
        sle (Single Loss Expectancy)
        ale (Annualised Loss Expectancy)
        error

    METHOD Initialize(title)
        SET title to provided title
        SET all other attributes to empty strings
    END METHOD

    METHOD calculate_risk()
        TRY
            CONVERT asset_value to decimal number as av
            CONVERT exposure_value to decimal number as ev
            CONVERT aro to decimal number as aro_val

            IF av < 0 OR ev < 0 OR aro_val < 0 THEN
                CLEAR sle and ale
                SET error to "Bummer! No negative numbers allowed. Try again, pal!"
                EXIT method
            END IF

            IF ev > 100 THEN
                CLEAR sle and ale
                SET error to "Bummer! Exposure value can't be more than 100%. Try again, pal!"
                EXIT method
            END IF

            CALCULATE sle = av * (ev ÷ 100)
            CALCULATE ale = sle * aro_val

            FORMAT sle to 2 decimal places
            FORMAT ale to 2 decimal places
            CLEAR error message

        CATCH invalid input error
            CLEAR sle and ale
            SET error to "Bummer! Those digits don't compute. Try again, pal!"
        END TRY
    END METHOD
END CLASS

MAIN PROGRAM
    CREATE calculator object with title "SLE-ALE Calculator"

    ROUTE for home page ("/")
        IF request is GET THEN
            DISPLAY template with calculator data
        ELSE IF request is POST THEN
            GET asset_value from form input
            GET exposure_value from form input
            GET aro from form input
            CALL calculate_risk() method
            DISPLAY template with updated calculator data
        ELSE
            DISPLAY "Invalid request method!"
        END IF
    END ROUTE

    ROUTE for clear function ("/clear")
        RESET asset_value to empty
        RESET exposure_value to empty
        RESET aro to empty
        RESET sle to empty
        RESET ale to empty
        RESET error to empty
        DISPLAY template with cleared calculator data
    END ROUTE

    START web application on port 8080
END PROGRAM

```


### Python Code

```python
#!/usr/bin/env python3

#SLE-ALE Calculator

#Name: Grace Garrett

#Date:16/10/2025

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

```

### Desk Check - Summary Table - All Results

| Device      | Exposure Level | Asset Value ($) | Exposure Value (%) | ARO  | SLE ($) | ALE ($) |
| ----------- | -------------- | --------------- | ------------------ | ---- | ------- | ------- |
| Server      | Low            | 4214            | 2                  | 0.05 | 84.28   | 4.21    |
| Server      | Medium         | 4214            | 30                 | 0.05 | 1264.20 | 63.21   |
| Server      | High           | 4214            | 80                 | 0.05 | 3371.20 | 168.56  |
| Workstation | Low            | 2165            | 8                  | 0.1  | 173.20  | 17.32   |
| Workstation | Medium         | 2165            | 50                 | 0.1  | 1082.50 | 108.25  |
| Workstation | High           | 2165            | 75                 | 0.1  | 1623.75 | 162.38  |
| Router      | Low            | 3412            | 2                  | 0.04 | 68.24   | 2.73    |
| Router      | Medium         | 3412            | 36                 | 0.04 | 1228.32 | 49.13   |
| Router      | High           | 3412            | 90                 | 0.04 | 3070.80 | 122.83  |
| Switch      | Low            | 2111            | 2                  | 0.04 | 42.22   | 1.69    |
| Switch      | Medium         | 2111            | 50                 | 0.04 | 1055.50 | 42.22   |
| Switch      | High           | 2111            | 89                 | 0.04 | 1878.79 | 75.15   |
| Laptop      | Low            | 2444            | 8                  | 0.11 | 195.52  | 21.51   |
| Laptop      | Medium         | 2444            | 30                 | 0.11 | 733.20  | 80.65   |
| Laptop      | High           | 2444            | 86                 | 0.11 | 2101.84 | 231.20  |
| Printer     | Low            | 988             | 4                  | 0.11 | 39.52   | 4.35    |
| Printer     | Medium         | 988             | 50                 | 0.11 | 494.00  | 54.34   |
| Printer     | High           | 988             | 90                 | 0.11 | 889.20  | 97.81   |

---

## Project Task 3

### Application 3a

```python
#!/usr/bin/env python3

# Coded Python Script
# Author Linus Torvalds
# Date: 18/09/2025

# Import math module for accurate pi value
import math

# CamelCase is preferable when creating a class
class Areas:
    # Added a missing colon for function definition
    def rect_square(self, side_length):
        # Uses a local variable
        square_area = side_length * side_length
        return square_area

    # Added a space for function and deleted semicolons
    def circle_area(self, radius_length):
        # Made calculation more concise
        # Use math.pi for more accurate value (3.14)
        circle_area = math.pi * radius_length ** 2
        return circle_area

def main():
    # This function is not part of the class Areas()
    # Create an instance of Areas class
    calculator = Areas()
    # Removed any redundancies
    # Format output to 2 decimal places for cleaner display
    print(f"Area of square is: {calculator.rect_square(2):.2f}")
    print(f"Area of circle is: {calculator.circle_area(3):.2f}")

# Added condition to only run main when script is executed directly
if __name__ == "__main__":
    main()
```

### Application 3b

```python
#!/usr/bin/env python3

# Coded Python Script
# Author: Margaret Hamilton
# Date: 29/10/2025

#Changed the capital T to a lowercase t
from tkinter import * # import everything from the Tkinter GUI framework

#Closed bracket and added colon and 
# Changed "pay" to "age".in comment
def calculate_age(): # calculate the age and display
    #Removed global age
    
    # Added error handling for invalid input
    try:
        # Removed redundancies and fixed syntax of function 
        days = 365 * float(e1.get())
        e2.config(text="Age in days is " + str(int(days)))
        e1.delete(0, 'end')
    except ValueError:
        # Shows error message if input is not a number
        e2.config(text="Error: We need a number, champ.")

# Added colon and space
def close_window(): # close menu window and stop program
    master.destroy()

# Closed bracket
master = Tk()

# Added corrected geometry format and got rid of spaces
master.geometry("350x200")

#Added changed title to be clearer
master.title("Age Calculator")


# Reordered labels and entries
# Added specifications for position of label
Label(master, text="Enter your age in years:").grid(row=0, sticky=W, padx=5, pady=5)

# Moved entry creation here
e1 = Entry(master)

#This will initialise the label for output
e2 = Label(master, text="")

# Bind Enter key to calculate function
# The lambda ignores the event parameter that tkinter passes
e1.bind('<Return>', lambda event: calculate_age())

#This will place the entry in grid
e1.grid(row=0, column=1, padx=5, pady=5)

#This will initialise the output Label's position
e2.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

# Buttons
# Creates buttons
# grid places buttons using a grid layout
# row and column specifies position
# sticky=W means buttons will stick to the West of grid
# pady=4 means there will be padding of 4 pixels around button for spacing
Button(master, text='Calc', command=calculate_age).grid(row=4, column=1, sticky=W, pady=4)
Button(master, text='Quit', command=close_window).grid(row=4, column=0, sticky=E, padx=10, pady=4)

# Changed to a lowercase m and changed from master.destroy
master.mainloop()
```

### Application 3c

```python
#!/usr/bin/env python3

# Coded Python Script
# Author Grace Hopper 
# Date: 29/10/2025

# Added space between import and os
import os

#initialise variables
hours=0
rate=0
pay=0

# Added closing quotation
os.system("clear")
# run the Linux system clear screen command

# input values with error handling
# Added while loop to keep asking until valid input
while True:
    try:
        # Added closing bracket and spaces
        hours = float(input("Enter your hours: "))
        # Check if hours is negative
        if hours < 0:
            print("Error: It can't be a negative number, chief.")
            continue
        break  # Exits loop if input is valid
    except ValueError:
        # Catches accidental letters or symbols
        print("Error: Try a number this time, buddy.")

# Added while loop for rate input validation
while True:
    try:
        # Added closing quotation spaces and removed semicolons
        rate = float(input("Enter pay rate: "))
        # Check if rate is negative
        if rate < 0:
            print("Error: It can't be a negative number, friend.")
            continue
        break  # Exit loop if input is valid
    except ValueError:
        # Catches accidental letters or symbols
        print("Error: Try a number this time, guy.")

# Added spaces
pay = hours*rate

# Added the print statement here to make calculated pay show
# the f indicates an f-string
# 2f formats for 2 decimal places instead of only 1
print(f"Total Pay is: ${pay:.2f}")
```

---

## Project Task 4

### Debugging Documentation

**Script Name:** Application_3c

**Author:** Grace Hopper

**Date Debugged:** 29/10/2025

**Purpose:** Calculate employee pay based on hours worked and hourly rate

#### Errors Identified and Corrections

**Error #1: Import Statement Syntax Error**

- **Line:** 5

- **Original Code:** `importos`

- **Error Type:** Syntax Error

- **Problem:** Missing space between import and os prevents Python from recognizing the import statement

- **Corrected Code:** `import os`

- **Screenshots:**

 ![Error 1 original](images/image1.PNG)

 ![Error 1 corrected](images/image2.PNG)

**Error #2: Unclosed String in os.system()**

- **Line:** 13

- **Original Code:** `os.system("clear)`

- **Error Type:** Syntax Error (SyntaxError: while scanning string)

- **Problem:** Missing closing quotation mark makes Python unable to finish the string

- **Corrected Code:** `os.system("clear")`

- **Screenshots:**

 ![Error 2 original](images/image3.PNG)

 ![Error 2 corrected](images/image4.PNG)

**Error #3: Misplaced Print Statement**

- **Line:** 16

- **Original Code:** `print("Pay is $ : " + str(pay))`

- **Error Type:** Logic Error

- **Problem:** Print statement appears before calculations are performed, making the output $0.00 instead of the calculated pay

- **Corrected Code:** Moved to line 54 after calculation: `print(f"Total Pay is: ${pay:.2f}")`

- **Screenshots:**

 ![Error 3 original](images/image5.PNG)

 ![Error 3 corrected](images/image6.PNG)

**Error #4: Unclosed Bracket in hours Input**

- **Line:** 17

- **Original Code:** `hours=float(input("Enter your hours: ")`

- **Error Type:** Syntax Error

- **Problem:** Missing closing bracket for the float() function

- **Corrected Code:** `hours = float(input("Enter your hours: "))`

- **Screenshots:**

 ![Error 4 original](images/image7.PNG)

 ![Error 4 corrected](images/image8.PNG)

**Error #5: Multiple Syntax Errors in rate Input**

- **Line:** 18

- **Original Code:** `rate=float(input("Enter pay rate: ));;;;`

- **Error Type:** Multiple Syntax Errors

- **Problems:**

 - Missing closing quotation mark

 - Extra closing bracket

 - Unnecessary semicolons (not used in Python)

- **Corrected Code:** `rate = float(input("Enter pay rate: "))`

- **Screenshots:**

 ![Error 5 original](images/image9.PNG)

 ![Error 5 corrected](images/image10.PNG)

**Error #6: Missing Spaces in Calculation**

- **Line:** 20

- **Original Code:** `pay=hours*rate`

- **Error Type:** Style/Readability Issue

- **Problem:** Lacks spacing around operators (not an error but is generally good practice in some style guidelines)

- **Corrected Code:** `pay = hours * rate`

- **Screenshots:**

 ![Error 6 original](images/image11.PNG)

 ![Error 6 corrected](images/image12.PNG)

#### Enhancements Made

**Enhancement #1: Input Validation with Error Handling**

- **Lines:** 19-32 and 34-46

- **Addition:** Created while loops with error handling

- **Purpose:**

 - Catches ValueError exceptions when users enters anything other than a number

 - Validates that hours and rate are not negative

 - Provides user-friendly error messages

 - Continues prompting until valid input is received

- **Benefit:** Prevents program crashes and improves user experience

- **Screenshots:**

 ![Enhancement 1 part 1](images/image13.PNG)

 ![Enhancement 1 part 2](images/image14.PNG)

**Enhancement #2: Improved Output Formatting**

- **Line:** 49

- **Addition:** Changed from string to f-string with formatting

- **Original:** `"Pay is $ : " + str(pay)`

- **Improved:** `f"Total Pay is: ${pay:.2f}"`

- **Benefit:** Ensures pay displays exactly 2 decimal places (currency format)

- **Screenshot:**

 ![Enhancement 2](images/image6.PNG)

#### Testing Results

**Test 1: Valid Input**

- **Input:** Hours = 40, Rate = 25.50

- **Expected Output:** Total Pay is: $1020.00

- **Actual Output:** Total Pay is: $1020.00

- **Status:** ✓ PASSED

- **Screenshot:**

 ![Test 1](images/image15.PNG)

**Test 2: Negative Hours**

- **Input:** Hours = -5

- **Expected Output:** Error message, prompt to re-enter

- **Actual Output:** "Error: It can't be a negative number, chief."

- **Status:** ✓ PASSED

- **Screenshot:**

 ![Test 2](images/image16.PNG)

**Test 3: Non-numeric Input (Letters)**

- **Input:** Hours = "abc"

- **Expected Output:** Error message, prompt to re-enter

- **Actual Output:** "Error: Try a number this time, buddy."

- **Status:** ✓ PASSED

- **Screenshot:**

 ![Test 3](images/image17.PNG)

**Test Case 4: Decimal Values**

- **Input:** Hours = 37.5, Rate = 18.75

- **Expected Output:** Total Pay is: $703.12

- **Actual Output:** Total Pay is: $703.12

- **Status:** ✓ PASSED

- **Screenshot:**

 ![Test 4](images/image18.PNG)

---

## Conclusion

Completing this assessment has reinforced my understanding of structured programming, debugging, and user interface design. It has been a very new experience for me to deal with core programming concepts like error handling, pseudo-code writing and creating/testing an entire web app (with python, html and css). Overall, this project has strengthened my skills in writing professional looking, maintainable code and demonstrated how patience and testing are essential to successful software development.

---

## References

- W3Schools (2019). *Python Tutorial*. [online] W3schools.com. Available at: <https://www.w3schools.com/python/default.asp>.

- Metwalli, S. (2022). *Pseudocode: What It Is and How to Write It | Built In*. [online] builtin.com. Available at: <https://builtin.com/data-science/pseudocode>.

- GeeksforGeeks (2018). *How to write a Pseudo Code?* [online] GeeksforGeeks. Available at: <https://www.geeksforgeeks.org/dsa/how-to-write-a-pseudo-code/>.

- White, C. (2018). *Documenting Debugging Processes - Chris White - Medium*. [online] Medium. Available at: <https://medium.com/@cwgem/documenting-debugging-processes-2707c46c5f8e>.

- Meegle.com. (2025). *Debugging Documentation*. [online] Available at: <https://www.meegle.com/en_us/topics/debugging/debugging-documentation> [Accessed 6 Nov. 2025].

- Dyouri, A. (2020). *How To Make a Web Application Using Flask in Python 3*. [online] DigitalOcean. Available at: <https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3>.

- Indeed Career Guide. (2024). *What Is an ALE Formula? (And How To Use It)*. [online] Available at: <https://www.indeed.com/career-advice/career-development/ale-formula>.

- W3Schools (2022). *CSS Tutorial*. [online] W3schools.com. Available at: <https://www.w3schools.com/css/default.asp>.

- W3Schools (2022). *HTML Tutorial*. [online] W3schools.com. Available at: <https://www.w3schools.com/html/default.asp>.
