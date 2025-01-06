from solana.rpc.api import Client
from solders.pubkey import Pubkey
import os
import requests

# Fungsi untuk mendapatkan harga SOL dalam USD
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

# Membaca URL endpoint dari file endpoint.txt
def get_endpoint():
    try:
        with open("endpoint.txt", "r") as endpoint_file:
            endpoint_url = endpoint_file.readline().strip()
            return endpoint_url
    except FileNotFoundError:
        print("File endpoint.txt tidak ditemukan.")
        return None
    except Exception as e:
        print("Terjadi kesalahan saat membaca endpoint:", e)
        return None

# Mendapatkan URL endpoint dari file endpoint.txt
endpoint_url = get_endpoint()

if endpoint_url:
    # Inisialisasi klien Solana dengan URL dari endpoint.txt
    solana_client = Client(endpoint_url)

    # Meminta pengguna untuk menentukan file txt
    file_path = input("Masukkan path file txt (format: wallet|privatekey): ")

    # Path untuk menyimpan log
    log_file_path = os.path.join("data", "log_balance.txt")

    # Dapatkan harga SOL saat ini dalam USD
    sol_price_in_usd = get_sol_price()

    if sol_price_in_usd:
        try:
            # Membaca wallet dari file
            with open(file_path, 'r') as file:
                lines = file.readlines()

            # Membuka file log untuk menulis hasil
            with open(log_file_path, 'a') as log_file:
                for line in lines:
                    # Mengambil wallet dari format wallet|privatekey
                    wallet = line.split('|')[0].strip()

                    # Mengubah string wallet menjadi Pubkey
                    pubkey = Pubkey.from_string(wallet)

                    # Mendapatkan saldo
                    balance_result = solana_client.get_balance(pubkey)

                    # Memeriksa apakah hasilnya valid
                    if balance_result.value is not None:
                        balance_in_sol = balance_result.value / 1_000_000_000
                        balance_in_usd = balance_in_sol * sol_price_in_usd
                        log_message = f"Wallet: {wallet}, Jumlah Token: {balance_in_sol} SOL, Harga dalam USD: {balance_in_usd:.2f} USD\n"
                        print(log_message.strip())  # Cetak ke konsol
                        log_file.write(log_message)  # Simpan ke file log
                    else:
                        error_message = f"Error retrieving balance for {wallet}: {balance_result}\n"
                        print(error_message.strip())  # Cetak ke konsol
                        log_file.write(error_message)  # Simpan ke file log

        except FileNotFoundError:
            print("File tidak ditemukan. Pastikan path file yang dimasukkan benar.")
        except Exception as e:
            print("Terjadi kesalahan:", e)
    else:
        print("Tidak dapat mendapatkan harga SOL dalam USD. Program berhenti.")
else:
    print("Tidak dapat membaca endpoint URL dari file. Program berhenti.")
