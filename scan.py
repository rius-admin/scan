#!/usr/bin/env python

import requests
from urllib.parse import urljoin
import os

def clear_screen():
    """Membersihkan layar terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def scan_paths(base_url, path_file="path.txt"):
    """Membaca daftar path dari file dan melakukan scanning ke target website."""
    try:
        with open(path_file, "r") as file:
            # Menghapus spasi dan baris kosong
            paths = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"[!] File {path_file} tidak ditemukan.")
        return

    print(f"Memulai pemindaian path berdasarkan '{path_file}' di {base_url}...\n")
    for path in paths:
        # Gabungkan base_url dengan path yang dibaca dari file
        full_url = urljoin(base_url, path)
        try:
            response = requests.get(full_url, timeout=10)
            if response.status_code == 200:
                print("[+] Path ditemukan: {full_url} (Status Code: {response.status_code})")
            else:
                print("[-] Path tidak ditemukan: {full_url} (Status Code: {response.status_code})")
        except requests.exceptions.RequestException as e:
            print("[!] Error saat memindai {full_url}: {e}")

# Main program
clear_screen()
target_url = input("Masukkan target website (contoh: target.com): ").strip()

# Menambahkan skema (http://) jika belum ada
if not target_url.startswith("http://") and not target_url.startswith("https://"):
    target_url = "http://" + target_url

# Menambahkan tanda "/" di akhir URL jika belum ada
if not target_url.endswith('/'):
    target_url += '/'

# Mulai pemindaian path berdasarkan file path.txt
scan_paths(target_url)
