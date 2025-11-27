from generator.validator import validate_choices, validate_length
from generator.generator import create_password

def get_bool_input(prompt):
    return input(prompt + " y/n: ").lower() == "y"

def main():

    print("\n🔐 PASSWORD GENERATOR 🔐\n")

    try:
        length = int(input("Enter password length: "))
        
        include_lowercase = get_bool_input("Include lowercase letters? ")
        include_uppercase = get_bool_input("Include uppercase letters? ")
        include_digits = get_bool_input("Include digits? ")
        include_symbols = get_bool_input("Include symbols? ")
        validate_length(length)
        validate_choices(include_lowercase, include_uppercase, include_digits, include_symbols)
        password = create_password(
            length,
            include_lowercase,
            include_uppercase,
            include_digits,
            include_symbols
        )
        print(f"\n Your generated password:  {password}")

    except ValueError as e:
        print ("Error: ", e)


if __name__ == "__main__":
    main()
