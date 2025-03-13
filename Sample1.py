
def check_odd_even(char):
    if char.isdigit():
        num = int(char)
        if num % 2 == 0:
            return f"{char} is an even number"
        else:
            return f"{char} is an odd number"
    return None

def check_vowel_consonant(char):
    vowels = "AEIOUaeiou"
    if char.isalpha():
        if char in vowels:
            return f"{char.upper()} IS A VOWEL LETTER"
        else:
            return f"{char} is a consonant letter"
    return None

def check_special_character(char):
    if not char.isalnum():
        return f"{char} is a special character"
    return None

def process_input(user_input):
    print(f"USER INPUT: {user_input}")
    for char in user_input:
        result = check_vowel_consonant(char) or check_odd_even(char) or check_special_character(char)
        if result:
            print(result)

def main():
    while True:
        print("\n1. Function for determining a number as odd or even")
        print("2. Function for determining a letter as vowel or consonant")
        print("3. Function for determining a character as special character")
        print("4. Combination of all functions")
        print("Type 'STOP' to exit")
        
        choice = input("\nEnter your choice: ").strip()
        
        if choice.lower() == "stop":
            print("Program stopped.")
            break
        elif choice in ["1", "2", "3", "4"]:
            user_input = input("\nEnter a string: ").strip()
            process_input(user_input)
        else:
            print("Invalid choice. Please enter a number between 1-4 or 'STOP' to exit.")

if __name__ == "__main__":
    main()
