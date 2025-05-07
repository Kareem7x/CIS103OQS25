def recursive_sum(n):
    if n <= 0:
        return 0
    else:
        return n + recursive_sum(n - 1)

def main():
    while True:
        print("\n--- sum up numbers---")
        try:
            number_str = input("enter number:")
            if not number_str:
                print("Input cannot be blank")
                continue

            number = int(number_str)
            if number < 0:
                print("number cannot be negative")
                continue

            total = recursive_sum(number)

            addition_string = '+'.join(str(i) for i in range(number, 0, -1))

            print(addition_string + " = " + str(total))

        except ValueError:
            print("Invalid input detected")

        again = input("Another number (y/n): ").lower()
        if again != 'y':
            break

    print("---done---")

if __name__ == "__main__":
    main()