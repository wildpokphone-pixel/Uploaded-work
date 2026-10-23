def authenticate(username:str,password:str) -> bool:
    """Returns true only if both username and password match the stored credentials"""
    return username == "admin" and password == "admin123"


def main():
    print("--- Task 2: login Authentication ---")
    while True:
        try:
            username = input("Username: ").strip()
            password = input("Password: ").strip()
 
            #treat empty input as invalid input
            if username == "" or password == "":
                raise ValueError("Username and password cannot be empty.")
 
            if authenticate(username, password):
                print("Login successful")
                break
 
            print("Invalid username or password\n") 
 
        except ValueError as error:
            print(f"Invalid input: {error}\n")
        except EOFError:
            print("\nNo input received exiting login")
            break
 
if __name__ == "__main__":
    main()