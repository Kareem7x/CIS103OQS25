import random

def generate_lottery_numbers(highest_number, num_to_generate):
    numbers = set()
    while len(numbers) < num_to_generate:
        numbers.add(random.randint(1, highest_number))
    return sorted(list(numbers))

def powerball():
    numbers = generate_lottery_numbers(69, 5)
    print("Powerball", ", ".join(map(str, numbers)))

def mega_million():
    numbers = generate_lottery_numbers(70, 5)
    print("Mega Million", ", ".join(map(str, numbers)))

def lucky_day_lotto():
    numbers = generate_lottery_numbers(45, 5)
    print("Lucky Day Lotto", ", ".join(map(str, numbers)))

def lotto():
    numbers = generate_lottery_numbers(52, 6)
    print("Lotto", ", ".join(map(str, numbers)))

def main():
    while True:
        print("\nIllinois Lottery Number Generator")
        print("1. Powerball")
        print("2. Mega Million")
        print("3. Lucky Day Lotto")
        print("4. Lotto")
        print("9. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            powerball()
        elif choice == '2':
            mega_million()
        elif choice == '3':
            lucky_day_lotto()
        elif choice == '4':
            lotto()
        elif choice == '9':
            break
        else:
            print("Invalid menu selection")
        input("Hit enter key to return to menu")

    print("---done---")

if __name__ == "__main__":
    main()