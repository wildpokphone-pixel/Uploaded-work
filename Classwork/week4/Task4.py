def validate_ip(ip: str) -> bool:
    """
    basic ipv4 format check:
    exactly three dots giving four parts 
    every part is digits only and between 0 and 255
    """
    #remove leading/ trailing whitespace
    ip = ip.strip()

    if "." not in ip:
        return False

    parts = ip.split(".")
    if len(parts) != 4:
        return False

    for part in parts:
        #reject empty parts letter negative signs
        if not part.isdigit():
            return False

        number = int(part)
        if number < 0 or number > 255:
            return False
    return True

def main():
    ip_Address = input("Enter an ip address: ")

    if validate_ip(ip_Address):
        print("Valid IP address")
    else:
        print("Invalid IP address")

if __name__ =="__main__":
    main()