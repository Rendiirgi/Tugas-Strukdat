fnama = open("nama.txt", "r")
fnpm = open("npm.txt", "r")
fkelas = open("kelas.txt", "r")
fjurusan = open("jurusan.txt", "r")

readnama = fnama.readlines()
readnpm = fnpm.readlines()
readkelas = fkelas.readlines()
readjurusan = fjurusan.readlines()

print("""
+-----------------------+------------------------------------ -+----------------------+
| NAMA                  | NPM               |KELAS             |JURUSAN               |
+-----------------------+-------------------+------------- ----+----------------------+""")
