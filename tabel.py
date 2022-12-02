"""
    Untuk line 9 yang artinya membuat tampilan awal output.
    Pada line 10 yang artinya kita diperintahkan untuk menginputkan jumlah data dengan inputan harus bertipedata integer dan disimpan pada variable jml_data.
"""
nama = []
npm = []
kelas = []
jurusan = []
print("===============TUGAS STRUKDAT===============")
jml_data = int(input("Masukan Jumlah data : "))

for i in range(jml_data):
    i+=1
"""
    Untuk line 17 yang artinya kita membuat tampilan awal output dengan statement "Data Mahasiswa Ke-" serta ditambahkan nilai variable i dengan kondisi jika mengisi nilai variable i akan ditambah 1.
    Terdapat line 18 yang artinya kita diperintahkan untuk menginputkan data berupa nama dengan inputan harus bertipedata string dan inputan tersebut akan disimpan pada variable nm.
    Pada line 19 sampai dengan line 21 sama halnya seperti line 11 yaitu menginputkan data dimana masing-masing mempunyai penyimpanan inputan variable yang berbeda.
    Ada line 23 yang artinya variable nama akan menambahkan nilai array pada urutan akhir terhadap variable nm.
    Di line 24 sampai dengan line 26 sama halnya seperti line 22 yaitu menambahkan nilai array pada urutan akhir pada variable yang berbeda-beda dan juga terhadap variable yang berbeda-beda.
"""    
print("===========Data Mahasiswa ke -",i,"===========")
    nm = str(input("Masukan Nama    : "))
    np = (input("Masukan NPM     : "))
    kls = (input("Masukan Kelas   : "))
    jrsn = (input("Masukan Jurusan : "))
    print("===========================================")
    nama.append(nm)
    npm.append(np)
    kelas.append(kls)
    jurusan.append(jrsn)

"""
    selanjutnya pada program dibawah akan terdapat prose pembuatan file txt dari nama, npm, kelas dan jurusan.
    Dengan menggunakan operasi 'w' yang berfungsi untuk membuka file dan menulis isi dari file yang dibuat
    Lalu menngunakan perulangan for dan .close untuk menutup file
"""
    with open('nama.txt', 'w') as fnama:
    for line in nama:
        fnama.write(f"{line}\n")
fnama.close()
with open('npm.txt', 'w') as fnpm:
    for line in npm:
        fnpm.write(f"{line}\n")
fnpm.close()
with open('kelas.txt', 'w') as fkelas:
    for line in kelas:
        fkelas.write(f"{line}\n")
fkelas.close()
with open('jurusan.txt', 'w') as fjurusan:
    for line in jurusan:
        fjurusan.write(f"{line}\n")
fjurusan.close()
