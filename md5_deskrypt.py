import requests


print("-" * 26)
print("MD5".center(26," "))
print("DESCRYPTOR".center(26," "))
print("Created : By JKresna".center(26," "))
print("-" * 26)
print("\n")

url = "http://www.nitrxgen.net/md5db/"
md5_code = input("Masukan Kode MD5 : ")
url += md5_code

deskrypt = requests.get(url)

print(f"[DONE] Hasil Deskripsi : {deskrypt.text}")
