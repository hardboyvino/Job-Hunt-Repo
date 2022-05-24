# Problem Statement - Write a Python program to convert month name to a number of days.

calendar = {
    "January": "31 days",
    "February": "28/29 days",
    "March": "31 days",
    "April": "30 days",
    "May": "31 days",
    "June": "30 days",
    "July": "31 days",
    "August": "31 days",
    "September": "30 days",
    "October": "31 days",
    "November": "30 days",
    "December": "31 days",
}

month = input("Input the name of Month: ").strip().title()

if month in calendar:
    print(calendar[month])