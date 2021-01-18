listnama = []
listtelp = []
n = 0
print("\nSelamat datang!")

while(True):

    print("\n--- Menu ---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")

    menu = int(input("Pilih menu: "))

    if(menu == 2):
        nama = (input("Nama: "))
        listnama.append(nama)
        telp = input("No Telepon: ")
        listtelp.append(telp)
        print("Kontak berhasil ditambahkan\n")
        n += 1
    elif(menu == 1):
        print("Daftar kontak: ")
        for i in range(0, n):
            print(str(i+1) + ". " + "Nama: " + str(listnama[i]))
            print("   No.Telepon: " + str(listtelp[i]))
    elif(menu == 3):
        break
    else:
        print("Menu tidak tersedia\n")


print("Program selesai, sampai jumpa!\n")
