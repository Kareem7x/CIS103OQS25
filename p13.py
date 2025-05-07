def main():
    roman_map = {
        1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI',
        7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 11: 'XI', 12: 'XII',
        13: 'XIII', 14: 'XIV', 15: 'XV', 16: 'XVI', 17: 'XVII', 18: 'XVIII',
        19: 'XIX', 20: 'XX', 21: 'XXI', 22: 'XXII', 23: 'XXIII', 24: 'XXIV'
    }
    print("Initial Dictionary:")
    print(roman_map)

    while True:
        try:
            
            decimal = input("Enter a decimal number: ")

            
            if not decimal:
                print("Input cannot be blank.")
                continue

            if not decimal.isdigit():
                print("Input must be a number (integer).")
                continue

            number = int(decimal)

            
            if number <= 0:
                break

            
            if number in roman_map:
                print("The Roman numeral for", number, "is", roman_map[number])
            
            else:
                roman_numeral = input(f"Enter the roman numeral for {number}: ")  

                
                if not roman_numeral.isalpha(): 
                  print ("Numeral must be alphabetic") 

                else:
                  roman_map[number] = roman_numeral
                  print (str(number) + " " + roman_numeral + " to dictionary.")

        
        except Exception as e:
            print("Looks like there is an error ", e)

    print("\nFinal Dictionary:") 
    print(roman_map) 


main()