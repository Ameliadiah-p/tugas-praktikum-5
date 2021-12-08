# tugas-praktikum-5

***

#### Nama   : Amelia Diah Parwati
#### NIM    : 312110134
#### Kelas  : TI.21.CA1

---

# Latihan1
## Membuat Daftar Kontak Dengan Menggunakan Dictionary Pada Python

##### Buat Dictionary daftar kontak
Berikut programnya



Berikut tampilan programnya




##### Tampilkan Kontaknkya Ari 


##### Tambah kontak baru dengan nama Riko, nomor 087654544


##### Ubah kontak Dina dengan nomor baru 088999776


##### Tampilkan semua Nama


##### Tampilkan semua Nomor


##### Tampilkan daftar Nama dan nomornya


##### Hapus kontak Dina.


===================================================

# Tugas Praktikum 5
## Membuat program input data nilai siswa dengan menerapkan menu tambah, ubah,cari, hapus dan keluar

Flowchart


Berikut Programnya


Dengan keterangan

'''Python

    a = {}

'''

* Kode diatas untuk membuat dictionary kosong, untuk menampung dictionary dengan mrnggunakan tuple

'''Python

    while True:
     x = input ("[T]tambah, [U]ubah, [H]hapus, [C]cari, [L]lihat, [K]keluar: ")

'''

* kode diatas untuk perulangan while, dan juga untuk menginisialkan penambahanan menu pilihan yaitu Tambah, Ubah, Hapus, Cari, Lihat dan Keluar

'''Python

    if x.lower() == "t":
        print("Ubah Data")
        nama = input("Masukan Nama               : ")
        nim = int(input("Masukan NIM                : "))
        uts = int(input("Nilai UTS                  : "))
        uas = int(input("Nilai UAS                  : "))
        tugas = int(input("Nilai Tugas                : "))
        hasil = tugas * 0.30 + uts * 0.35 + uas * 0.35
        a[nama] = nim, uts, uas, tugas, hasil

'''


* kode diatas untuk syntak penambahan data, jika mengetikan "t" artinya menambahkan data, dan ditampung kedalam dictionary "a={}" dengan status keys, dan yang lainnya sebagai values

'''Python

    elif x.lower() == "u":
        print("Ubah Data")
        nama = input("Masukan Nama              : ")
        if nama in a.keys():
            nim = int(input("Masukan NIM                : "))
            uts = int(input("Nilai UTS                  : "))
            uas = int(input("Nilai UAS                  : "))
            tugas = int(input("Nilai Tugas                    : "))
            hasil = tugas * 0.30 + uts * 0.35 + uas * 0.35                
            a[nama] = nim, uts, uas, tugas, hasil
        else:
            print("Nama{0} Tidak di Tentukan".format(nama))

'''

* code diatas untuk syntax mengubah data, jika mengetikan "u" maka akan melakukan perubahan data, tetapi yang dapat dibah hanya valuesnya saja

'''Python

    elif x.lower() == "h":
        print("Hapus Data")
        nama = input("Masukan Nama              : ")    
        if nama in a.keys():
            del a[nama]
        else:
            print("Nama{0} Tidak di Temukan".format(nama))

'''

* code diatas untuk syntak menghapus data, jika mengetikan "h" maka akaan melakukan penghapusan dengan statemen "del a[nama]"

'''Python

    elif x.lower() == "c" :
        print("Cari Data")            
        nama = input("Masukan Nama              : ")
        if nama in a.keys():
            print("="*75)
            print("|                                   DAFTAR MAHASISWA                                   ") 
            print("="*75)
            print("| {0:15s} | {1:15d} | {2:5d} | {3:5d} | {4:7d} | {5:7.2f} |" 
                 .format(nama, nim, uts, uas, tugas,hasil))
            print("="*75)
        else:
            print("Nama{0} Tidak di Tentukan".format(nama))

'''

* code diatas adalah syntak untuk pencarian data, jika mengetikan "c" maka akan melakukan pencarian data dengan memasukan keys

'''Python

    elif x.lower() == "l" :
        if a.items():
            print("="*79)
            print("|                                   DAFTAR MAHASISWA                               ") 
            print("="*79)
            print("|No. | Nama            |       NIM       |  UTS  |  UAS  |  Tugas  |  Akhir  |")
            print("="*79)
            i = 0 
            for y in a.items():
                i += 1
                print("| {no:2d} | {0:15s} | {1:15d} | {2:5d} | {3:5d} | {4:7d} | {5:7.2f} |"
                    .format(y[0][:13], y[1][0], y[1][1], y[1][2], y[1][3], y[1][4], no=i))
                print("="*79)

'''

* code diatas untuk syntax melihat data, jika mengetikan "l" maka akan menampilkan keseluruhan dari data yang telah kita masukan

'''Python

    else:
            print("="*79)
            print("|                                   DAFTAR MAHASISWA                                ") 
            print("="*79)
            print("|No. | Nama            |       NIM       |  UTS  |  UAS  |  Tugas  |  Akhir  |")
            print("="*79)
            print("|                                   TIDAK ADA DATA                                  ") 
            print("="*79)

'''

* code diatas untuk menampilkan "TIDAK ADA DATA", jika kita mengetikan "l" dan sebelumnya belum pernah menambahkankan atau memasukan data

'''Python

    elif x.lower() == "k":
        print("Anda Telah Keluar")
        break
'''

* code diatas untuk syntax keluar dari program, jika mengetikan "k" maka otomatis program selesai dan keluar

'''Python

    else:
        print("Pilih Menu Yang Tersedia")
'''

* dan code yang terakhir adalah untuk syntax, jika kita mengetikan huruf yang diluar dari program, maka akan menampilkan "Pilih Menu Yang Tersedia"

Berikut Tampilannya

