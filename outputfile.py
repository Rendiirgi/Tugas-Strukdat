fnama = open("nama.txt", "r") 
fnpm = open("npm.txt", "r") 
fkelas = open("kelas.txt", "r") 
fjurusan = open("jurusan.txt", "r")  

# Pada line 1 yang artinya nilai dari variable nama akan membuka dan membaca file nama.
# Ada line 2 yang artinya nilai dari variable npm akan membuka dan membaca file npm.
# Untuk line 3 yang artinya nilai dari variable kelas akan membuka dan membaca file kelas.
# Terdapat line 4 yang artinya nilai dari variable jurusan akan membuka dan membaca file jurusan.

readnama = fnama.readlines()
readnpm = fnpm.readlines()
readkelas = fkelas.readlines()
readjurusan = fjurusan.readlines()

# Pada line 11 yang artinya untuk membaca variable nama, dimana file nama akan membaca seluruh baris pada file, dan meletakkannya ke dalam sebuah list.
# Ada line 12 yang artinya untuk membaca varible npm, dimana file npm akan membaca seluruh baris pada file, dan meletakkannya ke dalam sebuah list.
# Untuk line 13 yang artinya untuk membaca variable kelas, dimana file kelas akan membaca seluruh baris pada file, dan meletakkannya ke dalam sebuah list.
# Terdapat line 14 yang artinya untuk membaca variable jurusan, dimana file jurusan akan membaca seluruh baris pada file, dan meletakkannya ke dalam sebuah list

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
