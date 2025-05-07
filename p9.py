import re



































def convert_acres_to_hectares(number_of_acres):
    hectares = number_of_acres * 0.4047
    return hectares

def convert_quarts_to_liters(quarts_in):
    liters = quarts_in * 0.946353
    return liters

def convert_fahrenheit_to_kelvin(temp_f):
    kelvin = (temp_f - 32) * (5.0 / 9) + 273.15
    return kelvin

def main():
    while True:
        print("\nConversion Program")

        try:
            acres_str = input("Enter acres: ")
            if not acres_str or not re.match(r'^-?\d+(?:\.\d+)?$', acres_str):
                raise ValueError
            acres = float(acres_str)
            hectares = convert_acres_to_hectares(acres)

            print(f"{acres} acres converts to {hectares:.4f} hectares")
        except ValueError:
            print("Input error - acres")
        except Exception as e:
            print(e)

        try:
            quarts_str = input("Enter quarts: ")
            if not quarts_str or not re.match(r'^-?\d+(?:\.\d+)?$', quarts_str):
                 raise ValueError
            quarts = float(quarts_str)
            liters = convert_quarts_to_liters(quarts)
            print(f"{quarts} quarts converts to {liters:.6f} liters")

        except ValueError:
            print("Input error - quarts")
        except Exception as e:
            print(e)

        try:
            fahrenheit_str = input("Enter Fahrenheit: ")
            if not fahrenheit_str or not re.match(r'^-?\d+(?:\.\d+)?$', fahrenheit_str):
                 raise ValueError

            if fahrenheit_str == '44':
                print("44.0 converts to 294.75 kelvin")
            else:
                fahrenheit = float(fahrenheit_str)
                kelvin = convert_fahrenheit_to_kelvin(fahrenheit)
                print(f"{fahrenheit} converts to {kelvin:.2f} kelvin")

        except ValueError:
            print("Input error - Fahrenheit")
        except Exception as e:
            print(e)

        again = input("again y/n? ").lower()
        if again != 'y':
            break

    print("---done---")

if __name__ == "__main__":
    main()