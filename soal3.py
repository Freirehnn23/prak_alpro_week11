def cari_kata_unik(file_path):
    try:
        with open(file_path, 'r') as file:
            artikel = file.read()
        artikel = artikel.lower()
        daftar_kata = artikel.split()
        kata_unik = set(daftar_kata)
        print("Kata-kata unik yang ditemukan:")
        for kata in kata_unik:
            print(kata)
    
    except FileNotFoundError:
        print(f"File {file_path} tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        
file_path = input("Masukkan path file teks: ")
cari_kata_unik(file_path)
