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
  
