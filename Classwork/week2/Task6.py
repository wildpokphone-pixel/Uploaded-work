# returns true if the password entered matches the correct password
def is_correct_password(password: str, correct_password: str) -> bool:
    return password == correct_password


def main():
    # the password the user needs to enter
    correct_password = "python123"

    # ask for the password for the first time
    entered_password = input("enter the password: ")

    # keep asking while the password is incorrect
    while not is_correct_password(entered_password, correct_password):
        print("incorrect password, try again")
        entered_password = input("enter the password: ")

    # the loop only ends when the correct password is entered
    print("access granted")

# only run main() when this file is run directly not when imported
if __name__ == "__main__":
    main()