import sys
total = []

print("--------------------------")
print("KASIR gudang kamera")
print("-------------------------------")

def daftar_barang():
    print(" No | Nama Barang | Harga")
    print("-------------------------------")
    print(" 1  | sony a6000       | 5000000")
    print(" 2  | sony a7 mark3     | 4000000")
    print(" 3  | lumix g85  | 10000000")
    print(" 4  | dji mavic pro    | 12000000")
    print(" 5  | fuji film xs10       | 70000000")
    print("-------------------------------")
    kode = int(input("Masukkan angka barang  : "))
    if kode == 1:
        jumlah1 = int(input("Masukkan jumlah barang : "))
        total1 = 5000000 * jumlah1
        total.append(total1)
        tanya()
    elif kode == 2:
        jumlah2 = int(input("Masukkan jumlah barang : "))
        total2 = 4000000 * jumlah2
        total.append(total2)
        tanya()
    elif kode == 3:
        jumlah3 = int(input("Masukkan jumlah barang : "))
        total3 = 10000000 * jumlah3 
        total.append(total3)
        tanya()
    elif kode == 4:
        jumlah4 = int(input("Masukkan jumlah barang : "))
        total4 = 12000000 * jumlah4
        total.append(total4)
        tanya()
    elif kode == 5:
        jumlah5 = int(input("Masukkan jumlah barang : "))
        total5 = 7000000 * jumlah5   
        total.append(total5)
        tanya()
    return

    

def tanya():
    print("\n-------------------------------")
    tanya = input("Ingin tambah barang? [y/t] : ")
    print("-------------------------------")
    if tanya == "y":
        daftar_barang()
    elif tanya == "t":
        akhir()
    else:
        print("Pilihan yang anda masukan salah!")


def akhir():
    for harga in total:
        print("SubTotal         : ", sum(total))
        diskon = 0
        a = sum(total)
        if a > 5000000:
            diskon = a * 8/100
        elif a > 4000000:
            diskon = a * 5/100
        elif a > 10000000:
            diskon = a * 3/100
        elif a > 120000000:
            diskon = a * 1/100
        else:
            diskon = 0
        print("Potongan Harga   : ", diskon)
        totalakhir = a - diskon
        print("Total            : ", totalakhir)
        print("-------------------------------")
        bayar = int(input("Bayar            :  "))
        kembalian = bayar - totalakhir
        print("Kembalian        : ", kembalian)
        print("-------------------------------")
        print("          Terima Kasih         ")
        print("-------------------------------")


daftar_barang()