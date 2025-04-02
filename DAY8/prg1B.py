def temperature_converter():
    print("Temperature Converter")
    temp = float(input("Enter temperature: "))
    
    print("\nSelect the unit of the input temperature:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    input_unit = input("Enter choice (1/2/3): ")

    print("\nSelect the unit to convert to:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    output_unit = input("Enter choice (1/2/3): ")

    # Celsius to Fahrenheit and Kelvin
    if input_unit == '1':
        if output_unit == '2':  # Celsius to Fahrenheit
            fahrenheit = (temp * 9/5) + 32
            print(f"{temp}°C is {fahrenheit}°F")
        elif output_unit == '3':  # Celsius to Kelvin
            kelvin = temp + 273.15
            print(f"{temp}°C is {kelvin}K")
        elif output_unit == '1':  # Celsius to Celsius
            print(f"{temp}°C is {temp}°C")
        else:
            print("Invalid output unit")

    # Fahrenheit to Celsius and Kelvin
    elif input_unit == '2':
        if output_unit == '1':  # Fahrenheit to Celsius
            celsius = (temp - 32) * 5/9
            print(f"{temp}°F is {celsius}°C")
        elif output_unit == '3':  # Fahrenheit to Kelvin
            kelvin = (temp - 32) * 5/9 + 273.15
            print(f"{temp}°F is {kelvin}K")
        elif output_unit == '2':  # Fahrenheit to Fahrenheit
            print(f"{temp}°F is {temp}°F")
        else:
            print("Invalid output unit")

    # Kelvin to Celsius and Fahrenheit
    elif input_unit == '3':
        if output_unit == '1':  # Kelvin to Celsius
            celsius = temp - 273.15
            print(f"{temp}K is {celsius}°C")
        elif output_unit == '2':  # Kelvin to Fahr13enheit
            fahrenheit = (temp - 273.15) * 9/5 + 32
            print(f"{temp}K is {fahrenheit}°F")
        elif output_unit == '3':  # Kelvin to Kelvin
            print(f"{temp}K is {temp}K")
        else:
            print("Invalid output unit")

    else:
        print("Invalid input unit")

temperature_converter()
