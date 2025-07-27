# explore_datetime.py
# This script demonstrates usage of Python's datetime module
# to handle current date/time and calculate a future date

from datetime import datetime, timedelta  # Import necessary components

def display_current_datetime():
    """
    Display the current date and time in 'YYYY-MM-DD HH:MM:SS' format
    """
    current_date = datetime.now()  # Get current date and time
    # Format and print the date/time
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    """
    Prompt user for number of days and calculate future date
    """
    # Take input from user and convert it to an integer
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    
    current_date = datetime.now()  # Get current date again
    # Add specified days to the current date
    future_date = current_date + timedelta(days=number_of_days)
    
    # Print the future date in 'YYYY-MM-DD' format
    print("Future date:", future_date.strftime("%Y-%m-%d"))

# --- Script Execution ---
display_current_datetime()  # Call function to show current date/time
calculate_future_date()     # Call function to calculate future date
