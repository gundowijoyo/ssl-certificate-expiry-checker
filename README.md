# SSL Certificate Expiry Checker

### Deskripsi
Proyek ini adalah program Python yang digunakan untuk memeriksa masa berlaku (kedaluwarsa) dari sertifikat SSL/TLS sebuah domain. Program ini akan mengambil informasi dari sertifikat SSL yang diterbitkan oleh situs dan menampilkan tanggal kedaluwarsa sertifikat tersebut.

### Cara Kerja
1. Program akan meminta pengguna untuk memasukkan domain yang ingin diperiksa.
2. Menggunakan socket dan SSL, program akan mencoba membuat koneksi ke server melalui port 443 (port standar untuk HTTPS).
3. Program kemudian akan mengambil sertifikat SSL dan menampilkan tanggal kedaluwarsa sertifikat tersebut.

### Fitur
- Memeriksa sertifikat SSL dari sebuah domain.
- Menampilkan tanggal kedaluwarsa sertifikat SSL yang digunakan oleh domain tersebut.

### Instalasi
Tidak perlu menginstal pustaka eksternal, karena program ini menggunakan pustaka standar Python seperti `ssl`, `socket`, dan `datetime`.

### Penggunaan
1. Jalankan program.
2. Masukkan domain (misalnya `example.com`).
3. Program akan menampilkan tanggal kedaluwarsa sertifikat SSL dari domain tersebut.

### Contoh Penggunaan
```
Masukkan domain untuk memeriksa sertifikat SSL: example.com
Sertifikat SSL untuk example.com akan kedaluwarsa pada: 2025-12-31 23:59:59
```

### Kode Program
```python
import ssl
import socket
from datetime import datetime

def check_ssl_expiry(domain):
    port = 443
    context = ssl.create_default_context()
    with socket.create_connection((domain, port)) as sock:
        with context.wrap_socket(sock, server_hostname=domain) as ssock:
            cert = ssock.getpeercert()
            expiry_date = cert['notAfter']
            expiry_date = datetime.strptime(expiry_date, "%b %d %H:%M:%S %Y GMT")
            return expiry_date

def main():
    domain = input("Masukkan domain untuk memeriksa sertifikat SSL: ")
    expiry_date = check_ssl_expiry(domain)
    print(f"Sertifikat SSL untuk {domain} akan kedaluwarsa pada: {expiry_date}")

if __name__ == "__main__":
    main()
```

### Penjelasan Kode
1. **check_ssl_expiry(domain)**: Fungsi ini membuat koneksi SSL ke domain pada port 443, kemudian mengambil informasi sertifikat dan mengembalikan tanggal kedaluwarsa.
2. **main()**: Fungsi utama yang meminta input domain dari pengguna dan memanggil fungsi `check_ssl_expiry` untuk menampilkan tanggal kedaluwarsa sertifikat SSL.

### Catatan
- Pastikan domain yang dimasukkan memiliki sertifikat SSL/TLS yang valid.
- Program hanya memeriksa sertifikat yang terpasang pada port 443 (HTTPS).
