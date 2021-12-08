daftarkontak = {"Nama":"Nomor Telepon"}
kontak = {"Ari":"081267888", "Dina":"087677776"}

print("="*50)
print("   Nama       |    Nomor Telepon   " )
print("="*50)
print(" # Ari        |   ", kontak["Ari"])
print(" # Dina       |   ", kontak["Dina"])
print("-"*50)
print()
print()
print("="*50)

# Menampilkan kontak Ari
print("Menampilkan Kontak Ari")
print("="*50)
print(" # Ari        |   ", kontak["Ari"])
print("-"*50)
print()
print()
print("="*50)

# Menambahkan kontak dengan nama Riko
print("Menambahkan kontak dengan Nama Riko")
print("dengan Nomor telepon 087654544")
kontak["Riko"] = "087654544"
print("="*50)
print(" # Riko            |   ", kontak["Riko"])
print("-"*50)
print()
print()
print("="*50)

# Mengubah Nomor Dina dengan Nomor baru
print("Mengubah Nomor Dina dengan Nomor 088999776")
print("="*50)
print(" # Dina     |    ", kontak["Dina"])
print("-"*50)
print()
print()
print("="*50)


# Menampilkan semua Nama
print("Menampilkan Semua Nama dalam Kontak")
print("="*50)
print(kontak.keys())
print("-"*50)
print()
print()
print("="*50)

# Menampilkan semua Nomor
print("Menampilkan semua Nomor dalam Konntak")
print("="*50)
print(kontak.values())
print("-"*50)
print()
print()
print("="*50)

# Menampilkan semua daftar kontak
print("Menampilkan Semua Daftar Kontak")
print("="*50)
print(kontak.items())
print("-"*50)
print()
print()
print("="*50)


# Menghapus Salah satu Kontak
print("Hapus Kontak Dina")
print("="*50)
kontak.pop("Dina")
print(kontak.items())
print("-"*50)
print()
