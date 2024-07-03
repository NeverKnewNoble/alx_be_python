# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# Function to handle user interaction
def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'F':
            converted_temperature = convert_to_celsius(temperature)
            print(f"{temperature:.1f}°F is {converted_temperature:.1f}°C")
        elif unit == 'C':
            converted_temperature = convert_to_fahrenheit(temperature)
            print(f"{temperature:.1f}°C is {converted_temperature:.1f}°F")
        else:
            raise ValueError("Invalid temperature unit. Please enter 'C' or 'F'.")
    
    except ValueError as ve:
        print(f"Error: {ve}. Please enter a numeric value.")

if __name__ == "__main__":
    main()
