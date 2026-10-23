# Converts GMT hours to another time zone using the offset, wrapping around the 24 hour clock
def convert_hour(gmt_hour: int, offset: int) -> int:
    return (gmt_hour + offset) % 24 

# Formats hours and minutes as a 24-hour clock string
def format_time(hour: int, minute: int) -> str:
    return f"{hour:02d}: {minute:02d}"

def main():
    # offsets from GMT in hours
    pst_offset = -8
    cet_offset = 1
    
    # ask the user for the GMT time using the 24 hour clock 
    gmt_hour = int(input("enter the GMT hour(0-23): "))
    gmt_minute = int(input("enter the GMT minute(o-59: "))

    # convert the hour for each time zone
    pst_hour = convert_hour(gmt_hour, pst_offset)
    cet_hour = convert_hour(gmt_hour, cet_offset)

    print("\nTIME ZONES")
    print(f"GMT: {format_time(gmt_hour, gmt_minute)}")
    print(f"PST: {format_time(pst_hour, gmt_minute)}")
    print(f"CET: {format_time(cet_hour, gmt_minute)}")

# only run main() when this file is run directly not when imported
if __name__ == "__main__":
    main()
