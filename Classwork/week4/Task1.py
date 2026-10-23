#task 1 password policy validator
ALLOWED_SYMBOLS = "!@#$%"

def validate_password(password: str) -> bool:
    """
    Return True if password meets the organisations policy 
    at least 10 characters 
    at least 1 upper case letter 
    at least 1 lowercase letter 
    at least 2 digits
    at least 1 symbol and only the symbols ! @ # $ % are allowed 
    no spaces
    """
    # minimum length
    if len(password) < 10:
        return False

    # no spaces allowed 
    if " " in password:
        return False

    upper_count = 0 
    lower_count = 0
    digit_count = 0
    symbol_count = 0

    for char in password:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char in ALLOWED_SYMBOLS:
            symbol_count += 1
        else:
            # any other characters is not an allowed symbol
            return False

    return (
        upper_count >= 1
        and lower_count >= 1
        and digit_count >= 1
        and symbol_count >= 1
    )

def main():
    print("---Task 1: Password Policy Validator ---")
    while True:
        username = input("Enter a new username: ").strip()
        password = input("Enter a new password: ")
        if username == "":
            print("username cannot be empty please try again.\n")
            continue

        if validate_password(password):
            print("password accepted. your account has been created")
            break

        print("Password rejected it must:")
        print(" - be at least 10 chracters long")
        print(" - contain at least 1 uppercase and 1 lowercase letter")
        print(" - contain at least 2 digits")
        print(f" - contain at least 1 symbol from: {' '.join(ALLOWED_SYMBOLS)} (no other symbols)")
        print(" - contain no spaces\n")


if __name__ == "__main__":
    main()