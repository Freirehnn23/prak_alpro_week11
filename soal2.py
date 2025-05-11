# opsi 1
def main():
    bilangan = []
    print('Masukkan bilangan satu per satu. Ketik "done" untuk selesai dan lihat rata-rata.')

    while True:
        user_input = input("Masukkan bilangan (atau 'done'): ").strip()

        if user_input.lower() == "done":
            break

        try:
            angka = float(user_input)
            bilangan.append(angka)
        except ValueError:
            print("Input tidak valid, mohon masukkan bilangan atau 'done'.")

    if bilangan:
        rata_rata = sum(bilangan) / len(bilangan)
        print(f"Rata-rata bilangan yang dimasukkan adalah: {rata_rata}")
    else:
        print("Tidak ada bilangan yang dimasukkan.")

if __name__ == "__main__":
    main()

#  ================================================
# opsi 2

def hitung_rata_rata():
    total = 0
    count = 0
    
    while True:
        input_user = input("Masukkan bilangan atau ketik 'done' untuk selesai: ")
        
        if input_user.lower() == 'done':
            break
        
        if input_user.replace('.', '', 1).isdigit(): 
            total += float(input_user)
            count += 1
        else:
            print("Input tidak valid.")
    
    if count > 0:
        print(f"Rata-rata bilangan: {total / count}")
    else:
        print("Tidak ada bilangan yang dimasukkan.")


hitung_rata_rata()
