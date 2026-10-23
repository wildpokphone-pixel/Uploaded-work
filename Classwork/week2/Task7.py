# returns the next term in the series by adding the previous two terms 
def calculate_next_term(first: int, second: int) -> int:
    return first + second

def main():
    # how many terms to print
    term_count = 20

    # the two terms we are currently holding starting with 0 and 1 
    first = 0 
    second = 1

    print("FIBONACCI SERIES")

    # each time round the loop print the first term then move both terms along
    for term in range(term_count):
        print(first, end="")

        #add a comma between terms but not after the last one 
        if term < term_count -1:
            print(",", end="")

        next_term = calculate_next_term(first, second)
        first = second
        second = next_term
    # print a new line at the end 
    print()

#only run main() when this file is run directly not when imported
if __name__ == "__main__":
    main()