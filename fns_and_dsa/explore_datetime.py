import datetime

# Part 1: Function to display the current date and time
def display_current_datetime():
    # Get the current date and time
    current_datetime = datetime.datetime.now()
    
    # Format the current date and time as "YYYY-MM-DD HH:MM:SS"
    current_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    
    # Print the current date and time
    print("Current Date and Time:", current_date)

# Part 2: Function to calculate a future date
def calculate_future_date():
    # Ask the user to input a number of days
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    
    # Get the current date
    current_date = datetime.datetime.now()
    
    # Calculate the future date by adding the number of days
    future_date = current_date + datetime.timedelta(days=days_to_add)
    
    # Format and print the future date as "YYYY-MM-DD"
    print("Future Date:", future_date.strftime("%Y-%m-%d"))

# Call Part 1 function to display current date and time
display_current_datetime()

# Call Part 2 function to calculate and display future date
calculate_future_date()
