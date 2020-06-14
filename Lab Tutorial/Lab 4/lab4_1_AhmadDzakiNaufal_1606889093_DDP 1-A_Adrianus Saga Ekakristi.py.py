namal = input("Masukan Nama File: ")
namab = input("Masukan Nama File Setelah Diganti: ")
katalama = input("Masukan Kata Yang Akan Diganti: ")
katabaru = input("Masukan Kata Pengganti: ")


z = open(namal, "r")
VarRead = z.read()
z.close()

ganti = VarRead.replace(katalama,katabaru)
ganti = ganti.replace(katalama.capitalize(),katabaru.capitalize())

z = open(namab, "w")
z.write(ganti)
z.close()
                             
