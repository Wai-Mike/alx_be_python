from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in YYYY-MM-DD HH:MM:SS format.
    """
    current_date = datetime.now()
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_datetime}")
    return current_date

def calculate_future_date(days_to_add):
    """
    Calculate and display a future date by adding specified days to current date.
    
    Args:
        days_to_add (int): Number of days to add to current date
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")
    return future_date

def main():
    """
    Main function to demonstrate datetime module functionality.
    """
    # Part 1: Display current date and time
    print("Part 1: Current Date and Time")
    current_date = display_current_datetime()
    
    # Part 2: Calculate future date
    print("\nPart 2: Calculate Future Date")
    try:
        days_input = input("Enter the number of days to add to the current date: ")
        days_to_add = int(days_input)
        future_date = calculate_future_date(days_to_add)
    except ValueError:
        print("Error: Please enter a valid integer for the number of days.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
