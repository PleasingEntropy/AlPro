angka = input('Masukkan angka bulat: ')
if angka % 2 == 0 and angka / 2 < 5:
    print('Angka Anda genap, kurang dari 10')
elif angka % 2 == 0 and angka / 2 > 5:
    print('Angka Anda genap, lebih dari 10')
else:
    print('Angka Anda ganjil')

sedang_hujan = True
if not sedang_hujan:
    print('matahari terlihat')    
else:
    print('Matahari tertutup awan mendung')

uang = int(input('Masukkan jumlah uang: '))
if uang >= 13000:
    jumlah_item = int(uang / 13000)
    jumlah_beli = int(input('Anda bisa membeli sebanyak ' + str(jumlah_item) + ' atau masukkan jumlah yang diinginkan: '))
    if jumlah_beli > int(uang / 13000):
        print('Uang Anda kurang, mohon masukkan jumlah item yang pas')
    elif jumlah_beli == 0:
        print('Masukkan jumlah selain 0')
    elif jumlah_beli == jumlah_item:
        print('Transaksi sebanyak ' + str(jumlah_item) + ' item berhasil', ', sisa uang: ' + str(uang % 13000))
    else:
        print('Transaksi sebanyak ' + str(jumlah_beli) + ' item berhasil', ', sisa uang: ' + str(uang - (13000 * jumlah_beli)))
elif uang < 13000:
    print('Siahkan masukkan nominal uang tambahan atau batalkan transaksi')
else:
    print('Silahkan masukkan nominal yang valid')