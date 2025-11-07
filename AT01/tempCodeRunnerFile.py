# Bind Enter key to calculate function
# The lambda ignores the event parameter that tkinter passes
e1.bind('<Return>', lambda event: calculate_age())