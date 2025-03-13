
def check_odd_even():
    num = input("Enter a number: ")
    if num.isdigit():
        num = int(num)
        if num % 2 == 0:
            print(f"{num} is Even.")
        else:
            print(f"{num} is Odd.")
    else:
        print("Invalid input. Please enter a valid number.")

def check_vowel_consonant():
    char = input("Enter a letter: ").lower()
    if char.isalpha() and len(char) == 1:
        if char in 'aeiou':
            print(f"{char} is a Vowel.")
        else:
            print(f"{char} is a Consonant.")
    else:
        print("Invalid input. Please enter a single letter.")

def check_special_character():
    char = input("Enter a character: ")
    if not char.isalnum() and len(char) == 1:
        print(f"{char} is a Special Character.")
    else:
        print("Invalid input. Please enter a single special character.")

def combined_function():
    check_odd_even()
    check_vowel_consonant()
    check_special_character()

def main():
    while True:
        print("\nMENU:")
        print("1. Check if a number is odd or even")
        print("2. Check if a letter is a vowel or consonant")
        print("3. Check if a character is special")
        print("4. Perform all checks")
        print("Type 'STOP' to exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            check_odd_even()
        elif choice == "2":
            check_vowel_consonant()
        elif choice == "3":
            check_special_character()
        elif choice == "4":
            combined_function()
        elif choice.lower() == "stop":
            print("Program stopped.")
            break
        else:
            print("Invalid choice. Please enter a number between 1-4 or type 'STOP' to exit.")

if __name__ == "__main__":
    main()
