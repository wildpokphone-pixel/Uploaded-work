# Password analysis tutorial: counts the character types in a password


def analyse_password(password: str) -> tuple[int, int, int, int]:
    """Analyse a password and return counts for uppercase, lowercase, numbers, and symbols."""

    upper = 0
    lower = 0
    numbers = 0
    symbols = 0

    for ch in password:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
        elif ch.isdigit():
            numbers += 1
        else:
            # Anything that is not a letter or a digit is treated as a symbol.
            symbols += 1

    return upper, lower, numbers, symbols


def main() -> None:
    password = input("Enter your password: ")

    upper, lower, numbers, symbols = analyse_password(password)

    print(f"Password length: {len(password)}")
    print(f"Uppercase: {upper}")
    print(f"Lowercase: {lower}")
    print(f"Numbers: {numbers}")
    print(f"Symbols: {symbols}")


if __name__ == "__main__":
    main()