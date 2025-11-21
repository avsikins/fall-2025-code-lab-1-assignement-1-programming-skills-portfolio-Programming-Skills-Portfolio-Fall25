# Exercise 05: Days of the Month
# This program asks the user for a month number and returns the number of days in that month
# considering leap years for February.

calendar = {
    "January": 31,
    "February": 28, 
    "Leap": 29,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

month_number = int(input("Enter the month number (1-12): "))
month_names = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Validates the month number and get days
if 1 < month_number < 12:
    month_name = month_names[month_number - 1]
    # Handle February separately for leap years
    if month_name == "February":
        leap_year = input("Is it a leap year? (yes/no): ").strip().lower() 
        if leap_year == "yes":
            days = calendar["Leap"]
        else:
            days = calendar["February"]
    else:
        days = calendar[month_name]
    print(f"{month_name} has {days} days.")
else:
        print("Invalid month number. Please enter a number between 1-12.") 