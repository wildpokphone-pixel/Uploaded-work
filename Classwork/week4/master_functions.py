import secrets
import string

def random_string(size:int=10) -> str:
    #create a pool to pick ascii characters from 
    pool = string.ascii_letters + string.digits
    some_str = "".join(secrets.choice(pool) for _ in range(size))
    return some_str

def generate_custom_email(full_name: str, domain: str) -> str:
    """
    Genereates an email address in the format:
    [first_inital][lastname][random_number]@helpme.net
    the random number is between 8 adn 121 (inclusive).
    """

    # Split the full name into words, for example ["bob", "carter"].
    name_parts = full_name.lower().split()


    #check that we have two names
    if len(name_parts)<2:
        #handle cases where input dosent have a first and last name
        raise ValueError(
            "input string must contain at least a first and a last name separated by a space"
        )

    first_name=name_parts[0]
    last_name=name_parts[-1]

    #extract the first inital
    first_inital = first_name[0]
        
    #generate a random number between 8 and 121 (inclusive)
    random_num = secrets.randbelow(114) + 8

    #assemble and return the final email string
    email =f"{first_inital}{last_name}{random_num}{domain}"

    return email

def display_ip_addresses(*ips) :
    list_of_ipda = ips[0]
    print(*list_of_ipda, sep="\n")

def display_all_Accounts(**accounts):
    for key, value in accounts.items():
        print(key, value)

def main():
    print(random_string())
    print(random_string(16))
    print(generate_custom_email(full_name="Frank Abagnale", domain="@trustme.org"))
    print(generate_custom_email(domain="@scrapmetal.org", full_name="victor lustig"))

    ips = ["192.168.1.2", "10.0.0.1", "172.125.25.12", "192.158.1.256"]
    display_ip_addresses(ips)
    display_all_Accounts(uid1="alice", uid2="bob", uid3="Charlie")


if __name__ == "__main__":
    main()