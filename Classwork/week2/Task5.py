# returns the result of mutiplying the number by the mutiplier 
def calculate_product(number: int, multiplier: int) -> int:
    return number * multiplier

def main():
    # the table runs from 1 up to 10 
    start = 1
    end = 10

    # ask the user for the number to build the table for
    number = int(input("etner a number: ")) 

    print(f"\nMUTIPLICATION TABLE FOR {number}")

    #l oop through each mutiplier from 1 to 10 range stops at the last number so add 1
    for multiplier in range(start, end + 1):
        results = calculate_product(number, multiplier )
        print(f"{number} x {multiplier} = {results}")

# only run main() when this file is run directly not when imported
if __name__ == "__main__":
    main()