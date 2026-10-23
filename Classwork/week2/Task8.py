# return part as a percentage of total
def calculate_percentage(part: int, total: int) -> float:
    if total == 0:
        return 0.0
    return (part / total) * 100

# return true if both the username and password match the stored credentials
def check_credentials(username: str, password: str, correct_username: str, correct_password: str) -> bool:
    return username == correct_username and password == correct_password

# print the security menu
def display_menu() -> None:
    print("\nSECURITY MENU")
    print("1. security event counter")
    print("2. brute-force simulator")
    print("3. login authentication")
    print("4. Exit")

# ask for username and password until they are correct or the maximum failed logins is reached
# returns true if authentication succeeded, false if the account is frozen
def login_authentication(correct_username: str, correct_password: str, max_failed: int) -> bool:
    failed_logins = 0

    while failed_logins < max_failed:
        username = input("enter username: ")
        password = input("enter password: ")

        if check_credentials(username, password, correct_username, correct_password):
            print("Authentication succeeded")
            return True

        failed_logins += 1
        print(f"authentication failed. failed logins: {failed_logins} of {max_failed}")

    print("account is frozen for 24 hours")
    return False

# ask for a password a set number of times and counts correct and incorrect entries
def security_event_counter(correct_password: str, total_attempts: int, alert_percentage: float) -> None:
    correct_count = 0
    incorrect_count = 0

    print("\nSECURITY EVENT COUNTER")

    for attempt in range(1, total_attempts + 1):
        entered_password = input(f"attempt {attempt} of {total_attempts} - enter password: ")

        if entered_password == correct_password:
            correct_count += 1
        else:
            incorrect_count += 1

    incorrect_percentage = calculate_percentage(incorrect_count, total_attempts)

    print(f"correct passwords: {correct_count}")
    print(f"incorrect passwords: {incorrect_count}")
    print(f"Percentage incorrect: {incorrect_percentage:.1f}%")

    # Raise an alert if more than half of the entries were wrong
    if incorrect_percentage > alert_percentage:
        print("ALERT: more than 50 percent of the passwords entered were incorrect")

#lets the user guess a predefinded password stopping when correct or when the attempts run out
def brute_force_simulation(predefined_password: str, max_attempts: int) -> None:
    attempts = 0
    guessed = False

    print("\nBRUTE-FORCE SIMULATION")

    # keep going until the password is guessed or no attempts are left
    while attempts < max_attempts and not guessed:
        guess = input(f"attempt {attempts + 1} of {max_attempts} - guess the password: ")
        attempts += 1

        if guess == predefined_password:
            guessed = True
            print(f"password guessed correctly in {attempts} attempt(s).")
        elif attempts >= max_attempts:
            print(f"maximum attempts ({max_attempts}) reached. password not guessed")

def main():
    # stored credentials are settings used by the tool
    correct_username = "Admin"
    correct_password = "Secure123"
    max_failed_logins = 3
    event_attempts = 10
    alert_percentage = 50.0
    brute_force_max_attempts = 5

    # the user must authenticate before the menu is shown
    print("AUTHENTICATION REQUIRED")
    authenticated = login_authentication(correct_username, correct_password, max_failed_logins)

    # of the account is frozen the program ends without showing the menu
    if not authenticated:
        return

    #keep showing the menu until the user chooses Exit
    running = True
    while running:
        display_menu()
        choice = input("select an option (1-4): ")

        if choice == "1":
            security_event_counter(correct_password, event_attempts, alert_percentage)
        elif choice =="2":
            brute_force_simulation(correct_password, brute_force_max_attempts)
        elif choice =="3":
            print("\nLOGIN AUTHENTICATION")
            login_authentication(correct_username, correct_password, max_failed_logins)
        elif choice == "4":
            print("thank you for using the security tool")
            running = False
        else:
            print("invalid choice please enter a number from 1 to 4")

#only run main() when this file is run directly not when imported
if __name__ == "__main__":
    main()