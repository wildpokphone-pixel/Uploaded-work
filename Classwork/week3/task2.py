#Password policy validator tutorial keep asking unitl vali 

#the only symbols the policy allows
allowed_symbols = "!@#$%"


def check_policy(password: str) -> list[str]:
    #check a password against the policy

    errors = []

    #count each type of character
    upper = sum(1 for c in password if c.isupper())
    lower = sum(1 for c in password if c.islower())
    digits = sum(1 for c in password if c.isdigit())
    good_symbols = sum(1 for c in password if c in allowed_symbols)

    #find symbols that are not on the allowed list
    bad_symbols = [c for c in password
                   if not c.isalnum() and c not in allowed_symbols and c != " "]

    #check each rule in the policy
    if len(password) < 10:
        errors.append("must contain at least 10 characters long.")
    if upper < 1:
        errors.append("Must contain at least 1 uppercase character")
    if lower < 1:
        errors.append("Must contain at least 1 lowercase character")
    if digits < 2:
        errors.append("Must contain at least 2 digits")
    if good_symbols < 1:
        errors.append("Must contain at least 1 symbol from: ! @ # $ %")
    if bad_symbols:
        errors.append(f"Contains disallowed symbols: {''.join(sorted(set(bad_symbols)))}")
    if " " in password:
        errors.append(" Must not contain spaces")

    return errors
def main() -> None:
    # run the program
    # keep asking until password follows policy
    while True:
        password = input("Create a new password: ")
        errors = check_policy(password)

        if not errors:
            print("Password accepted")
            break

        # reject the password and explain what needs fixing
        print("Password rejected:")
        for error in errors:
            print(f" - {error}")
        print()


if __name__ == "__main__":
    main()