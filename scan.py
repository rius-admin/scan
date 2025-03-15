#!/usr/bin/env python

import requests
from urllib.parse import urljoin
import os
from colorama import init, Fore, Style
from concurrent.futures import ThreadPoolExecutor

# Inisialisasi colorama
init(autoreset=True)

def clear_screen():
    """Membersihkan layar terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def scan_path(base_url, path):
    """Memindai satu path dan mengembalikan hasilnya."""
    full_url = urljoin(base_url, path)
    try:
        response = requests.get(full_url, timeout=5)
        if response.status_code == 200:
            return "{Fore.GREEN}[+] Path ditemukan: {full_url} (Status Code: {response.status_code}){Style.RESET_ALL}"
        else:
            return None
    except requests.exceptions.RequestException:
        return None

def scan_paths(base_url, path_file="path.txt", max_threads=13):
    """Membaca daftar path dari file dan melakukan scanning ke target website."""
    try:
        with open(path_file, "r") as file:
            # Menghapus spasi dan baris kosong
            paths = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("[!] File {path_file} tidak ditemukan.")
        return

    print("Memulai pemindaian path berdasarkan '{path_file}' di {base_url}...\n")
    
return f"{Fore.GREEN}[+] Path ditemukan: {full_url} (Status Code: {response.status_code}){Style.RESET_ALL}"
        results = executor.map(lambda path: scan_path(base_url, path), paths)
        for result in results:
            if result:
                print(result)

# Program utama
print (" ") 
print ("   terget.com ") 
clear_screen()
target_url = input("   scan > ").strip()

# Menambahkan skema (http://) jika belum ada
if not target_url.startswith("http://") and not target_url.startswith("https://"):
    target_url = "http://" + target_url

# Menambahkan tanda "/" di akhir URL jika belum ada
if not target_url.endswith('/'):
    target_url += '/'

print(f"Memulai pemindaian path berdasarkan '{path_file}' di {base_url}...\n")
