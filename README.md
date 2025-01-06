# JOIN LOUNGE
https://t.me/+BtLCoInVq5hjYTc1


# **Solana Wallet Balance Checker**

This Python script allows users to check the balance of multiple Solana wallets, convert the balance into USD, and log the results. It integrates with the Solana RPC API and uses the CoinGecko API to fetch the current price of SOL in USD.

---

## **Features**
- Retrieve SOL wallet balances from a list of wallets in a `.txt` file.
- Automatically fetch the current SOL price in USD.
- Log wallet balances and corresponding USD values to a file.
- Simple and user-friendly with clear error messages.

---

## **Requirements**

Before using the script, ensure you have the following installed:
1. Python 3.7 or later
2. Required Python libraries:
   - `solana`
   - `solders`
   - `requests`

Install the required libraries using:
```bash
pip install solana requests solders
```

---

## **Setup Instructions**

1. **Clone or download the repository.**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Prepare the required files:**
   - **`endpoint.txt`:** Add the Solana RPC endpoint URL (e.g., https://api.mainnet-beta.solana.com).
   - **Wallet file (e.g., `wallets.txt`):** A `.txt` file containing wallet addresses in the format:
     ```
     wallet1|privatekey1
     wallet2|privatekey2
     ```
     Note: Private keys are optional and not used in this script.

3. **Set up the logging directory:**
   Create a folder named `data` in the root directory. This will store the log file (`log_balance.txt`).

---

## **Usage**

1. **Run the script:**
   Execute the script using Python:
   ```bash
   python solana_wallet_checker.py
   ```

2. **Provide the file path:**
   When prompted, input the path to your wallet file:
   ```
   Enter the path to the txt file (format: wallet|privatekey): wallets.txt
   ```

3. **View the results:**
   - The script will display the wallet balances and USD values in the console.
   - It will also save the results in `data/log_balance.txt`.

---

## **Example Output**

### **Console Output:**
```
Wallet: WalletAddress1, Token Amount: 10.5 SOL, Price in USD: 245.25 USD
Wallet: WalletAddress2, Token Amount: 0.02 SOL, Price in USD: 0.47 USD
```

### **Log File Output (log_balance.txt):**
```
Wallet: WalletAddress1, Token Amount: 10.5 SOL, Price in USD: 245.25 USD
Wallet: WalletAddress2, Token Amount: 0.02 SOL, Price in USD: 0.47 USD
```

---

## **Error Handling**

The script handles the following errors:
1. **Missing `endpoint.txt`:** Displays an error if the endpoint file is not found.
2. **Invalid wallet file path:** Prompts if the specified file path is incorrect.
3. **Connection errors:** Notifies users if there is an issue with fetching data from Solana RPC or CoinGecko.

---

## **Contributing**

Feel free to contribute by:
1. Submitting issues or feature requests.
2. Creating pull requests to improve functionality or fix bugs.

---

## **License**

This project is licensed under the MIT License. See the LICENSE file for details.

