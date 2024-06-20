import random
import string
def get_user_input():
    length = int(input("Enter password length: "))
    include_letters = input("Include letters? (y/n): ").lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    return length, include_letters, include_numbers, include_symbols
def generate_password(length, include_letters, include_numbers, include_symbols):
    character_set = ''
    if include_letters:
        character_set += string.ascii_letters
    if include_numbers:
        character_set += string.digits
    if include_symbols:
        character_set += string.punctuation

    if not character_set:
        raise ValueError("No characters available to generate password.")

    password = ''.join(random.choice(character_set) for _ in range(length))
    return password
def main():
    length, include_letters, include_numbers, include_symbols = get_user_input()
    try:
        password = generate_password(length, include_letters, include_numbers, include_symbols)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
