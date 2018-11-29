##Kegiatan Praktikum 9
##Kegiatan 1
berkas = open("L200180155","w")
berkas.write("L200180155 \n")
berkas.write("13-02-1999 \n")
berkas.write("Iqbal Ramadhani \n")
berkas.close()

##Kegiatan 2
berkas = open("L200180155","w")
berkas.write("L200180155 \n")
berkas.write("13/02/1999 \n")
berkas.write("Iqbal Ramadhani \n")
berkas.write("Wonogiri \n")
berkas.close()

import shelve
a = open("L200180155","r")
NIM = a.readline()
TL = a.readline()
Nama = a.readline()
Kota = a.readline()
a.close()

a = shelve.open("Iqbal")
a['b'] = [Nama, Kota, TL, NIM]
a.close()

a = shelve.open("Iqbal")

print a['b'][0]
print a['b'][1]
print a['b'][2]
print a['b'][3]

##Kegiatan 3
import shelve
a = open("L200180155","r")
NIM = a.readline()
TL = a.readline()
Nama = a.readline()
Kota = a.readline()
a.close()

a = shelve.open("Iqbal")
a['b'] = [Nama, Kota, TL, NIM]
a.close()

##Kegiatan 4
import shelve
a = shelve.open("iqbal")
print "Nama :" , a['b'][0]
print "Kota :" , a['b'][1]
print "TL   :" , a['b'][2]
print "NIM  :" , a['b'][3]




