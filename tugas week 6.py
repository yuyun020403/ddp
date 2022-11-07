p1 = {"nama": "Budo","produk":"TV","jumlah": 3}
p2 = {"nama": "Ani","Produk":"AC","jumlah": 4}
p3 = {"nama": "Siti","produk":"Kulkas","jumlah": 3}
p4 = {"nama": "Dewi","produk":"AC","jumlah": 5}
p5 = {"nama": "Andi","produk":"kulkas","jumlah": 7}
p6 = {"nama": "Dedi","produk":"AC","jumlah": 1}
p7 = {"nama": "Sri","produk":"TV","jumlah": 4}


ar_pelanggan = [p1,p2,p3,p4,p5,p6,p7]

for pelanggan in ar_pelanggan:
    print(f"Nama:",pelanggan["nama"])
    print(f"Produk:",pelanggan["produk"])
    print(f"Jumlah:",pelanggan["jumlah"])

    if (pelanggan["produk"]== "TV"):
        hargasatuan=5000000
    elif(pelanggan["produk"]== "AC"):
        hargasatuan=6000000
    elif(pelanggan["produk"]== "Kulkas"):
        hargasatuan=7000000

        print("Harga satuan:",hargasatuan)

        hargakotor = pelanggan ["jumlah"]*
    hargasatuan
    print("Harga kotor:", hargakotor)

    diskon= (hargakotor* 0.05,hargakotor* 0.2)[pelanggan["produk"] =="kulkas" and pelanggan["jumlah"] >=3]
    print("Diskon:",diskon)

    ppn =0.11*(hargakotor - ppn)
    print("PPN :" ,ppn)

    harga_bayar= (hargakotor + ppn)-diskon
    print("Harga Bayar:" ,harga_bayar)


print("========================================")






