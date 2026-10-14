#Variabel
name = 'Gord'
greet = 'Halo, nama saya ' 
print('Halo, nama saya Rudy')
print('Halo, nama saya' + name)
print(greet + 'Rudy')
print(greet + name)


#Tipe data
#str()
'Kata'
"20000"
"200.23"
'@#$$^()))()'

int()
2032
10000
48

float()
354737.233
0.233
5.0

#Convert
str(20)
str(23.1)
int("50")
int(23.33)
float("23.4")
float('0.0')
      
#dictionary{
#}
Barang = {
    "Nama" : "Budi",
    'Usia' : "20"
}

#list[]
GEnap = [2, 4, 6]

tuple()
Ganjil = (1, 3, 5)

#set{}
Prima = (2, 3, 5)

#Operasi
20 + 5
20 - 5
20 * 5
20 % 5
20 ** 5
20 // 5

#Activity: 2
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input('Masukkan angka kedua: '))
operasi = (angka1 % angka2) - (angka2 // angka1 + 0.5)

#Program study hours calculator
jumlah_jam_tidur = int(input('Berapa jam sehari Anda tidur: '))
jumlah_jam_bermain = int(input('Berapa lama Anda bermain tiap hari: '))
jumlah_jam_istirahat = int(input('Berapa jam yang Anda inginkan untuk beristirahat: '))
waktu_belajar_tersedia = str(24 - jumlah_jam_tidur - jumlah_jam_istirahat - jumlah_jam_bermain)
print('Anda punya waktu luang untuk belajar sebanyak ' + str(waktu_belajar_tersedia) + ' jam')