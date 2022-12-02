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
    
    print('|')

print("+--------------------+----------------------------------------------------------------+")
