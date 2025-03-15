import requests
import os
from urllib.parse import urljoin

def clear_screen():
    """Membersihkan layar terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def scan_path(base_url, path):
    """Memindai satu path dan mengembalikan hasilnya."""
    full_url = urljoin(base_url, path)
    try:
        response = requests.get(full_url, timeout=5)
        if response.status_code == 200:
            print(f"[+] Path ditemukan: {full_url} (Status Code: {response.status_code})")
    except requests.exceptions.RequestException:
        pass

def scan_paths(base_url, path_file="path.txt"):
    """Membaca daftar path dari file dan melakukan scanning ke target website."""
    if not os.path.exists(path_file):
        print(f"[!] File {path_file} tidak ditemukan.")
        return

    with open(path_file, "r") as file:
        paths = [line.strip() for line in file if line.strip()]

    print(f"Memulai pemindaian path dari '{path_file}' di {base_url}...\n")
    for path in paths:
        scan_path(base_url, path)

# Program utama
clear_screen()
print("Target: contoh.com") 
target_url = input("Scan > ").strip()

# Menambahkan skema (http://) jika belum ada
if not target_url.startswith(("http://", "https://")):
    target_url = "http://" + target_url

# Menambahkan tanda "/" di akhir URL jika belum ada
if not target_url.endswith('/'):
    target_url += '/'

scan_paths(target_url)
