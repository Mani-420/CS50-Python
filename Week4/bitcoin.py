import sys
import requests

def main():
    length = check()
    float_number = to_float(sys.argv[1])
    bitcoin = to_bitcoin(float_number)
    print(f"${bitcoin:,.4f}")

def check():
    if len(sys.argv) == 0:
        sys.exit("Missing command-line argument")

def to_float (value):
    try:
        floating_number = float(value)
        return floating_number
    except ValueError:
        sys.exit("Command-line argument is not a number")

def to_bitcoin(number):
    try:
        # Fetch the current price of Bitcoin in USD
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()

        btc_price = data["bpi"]["USD"]["rate_float"]
        bitcoin = number * btc_price
        return bitcoin

    except requests.RequestException:
        sys.exit("Error fetching Bitcoin price.")

if __name__ == "__main__":
    main()