# Returns how many full gross eggs are in the total, and the eggs left over
def split_into_gross(total_eggs: int, gross_size: int) -> tuple[int, int]:
    gross = total_eggs // gross_size
    remaning_eggs = total_eggs % gross_size
    return gross, remaning_eggs 

# Returns how many full dozen eggs are in the eggs left over and single eggs left after that
def split_into_dozen(remaining_eggs: int, dozen_size: int) -> tuple[int, int]:
    dozen = remaining_eggs // dozen_size
    single_eggs = remaining_eggs % dozen_size
    return dozen, single_eggs 

def main():
    # number of eggs in one gross in one dozen
    gross_size = 144
    dozen_size = 12

    # ask the user for a whole number of eggs
    total_eggs = int(input("enter the total number of eggs : "))

    # split into gross first then split what is left into dozen and single eggs
    gross, remaining_eggs = split_into_gross(total_eggs, gross_size)
    dozen, single_eggs = split_into_dozen(remaining_eggs, dozen_size)

    print(f"{total_eggs} eggs is {gross} gross eggs + {dozen} dozen eggs + {single_eggs} single eggs")    

# only run main() when this file is run directly not when imported
if __name__ == "__main__":
    main()
