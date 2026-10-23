"""Security event string analysis tutorial: find key words and an IP address."""

EVENT = ("Security Alert: Failed login attempt detected from IP address "
         "192.168.1.25. the user account admin was targeted at 22:45. "
         "the server blocked the login attempt after an incorrect password "
         "was entered.")


def extract_ip(event: str) -> str:
    # extract the ip address that follows the text "ip address"

    # lower() makes the search ignore upper and lower case differences
    marker = "ip address "
    position = event.lower().find(marker)

    # find() returns -1 when the text is not found
    if position == -1:
        return "Not found"

    # slice from the end of the marker, then take the first word
    rest = event[position + len(marker):]
    return rest.split()[0].rstrip(".")


def analyse_event(event: str) -> None:
    # analyse information contained in a security event

    # lower() so "Failed", "failed" and "FAILED" are all detected
    failed = "failed" in event.lower()
    login = "login" in event.lower()
    ip_address = extract_ip(event)

    print("Security Event Analysis")
    print("------------------------")
    print(f"Failed event: {'Yes' if failed else 'No'}")
    print(f"Login event: {'Yes' if login else 'No'}")
    print(f"IP Address: {ip_address}")

    # show a message for each finding
    if failed:
        print("Warning: A failed security event was detected.")
    if login:
        print("Login activity detected.")
    if failed and login:
        print("Action: Investigate the failed login attempt.")


def main() -> None:
    # run the program
    analyse_event(EVENT)


if __name__ == "__main__":
    main()