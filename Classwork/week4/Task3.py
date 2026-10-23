def calculate_failed_percentage(failed: int, total: int) -> float:
    """
    failed percentage = failed login / total login attempts x 100
    raises zeroDivisionError if total is 0
    """
    return (failed / total) * 100

def classify_risk(percentage: float) -> str:
    """Maps a failed login percentage to a risk level"""

    if percentage >= 50:
        return "HIGH RISK"
    elif percentage >= 25:
        return "MEDIUM RISK"
    else:
        return "LOW RISK"

def main():
    print("--- Task 3: Failed login risk calc ---")
    try: 
        failed = int(input("Enter the number of failed loging attempts: "))
        total = int(input("Enter the total number of login attempts: "))

        if failed < 0 or total < 0:
            raise ValueError("NEgative numbers are not allowed")
            #a zero total rasies ZeroDivisionError here before any other check
        percentage = calculate_failed_percentage(failed, total)

        if failed > total:
            raise ValueError("Failed attempts cannot exceed total attempts")
        print(f"Failed login percentage: {percentage:.2f}%")
        print(f"Risk level: {classify_risk(percentage)}")
    except ValueError:
        print("Please eneter numbers only (whole numbers, failed <= total, no negatives).")
    except ZeroDivisionError:
        print("Total login attempts cannot be zero.")

if __name__ == "__main__":
   main()