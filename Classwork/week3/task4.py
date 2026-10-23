#Security event logger log every logina ttempt until logins succeeds 

import random
import socket 
from datetime import datetime

#demo credendtials
valid_username = "admin"
valid_password = "secure#2026"


def get_ip() -> str:
    #get the ip address of this system 

    try: 
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #no data is sent this is just to find the address used for outside traffic
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
        return ip_address
    except OSError:
        #fall back to localhost when there is no network connection
        return "127.0.0.1"

def log_event(username: str, success: bool) -> None:
    #print one event log entry for a login attempt

    event_id = random.randint(1000, 9999)
    event = "successful login" if success else "failed login"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"Event ID: {event_id}")
    print(f"Username: {username}")
    print(f"IP Address: {get_ip()}")
    print(f"Event: {event}")
    print(f"timestamp: {timestamp}")
    print()

def main() -> None:
    #run the program
    print("SECURITY EVENT LOG")
    print("==================")

    #keep asking until correct username and password are entered
    while True:
        username = input("Username: ")
        password = input("Password: ")

        success = username == valid_username and password == valid_password

        #log every attmept, failed or successful
        log_event(username, success)

        if success:
            break


if __name__ == "__main__":
    main()