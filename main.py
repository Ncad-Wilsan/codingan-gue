nama = 'richard wilsan' #tipe data string
umur = 18 #tipe integral
tinggi_badan = 175.5 #tipe data float

menyapa = 'halo semua, perkenalkan namaku '
menyapa_umur = 'sekarang umurku '
menyapa_tinggi = 'sekarang tinggi badanku '

#rumus = int("10") --> 10
#rumus = str(5) --> 5
#rumus = float(5) ---> 5

print(menyapa + nama)
print(menyapa_umur + str(umur))
print(menyapa_tinggi + str(tinggi_badan))

print('halo semua, perkenalkan nama saya ' + nama + ' sekarang umurku ' + str(umur) + ' tahun' + ' sekarang tinggiku ' + str(tinggi_badan))

input_nama = input('halo namamu siapa? ') #rumus input(lalala), untuk tanya jawab

print(input_nama) 

a = 1/2
b = 1/6
c = a/b
print(c) #tidak diberi int karena a&b sudah angka tulen

a = input('masukkan angka pertama ')
b = input('masukkan angka kedua ')
c = int(a) * int(b) #diberi int karena a&b data string, supaya hasilnya tidak seperti huruf

print('hasilnya adalah: ' + str(c))

nama_saya = "Richard Wilsan"

print(nama_saya.find('l')) # .find untuk mencari huruf ke berapa dalam variabel

print('n' in nama_saya) # 'huruf' in (variabel) sama seperti find tapi bernilai tru/false

print(len(nama_saya)) # len() untuk menghitung jumlah huruf dalam variabel

print(nama_saya.upper()) # .uppper() untuk mengkapital huruf dalam variabel

print(nama_saya.count('a')) # .count untuk menghitung kata/angka dalam variabel

usia = 20
# == sama dengan, != tidak sama dengan, sisanya sama

if usia >= 20 and usia <= 30:
    print('yomann lu udah masuk standart kita')
elif usia > 30:
    print('ketuaan lu')
else:
    print('coba lagi lain waktu')

usia = input('berapa usia kamu ')
# == sama dengan, != tidak sama dengan, sisanya sama

if usia >= str("20") and usia <= str("30"):
    print('yomann lu udah masuk standart kita')
elif usia > str("30"):
    print('yomann lu ketuaan')
else:
    print('ga cukup umur')