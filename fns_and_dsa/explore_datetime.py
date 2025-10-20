from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format the date and time as "YYYY-MM-DD HH:MM:SS"
    formatted_current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_current_date)

def calculate_future_date():
    # Prompt the user to enter a number of days
    number_of_days = int(input("Enter number of days to add: "))
    # Get the current date
    current_date = datetime.now()
    # Calculate the future date by adding the specified number of days
    future_date = current_date + timedelta(days=number_of_days)
    # Format the future date as "YYYY-MM-DD"
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print("Future date after adding", number_of_days, "days:", formatted_future_date)

# Call the functions
display_current_datetime()
calculate_future_date()
