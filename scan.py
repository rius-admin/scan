#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import os

def clear_screen():
    """Membersihkan layar terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def crawl_and_scan(base_url):
    visited_urls = set()  # Set untuk melacak URL yang sudah dikunjungi
    to_visit_urls = [base_url]  # Mulai dengan URL utama (base_url)

    print("Memulai pemindaian dan crawling di {base_url}...\n")
    
    while to_visit_urls:
        current_url = to_visit_urls.pop(0)  # Ambil URL yang belum dikunjungi
        if current_url in visited_urls:
            continue  # Lewati URL yang sudah dikunjungi

        try:
            response = requests.get(current_url, timeout=10)  # Tambahkan timeout agar tidak menggantung
            if response.status_code == 200:
                print("[+] Path ditemukan: {current_url} (Status Code: {response.status_code})")
            else:
                print("[-] Path tidak ditemukan: {current_url} (Status Code: {response.status_code})")

            visited_urls.add(current_url)  # Tandai URL sebagai telah dikunjungi

            # Mengambil konten HTML dari halaman yang ditemukan
            soup = BeautifulSoup(response.text, 'html.parser')

            # Temukan semua link (tag <a>) dalam halaman
            for link in soup.find_all('a', href=True):
                next_url = urljoin(current_url, link['href'])  # Gabungkan dengan URL dasar
                parsed_url = urlparse(next_url)

                # Hanya proses link yang berada di domain yang sama
                if parsed_url.netloc == urlparse(base_url).netloc and next_url not in visited_urls:
                    to_visit_urls.append(next_url)  # Tambahkan ke daftar URL yang akan dikunjungi

        except requests.exceptions.RequestException as e:
            print("[!] Error saat memindai {current_url}: {e}")

# Meminta input dari pengguna untuk target URL
print (" ") 
clear_screen()
target_url = input("Masukkan target website (contoh: target.com): ").strip()

# Menambahkan skema (http://) dan domain yang valid
if not target_url.startswith("http://") and not target_url.startswith("https://"):
    target_url = "http://" + target_url

# Menambahkan tanda "/" di akhir URL jika belum ada
if not target_url.endswith('/'):
    target_url += '/'

# Mulai pemindaian dan crawling
crawl_and_scan(target_url)
