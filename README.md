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

![rumus lat1](https://user-images.githubusercontent.com/92660371/145241634-e34523e4-ff58-43bf-9e55-f31dde3b0d32.png)


Berikut tampilan programnya

![tampilan dictionary](https://user-images.githubusercontent.com/92660371/145241644-44a58ac0-7acf-4450-a4bc-417cc6411db7.png)


##### Tampilkan Kontaknkya Ari 

![Ari](https://user-images.githubusercontent.com/92660371/145241603-4924743f-9e72-4365-8898-58ff0318919b.png)


##### Tambah kontak baru dengan nama Riko, nomor 087654544

![Riko](https://user-images.githubusercontent.com/92660371/145241632-81d65c42-9876-40d2-848a-08256ab88413.png)


##### Tampilkan semua Nama

![kontak nama](https://user-images.githubusercontent.com/92660371/145241626-33d8dffc-76e1-4706-9260-275540723922.png)


##### Tampilkan semua Nomor

![nomor](https://user-images.githubusercontent.com/92660371/145241629-bb08b05b-6711-420c-ab06-98fd67e80c2e.png)


##### Tampilkan daftar Nama dan nomornya

![daftar kontak](https://user-images.githubusercontent.com/92660371/145241611-5e1b2e01-98d7-4112-9fa8-79d8f542d78a.png)


##### Hapus kontak Dina.

![hapus](https://user-images.githubusercontent.com/92660371/145241623-19cb0e50-3a1c-44c1-a2b9-af39e17fb374.png)


===================================================

# Tugas Praktikum 5
## Membuat program input data nilai siswa dengan menerapkan menu tambah, ubah,cari, hapus dan keluar

Flowchart

![flowchart](https://user-images.githubusercontent.com/92660371/145241613-874b56fc-a82a-48f0-be15-450a0c0f21b4.jpg)

Berikut Programnya

![rumus praktikum](https://user-images.githubusercontent.com/92660371/145241640-ad1973d3-af98-4b2e-9244-b88183218daf.png)

Dengan keterangan

    a = {}
    
* Kode diatas untuk membuat dictionary kosong, untuk menampung dictionary dengan mrnggunakan tuple

    while True:
     x = input ("[T]tambah, [U]ubah, [H]hapus, [C]cari, [L]lihat, [K]keluar: ")

* kode diatas untuk perulangan while, dan juga untuk menginisialkan penambahanan menu pilihan yaitu Tambah, Ubah, Hapus, Cari, Lihat dan Keluar

    if x.lower() == "t":
        print("Ubah Data")
        nama = input("Masukan Nama               : ")
        nim = int(input("Masukan NIM                : "))
        uts = int(input("Nilai UTS                  : "))
        uas = int(input("Nilai UAS                  : "))
        tugas = int(input("Nilai Tugas                : "))
        hasil = tugas * 0.30 + uts * 0.35 + uas * 0.35
        a[nama] = nim, uts, uas, tugas, hasil
        
* kode diatas untuk syntak penambahan data, jika mengetikan "t" artinya menambahkan data, dan ditampung kedalam dictionary "a={}" dengan status keys, dan yang lainnya sebagai values

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

* code diatas untuk syntax mengubah data, jika mengetikan "u" maka akan melakukan perubahan data, tetapi yang dapat dibah hanya valuesnya saja

    elif x.lower() == "h":
        print("Hapus Data")
        nama = input("Masukan Nama              : ")    
        if nama in a.keys():
            del a[nama]
        else:
            print("Nama{0} Tidak di Temukan".format(nama))

* code diatas untuk syntak menghapus data, jika mengetikan "h" maka akaan melakukan penghapusan dengan statemen "del a[nama]"

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

* code diatas adalah syntak untuk pencarian data, jika mengetikan "c" maka akan melakukan pencarian data dengan memasukan keys

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

* code diatas untuk syntax melihat data, jika mengetikan "l" maka akan menampilkan keseluruhan dari data yang telah kita masukan

    else:
            print("="*79)
            print("|                                   DAFTAR MAHASISWA                                ") 
            print("="*79)
            print("|No. | Nama            |       NIM       |  UTS  |  UAS  |  Tugas  |  Akhir  |")
            print("="*79)
            print("|                                   TIDAK ADA DATA                                  ") 
            print("="*79)

* code diatas untuk menampilkan "TIDAK ADA DATA", jika kita mengetikan "l" dan sebelumnya belum pernah menambahkankan atau memasukan data

    elif x.lower() == "k":
        print("Anda Telah Keluar")
        break

* code diatas untuk syntax keluar dari program, jika mengetikan "k" maka otomatis program selesai dan keluar

    else:
        print("Pilih Menu Yang Tersedia")

* dan code yang terakhir adalah untuk syntax, jika kita mengetikan huruf yang diluar dari program, maka akan menampilkan "Pilih Menu Yang Tersedia"

Berikut Tampilannya


