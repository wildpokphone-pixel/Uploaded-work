#String analysis tutorial analyse URLS and assets ids.


def analyse_url(url: str) -> None:
    # analyse information contained in a url

    print("\n--- URL Analysis ---")
    print(f"URL: {url}")

    # check the start of the url
    if url.startswith("https://"):
        print("HTTPS detected - connection is encrypted.")
    elif url.startswith("http://"):
        print("HTTP detected - connection is not encrypted.")
    else:
        print("URL protocol not recognised")

    if "admin" in url:
        print("Admin area detected.")
    if url.endswith("/docs"):
        print("Documentation page detected")
def analyse_asset(asset_id: str) -> tuple[str, str, str]:
    # analyse an asset ID and return its separate parts

    print("\n--- Asset Analysis ---")
    print(f"Asset ID: {asset_id}")

    # split the asset id into separate parts
    parts = asset_id.split("-")

    asset_type = parts[0]
    asset_number = parts[1]
    location = parts[2].upper()

    #check that the asset number contains only digits
    if asset_number.isdigit():
        print("Asset number is numeric.")
    else:
        print("Asset number is not numeric")
    #return the processed asset information
    return asset_type, asset_number, location

def main() -> None:
    # run the program
    # replace these fixed values with user input
    url = input("Enter a URL: ")
    asset_id = input("Enter an asset ID: ")
    analyse_url(url)

    asset_type, asset_number, location = analyse_asset(asset_id)
    print(f"Asset type: {asset_type}")
    print(f"Asset number: {asset_number}")
    print(f"Location: {location}")


if __name__ == "__main__":
    main()