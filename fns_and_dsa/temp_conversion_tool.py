# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.
    
    Args:
        fahrenheit (float): Temperature in Fahrenheit
    
    Returns:
        float: Temperature in Celsius
    """
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    
    Args:
        celsius (float): Temperature in Celsius
    
    Returns:
        float: Temperature in Fahrenheit
    """
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    """
    Main function to handle user interaction and temperature conversion.
    """
    try:
        # Get temperature input from user
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)
        
        # Get unit input from user
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if unit == 'F':
            # Convert Fahrenheit to Celsius
            celsius = convert_to_celsius(temperature)
            print(f"{temperature}°F is {celsius}°C")
        elif unit == 'C':
            # Convert Celsius to Fahrenheit
            fahrenheit = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {fahrenheit}°F")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
            
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
