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