nama = []
npm = []
kelas = []
jurusan = []
print("===============TUGAS STRUKDAT===============")
jml_data = int(input("Masukan Jumlah data : "))

for i in range(jml_data):
    i+=1
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
