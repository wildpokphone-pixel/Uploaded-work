#CHaracter Analysis and libaries

import random
from datetime import datetime
import socket
def analyse_code(device_code: str) -> None:
    #Check individual characters in a device code

    #process the string one chracter at a time
    for character in device_code:
        if character.isdigit():
            print(f"Number found: {character}")
        if character.isupper():
            print(f"Uppercase character is found: {character}")

def create_analysis_details() -> None:
    #create and display details for the analysis

    #generate a random four digit analysis ID
    analysis_id = random.randint(1000,9999)

    #get the current date and time
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("\n--- Analysis Details ---")
    print(f"Analysis ID: {analysis_id}")
    print(f"Timestamp: {timestamp}")

def get_local_ip() -> str:
    #return the computers local IP address

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))

    ip_address = s.getsockname()[0]
    s.close()

    return ip_address
def main() -> None:
    #run the program

    device_code = "RTR2048gla"
    analyse_code(device_code)
    create_analysis_details()

    ip_address = get_local_ip()

    print("\n--- Network Details ---")
    print(f"local IP address: {ip_address}")


if __name__ == "__main__":
    main()