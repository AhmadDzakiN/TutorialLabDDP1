import random #modul random
import datetime #modul waktu

poin = []
nama = []
game = 0
print("Selamat Datang di Tebak Lirik!")


while True : #loop game
    name = input("Masukan Nama Kamu: ")
    skor = 0
    waktu = str(datetime.date.today()) #tanggal main
    print("Tanggal Main:",waktu)
    logbaru=open("log-"+name+".txt","w") #membuat file log pemain
    print("Nama Pemain:",name, file=logbaru)
    print("Tanggal Main:",waktu,"\n", file=logbaru)
    print("Selamat Bermain")
    namalagu = ["a thousand years", "air", "bad day", "bohemian rhapsody",\
        "dia", "heal the world", "hello", "kau adalah", "kepompong",\
        "kesempurnaan cinta", "laskar pelangi", "lost stars", "no one else like you",\
        "pupus", "sebuah kisah klasik", "sepatu", "tak gendong",\
        "the lazy song", "upup", "welcome to my life"] #judul lagu

    for round in range (1,11): #loop untuk jumlah ronde dalam game
        rdm = random.choice(namalagu) #mengacak lagu yang akan dimainkan
        apus = namalagu.remove(rdm) #menghapus lagu yang sudah dimainkan agar tidak muncul lagi di game
        print("Judul Lagu:", rdm  , file=logbaru)

        print("Ronde ke :", round)
        print("Lanjutkan Lirik Ini:")
        buka = open('lirik/'+rdm+".txt","r") #membuka lagu yang sudah diacak
        x = buka.readlines() #lirik perbaris dijadikan list
        x[-1] = x[-1]+'\n'
        rdm2 = random.randint(0, len(x)-4) #mengambil 4 baris secara acak namun berurutan untuk dijadikan soal 
        print(x[rdm2]+x[rdm2+1]+x[rdm2+2]) #menampilkan 3 baris lirik sebelum baris soal yang ditanyakan
        print("Lirik Soal:"+"\n"+x[rdm2]+x[rdm2+1]+x[rdm2+2], file=logbaru)
    

        var_a = 1    
        for i in range(3): #loop untuk jawaban
            jwb = input("Masukan Jawaban: ")
            jwb = jwb + "\n" 
            
            if jwb.lower() == x[rdm2+3].lower(): #untuk jawaban benar
                print("Benar")
                print("Tebakan: Benar","\n", file=logbaru)
                skor+=1
                break
                
            elif jwb.lower() != x[rdm2+3].lower() and var_a != 3: #jika jawaban salah
                print("Jawaban Salah")
                print(" ".join(x[rdm2+3].split()[0:var_a]))#menambahkan satu kata dari baris lirik soal yang ditanyakan untuk petunjuk
                var_a += 1
                
            else: #jika kesempatan habis
                print("Kesempatan Kamu Habis")
                print("Jawabannya adalah:", x[rdm2+3]) #akan memunculkan baris lirik soal yang ditanyakan
                print("Tebakan: Salah","\n", file=logbaru)

    game+=1 #game akan berakhir atau bertambah jika sudah selesai 10 ronde
    selesai = print("Permainan Telah Berakhir")
    print("Skor Kamu Sekarang Adalah: ", skor)            
    ulang = input("Apakah Ingin Bermain lagi? Yes/No ")
    print("Skor Akhir: ", skor, file=logbaru)

    poin.append(skor)
    avg = sum(poin)/len(poin) #rata rata skor
    nama.append(name)
    maksperaih = nama[poin.index(max(poin))] #mengetahui nama peraih skor tertinggi
    

    if ulang.lower() == "yes":
        continue
    elif ulang.lower() == "no":
        print("Terima Kasih Telah Bermain")
        logbaru.close()
        logstat = open("log statistik.txt", "w") #membuat log statistik dalam mode write
        print("Jumlah Permainan Dilakukan: ",game, file=logstat) #menghitung jumlah permainan
        print("Rata-Rata Skor Adalah: ", avg, file=logstat)
        print("Skor Tertinggi Adalah: ", max(poin), file=logstat)
        print("Peraih Skor Tertinggi Adalah: ", maksperaih, file=logstat)
        logstat.close()
        break

        
