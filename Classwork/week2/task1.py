# Returns the sum of the two values 
def calculate_sum(first_value: float, second_value: float) -> float:
    return first_value + second_value

# Returns the product of the two values
def calculate_product(first_value: float, second_value: float) -> float:
    return first_value * second_value

# Returns the second value subtracted from the first value 
def calculate_diffrence(first_value: float, second_value: float) -> float:
    return first_value - second_value 

#Returns the first value divided by the second value normal division 
def calculate_division(first_value: float, second_value: float) -> float:
    return first_value / second_value

# Returns the first value divided by the second value using interger division
def calculate_interger_division(first_value: float, second_value: float) -> float:
    return first_value // second_value

# Returns the remainder of the first value divided by the second value
def calculate_modulus(first_value:float, second_value: float) -> float:
    return first_value % second_value

# Returns the first value raised to the power of the second value 
def calculate_power(first_value: float, second_value: float) -> float:
    return first_value ** second_value 

def main():
    # Ask the user for two values and convert them to numbers
    first_value = float(input("enter the first value: "))
    second_value = float(input("enter the second value: "))

    # Operations that are always safe to run
    print("\nRESULTS")
    print(f"Sum: {calculate_sum(first_value, second_value)}")
    print(f"Prodcut: {calculate_product(first_value, second_value)}")
    print(f"Diffrence: {calculate_diffrence(first_value, second_value)}")

    # Dividing by zero cuases an error, so check the second value first 
    if second_value == 0:
        print("Division: Cannot divide by zero")
        print("Interget division: Cannot divide by zero")
        print("Modulus: cannot divide by zero")
    else:
        print(f"division: {calculate_division(first_value, second_value)}")
        print(f"interger division: {calculate_interger_division(first_value, second_value)}")
        print(f"modulus: {calculate_modulus(first_value, second_value)}")

    # Power is safe to run for any values entered 
    print(f"Power: {calculate_power(first_value, second_value)}")

# only run main() when this file is run directly not when imported
if __name__ == "__main__":
    main()