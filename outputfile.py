fnama = open("nama.txt", "r") #Membuka file bernama nama.txt
fnpm = open("npm.txt", "r") #Membuka file bernama npm.txt
fkelas = open("kelas.txt", "r") #Membuka file bernama kelas.txt
fjurusan = open("jurusan.txt", "r")  #Membuka file bernama jurusan.txt

readnama = fnama.readlines()
readnpm = fnpm.readlines()
readkelas = fkelas.readlines()
readjurusan = fjurusan.readlines()

print("""
+-----------------------+------------------------------------ -+----------------------+
| NAMA                  | NPM               |KELAS             |JURUSAN               |
+-----------------------+-------------------+------------- ----+----------------------+""")

for i in range (len(readnama)): 
    nama = str(readnama[i].strip()) 
    print('| '+nama,end='')
    #Perulangan for yang mendeklarasika variabel i in range dengan menggunakan len untuk mengetahui panjang item pada variabel nama.
    #Variabel nama akan sama dengan variabel readnama yang memiliki variabel i dan bertipe data string, dimana strip akan menghasilkan karakter besar atau kecil.
    #Lalu akan mencetak variabel nama dengan yang akan membuat baris baru ketika dicetak.
    for j in range(20-1-len(nama)):
        print(' ',end ='')
    npm = str(readnpm[i].strip())
    print('| '+npm,end='')
    for k in range(19-1-len(npm)):
         print(' ',end ='')
    kelas = str(readkelas[i].strip())
    print('| '+kelas,end='')
    for p in range(19-1-len(kelas)):
         print(' ',end ='')
    jurusan = str(readjurusan[i].strip())
    print('| '+jurusan,end='')
    for v in range(19-1-len(jurusan)):
         print(' ',end ='')
    #pada line 22 sampai 35 perulangan for dengan variabel j, k, p, v dalam jarak 20-1-len dan 19-1-len dimasukkan variabel nya masing masing disesuaikan
    #mencetak dengan print untuk baris barunya dan npm = string readnpm yang dimasukkan variabel i perulangannya dan strip sebagai menghasilkan karakternya besar atau kecil
    #lalu cetak lagi dengan akhiran end=
    
    print('|') # berfungsi untuk penutup pada output ketika dicetak 

print("+--------------------+----------------------------------------------------------------+") 
