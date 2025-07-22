import sys
import requests

def main():
    if len(sys.argv) == 2:
        try:
            n = float(sys.argv[1])
            print(btc_price(n))
        except ValueError:
            sys.exit("Command-line argument is not a number")
    else:
        sys.exit("Missing command-line argument")

def btc_price(num):
    try:
        response = requests.get(f"https://rest.coincap.io/v3/assets/bitcoin?apiKey=8d52b5cbc12038e7caa0c432f61956200a23d3cdd9d22912ac6ae1c4a57522af")
        result = response.json()
        price = float(result["data"]["priceUsd"])
        total = price * num
        return f"${total:,.4f}"
    except requests.RequestException:
        return None

main()


