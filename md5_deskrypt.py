print("-" * 26)
print("MD5".center(26," "))
print("DESCRYPTOR".center(26," "))
print("Created : By JKresna".center(26," "))
print("-" * 26)
print("PASTIKAN INTERNET MENYALA")


def md5_descrypt(md5):
        
    deskrypt = requests.get(md5)    
    hasil = deskrypt.text
    
    if len(hasil) == 0:
        print("[FAIL] Hasil tidak ditemukan!\n")
    else:
        print(f"[DONE] Hasil Deskripsi : {hasil}\n")



while True:
    try:    
        import requests
        
        print("\n")
        url = "http://www.nitrxgen.net/md5db/"
        md5_code = input("Masukan Kode MD5 : ")
        url += md5_code
        
        if len(md5_code) == 0:
            pass     
        else:
            md5_descrypt(url)
            
        quit = input("keluar? (tulis y untuk keluar, ENTER untuk lanjut) : ")
        if quit == 'y':
            break

    except ImportError:
        print("[ERROR] modul requests belum di install!")
        print("untuk menginstall lakukan perintah ini :")
        print("     $ pip install requests\n")
        break
    except KeyboardInterrupt:
        print("\nBye Bye.\n")
        break
    except EOFError:
        print("\nBye Bye.\n")
        break
    except:
        print("[ERROR] terjadi kesalahan!")
        print("NB: PASTIKAN UNTUK MENYALAKAN INTERNET!\n")
        break
