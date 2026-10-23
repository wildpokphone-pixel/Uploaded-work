# returns true if the number is even, divides by 2 with nothing left over
def is_even(num: int) -> bool:
    return num % 2 == 0

def main():
    #lowest and highest numbers allowed
    minimum = 1
    maximum = 100

    # ask the user for a whole number 
    number = int(input("enter a whole number between 1 and 100: "))

    # check the range first, then check odd or even 
    if number < minimum:
        print(f"Error: {number} is too low the number must be between {minimum} and {maximum}")
    elif number > maximum:
        print(f"Error: {number} is too high the number must be between {minimum} and {maximum}")
    elif is_even(number):
        print(f"{number} is an even number")
    else: 
        print(f"{number} is an odd number")

# only run main() when this file is run directly not when imported
if __name__ == "__main__":
    main()  