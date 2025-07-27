# temp_conversion_tool.py
# Script to convert temperatures between Celsius and Fahrenheit
# using global conversion factors to illustrate variable scope

# --- Global Conversion Factors ---
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    """
    Converts Fahrenheit to Celsius using global conversion factor
    """
    # Access global variable (read-only, no need for 'global' keyword)
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit using global conversion factor
    """
    # Access global variable (read-only, no need for 'global' keyword)
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# --- Main User Interaction ---
try:
    # Prompt user to enter temperature value
    temperature_input = input("Enter the temperature to convert: ")
    temperature = float(temperature_input)  # Validate numeric input

    # Prompt user to specify unit
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    # Conversion logic based on unit
    if unit == "F":
        converted = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted}°C")
    elif unit == "C":
        converted = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted}°F")
    else:
        raise ValueError("Invalid unit. Please enter 'C' or 'F'.")

except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
