import random

buku = {}
buku2 = {}


def daftar(nomor, nama):
    buku[nomor] = []
    buku[nomor].append(nama)
    buku[nomor].append(0)
    buku2[nomor] = []
    print(nama, "mendaftar", nomor)
    
def telepon(nomor1, nomor2, waktu):
    if nomor2 in buku:
        tarif = 100
    elif nomor2 not in buku:
        tarif = 200
    if nomor1 == nomor2:
        print("Telepon Gagal")
    elif buku[nomor1][1] - (waktu*tarif) < 0:
        lama = buku[nomor1][1]//tarif
        buku[nomor1][1]-= (tarif*lama)
        print("Pulsa tidak cukup, telepon berhenti pada detik ke", lama)
        buku2[nomor1].append("{} menelepon {} selama {} detik".format(buku[nomor1][0], nomor2, lama))
    elif buku[nomor1][1] > 0:
        buku[nomor1][1]-= (waktu*tarif)
        print(buku[nomor1][0], "menelepon", nomor2, "selama", waktu)
        buku2[nomor1].append("{} menelepon {} selama {} detik".format(buku[nomor1][0], nomor2, waktu))

def isi(nomor, pulsa):
    buku[nomor][1] += pulsa
    print(buku[nomor][0], "Mengisi Pulsa Sebanyak", pulsa)
    
def sms(nmr1, nmr2, pesan):
    if nmr2 in buku:
        tarif = 25
    elif nmr2 not in buku:
        tarif = 50
    if nmr1 == nmr2:
        print("Pesan Gagal Terkirim")
    elif (buku[nmr1][1] - (tarif*len(pesan))) <= 0 or buku[nmr1][1] == 0:
        print("Pesan Gagal Terkirim")
    elif buku[nmr1][1] > 0:
        buku[nmr1][1]-= (tarif*len(pesan))
        print(buku[nmr1][0], "mengirim pulsa kepada", nmr2)
    
def undian(bonus):
    lst = []
    for i in buku.keys():
        lst.append(i)
    rdm = random.choice(lst)
    buku[int(rdm)][1] += bonus
    print(rdm,"mendapatkan pulsa sebanyak",bonus)

def pulsa(nomor):
    print("Pulsa", buku[nomor][0], "dengan nomor", nomor, "sekarang", buku[nomor][1])
    
def pengguna(nama):
    lst2 = []
    for i in buku.keys():
        lst2.append(i)
    for i in lst2:
        if nama == buku[i][0]:
            print("Pulsa", nama, "dengan nomor", i, "sekarang adalah", buku[i][1])

def log(nomor):
    for i in buku2[nomor]:
        print(i)


pelanggan = int(input("Masukan Jumlah Pengguna: "))
for i in range(pelanggan):
    name = input("Masukan Nama Dari Pengguna: ")
jmlperintah = int(input("Masukan Jumlah Perintah Yang Akan Di Jalankan: "))
for x in range(jmlperintah):
    stop = True
    while True:
        perintah = input("Masukan Perintah: ").split(" ")
        if perintah[0] == "daftar".lower():
            daftar(int(perintah[2]), perintah[1])
            break    
        elif perintah[0] == "telepon".lower():
            try:
                telepon(int(perintah[1]),int(perintah[2]),int(perintah[3]))
            except ValueError:
                print("Silahkan Coba Lagi Karena Input Salah")
            except KeyError:
                print("Nomor", perintah[1], "Belum Terdaftar")
            break
        elif perintah[0] == "isi".lower():
            try:
                isi(int(perintah[1]),int(perintah[2]))
            except ValueError:
                print("Silahkan Coba Lagi Karena Input Salah")
            except KeyError:
                print("Nomor", perintah[1], "Belum Terdaftar")
            break
        elif perintah[0] == "sms".lower():
            try:
                sms(int(perintah[1]),int(perintah[2]),perintah[3])
            except ValueError:
                print("Silahkan Coba Lagi Karena Input Salah")
            except KeyError:
                print("Nomor", perintah[1], "Belum Terdaftar")
            break
        elif perintah[0] == "undian".lower():
            try:
                undian(int(perintah[1]))
            except ValueError:
                print("Silahkan Coba Lagi Karena Input Salah")
            break
        elif perintah[0] == "pulsa".lower():
            try:
                pulsa(int(perintah[1]))
            except ValueError:
                print("Silahkan Coba Lagi Karena Input Salah")
            except KeyError:
                print("Nomor", perintah[1], "Belum Terdaftar")
            break
        elif perintah[0] == "pengguna".lower():
            pengguna(perintah[1])
            break
        elif perintah[0] == "log".lower():
            try:
                log(int(perintah[1]))
            except ValueError:
                print("Silahkan Coba Lagi Karena Input Salah")
            except KeyError:
                print("Nomor", perintah[1], "Belum Terdaftar")
            break
                
