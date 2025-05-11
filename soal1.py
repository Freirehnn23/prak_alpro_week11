def tiga_bilangan_terbaik(lst):
    unique_numbers = set(lst)
    sorted_numbers = sorted(unique_numbers, reverse=True)
    return sorted_numbers[:3]

def main():
    bilangan = []
    print("Masukkan 3 bilangan satu per satu:")

    for i in range(3):
        while True:
            try:
                angka = int(input(f"Input bilangan ke-{i+1}: "))
                bilangan.append(angka)
                break
            except ValueError:
                print("Input harus berupa bilangan bulat valid, coba lagi.")

    terbaik = tiga_bilangan_terbaik(bilangan)
    print("3 bilangan terbaik adalah:", terbaik)

if __name__ == "__main__":
    main()



# Buatlah fungsi untuk mencari 3 bilangan terbaik dari sebuah list. Bilangan terbaik adalah bilangan dimulai dari yang paling tinggi. 