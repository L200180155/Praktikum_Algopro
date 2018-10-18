Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
>>> Nama
'Iqbal Ramadhani'
>>> Panggilan
'Iqbal'
>>> Agama
'Islam'
>>> NIM
'L200180155'
>>> Prodi
'Informatika'
>>> TTL
'Wonogiri, 13 Februari 1999'
>>> Alamat
'Jatisrono, Wonogiri'
>>> Hobi
'Futsal'
>>> Email
'Iqbalram95@gmail.com'
>>> Citacita
'Pengusaha'
>>> ================================ RESTART ================================
>>> 
>>> Nama
'Iqbal Ramadhani'
>>> Tanggal_Lahir
'13 Februari 1999'
>>> Nama_Singkat
'Iqbal.R'
>>> ## Hasil dari Nama_Singkat yaitu slicing Nama indeks 0 sampai 5 ditambah titik dan elemen Nama indeks 6
>>> Username
'I131999'
>>> ## Hasil dari username yaitu slicing inisial Nama, Tanggal_Lahir, dan Tahun_Lahir
>>> Password
'Iqb999'
>>> ## Hasil dari 3 huruf pertama Nama dan 3 digit angka terakhir Tahun lahir
>>> ================================ RESTART ================================
>>> 
>>> Nama = 'Iqbal Ramadhani'
>>> NIM = 'L200180155'
>>> X = '1' + NIM[7:]
>>> a = int(X)
>>> b = len(Nama)
>>> type(a)
<type 'int'>
>>> ## Menampilkan Tipe dari variabel a yaitu integer atau bilangan bulat
>>> type(b)
<type 'int'>
>>>  ## Menampilkan Tipe dari variabel b yaitu integer atau bilangan bulat
>>> a / b
77
>>> ## Hasil dari variabel a dibagi variabel b (1155/15)
>>> a // b
77
>>> ## Hasil pembagian bilangan bulat variabel a dibagi variabel b
>>> 10 * (a - 999)
1560
>>> ## Hasil dari variabel a dikurangi 999 kemudian dikali 10 [10 x (1155-999) = 1560]
>>> b ** 2
225
>>>  ## Hasil dari variabel b dipangkatkan 2 yaitu 225
>>> a % b
0
>>> ## Sisa pembagian antara variabel a dibagi b adalah 0
>>> c = 12.5
>>> type(c)
<type 'float'>
>>>  ## Tipe dari variabel c adalah float atau bilangan desimal
>>> a / c
92.4
>>> ## Hasil bagi antara variabel a dibagi variabel c (1155/12.5)
>>> a // c
92.0
>>> ## Hasil pembulatan bilangan dari pembagian variabel a dibagi variabel c (92.4 dibulatkan menjadi 92.0)
>>> a % c
5.0
>>> ## sisa pembagian antara variabel a dibagi variabel c adalah 5
>>> c > b
False
>>> ## Karena variabel c tidak lebih besar dari variabel b maka hasilnya False (salah)
>>> type(c > b)
<type 'bool'>
>>>  ## Tipe/jenis dari c > b merupakan Boolean karena berisi perbandingan antaradua objek
>>> a > b and b > c
True
>>> ## Karena a lebih besar dari b dan b lebih besar dari b maka hasilnya True, karena sesuai
>>> a > 1100 or b < 10
True
>>>  ## Karena memang variabel a lebih dari 1100 maka hasilnya True karena sesuai
>>> ================================ RESTART ================================
>>> 
>>> Nama = 'Iqbal Ramadhani'
>>> NIM = 155
>>> Tinggi = 1.70
>>> Berat = 55
>>> TahunLahir = 1999
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type(Aku)
<type 'tuple'>
>>> ## Tipe/jenis dari Aku merupakan suatu Tuple atau deretan objek
>>> Aku[0]
1999
>>> ## Menampilkan hasil dari elemen Tuple 'Aku' indeks ke 0
>>> a = NIM % 4; Aku[a]
155
>>> ## karena terdapat sisa pembagian dari operasi NIM % 4 maka yang ditampilkanadalah NIM itu sendiri
>>> type(Aku[a])
<type 'int'>
>>> ## Tipe/jenis dari variabel a adalah integer atau bilangan bulat
>>> Aku[a:4]
(155,)
>>> ## Hasil dari a sampai indeks ke 3 dari tuple Aku
>>> type(Aku[4])
<type 'str'>
>>> ## Tipe/jenis dari Tuple Aku indeks ke 4 adalah string
>>> Aku[0] = 'ok'

Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    Aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> ## Program Error karena ingin mengubah elemen tuple Aku indeks ke 0 menjadi ok, padahal elemen tuple tidak bisa diubah sehingga prgram ini error
>>> type(Data)
<type 'list'>
>>> ##Tipe/jenis dari Data merupakan suatu List
>>> type(Data[4])
<type 'str'>
>>> ## Tipe/jenis dari elemen List Data indeks ke 4 adalah string
>>> Data[4][5]
' '
>>> ## Karena pada elemen List Data, indeks 5 tidak ada/ hanya sampai indks 4
>>> Data[4][a:6]
'al '
>>> ## Hasil dari Data indeks 4 yaitu 'Iqbal Ramadhani' kemudian dipotong lagi dari huruf a sampai indeks ke 5 sehingga hasilnya adalah 'al'
>>> Data[0] = 'ok'; Data
['ok', 55, 1.7, 155, 'Iqbal Ramadhani']
>>> ## Elemen dalam List dapat diubah dan program tersebut bertujuan untuk mengubah elemen List Data indeks ke 0 yang semula tahun lahir menjadi 'ok'
>>> Data[-a]
1.7
>>> ## Hasil dari Data[-a] yaitu tinggi = 1.7
>>> range(a)
[0, 1, 2]
>>> ## Karena a = 155 /terdiri dari 3 digit angka maka perhitungan rangenya adalah [0, 1, 2]
