from solana.rpc.api import Client
from solders.pubkey import Pubkey
import os
import requests

# Function to get the price of SOL in USD
def get_sol_price():
    try:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd")
        if response.status_code == 200:
            data = response.json()
            return data["solana"]["usd"]
        else:
            print("Error fetching SOL price.")
            return None
    except Exception as e:
        print("Error fetching SOL price:", e)
        return None

# Read the endpoint URL from the file endpoint.txt
def get_endpoint():
    try:
        with open("endpoint.txt", "r") as endpoint_file:
            endpoint_url = endpoint_file.readline().strip()
            return endpoint_url
    except FileNotFoundError:
        print("The file endpoint.txt was not found.")
        return None
    except Exception as e:
        print("An error occurred while reading the endpoint:", e)
        return None

# Get the endpoint URL from the file endpoint.txt
endpoint_url = get_endpoint()

if endpoint_url:
    # Initialize the Solana client with the URL from endpoint.txt
    solana_client = Client(endpoint_url)

    # Prompt the user to specify the txt file
    file_path = input("Enter the path to the txt file (format: wallet|privatekey): ")

    # Path to save the log
    log_file_path = os.path.join("data", "log_balance.txt")

    # Get the current price of SOL in USD
    sol_price_in_usd = get_sol_price()

    if sol_price_in_usd:
        try:
            # Read wallets from the file
            with open(file_path, 'r') as file:
                lines = file.readlines()

            # Open the log file to write the results
            with open(log_file_path, 'a') as log_file:
                for line in lines:
                    # Extract the wallet from the format wallet|privatekey
                    wallet = line.split('|')[0].strip()

                    # Convert the wallet string to Pubkey
                    pubkey = Pubkey.from_string(wallet)

                    # Get the balance
                    balance_result = solana_client.get_balance(pubkey)

                    # Check if the result is valid
                    if balance_result.value is not None:
                        balance_in_sol = balance_result.value / 1_000_000_000
                        balance_in_usd = balance_in_sol * sol_price_in_usd
                        log_message = f"Wallet: {wallet}, Token Amount: {balance_in_sol} SOL, Price in USD: {balance_in_usd:.2f} USD\n"
                        print(log_message.strip())  # Print to the console
                        log_file.write(log_message)  # Save to the log file
                    else:
                        error_message = f"Error retrieving balance for {wallet}: {balance_result}\n"
                        print(error_message.strip())  # Print to the console
                        log_file.write(error_message)  # Save to the log file

        except FileNotFoundError:
            print("File not found. Make sure the file path entered is correct.")
        except Exception as e:
            print("An error occurred:", e)
    else:
        print("Unable to retrieve the price of SOL in USD. Program stopped.")
else:
    print("Unable to read the endpoint URL from the file. Program stopped.")
