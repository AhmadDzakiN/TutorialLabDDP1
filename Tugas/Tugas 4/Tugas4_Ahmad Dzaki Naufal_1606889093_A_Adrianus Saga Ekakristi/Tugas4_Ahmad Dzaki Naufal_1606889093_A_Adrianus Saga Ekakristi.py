import random
from datetime import datetime

class Lagu():
    def __init__(self,title,lyrics):
        self.title = title
        self.lyrics = lyrics

    def getTitle(self):
        return self.title

    def getLyrics(self):
        lst = []
        rdm = random.randrange(0, len(self.lyrics)-4)
        for x in range(0,4):
            lst.append(self.lyrics[rdm+x])
        return lst

class Player():
    def __init__(self,name,score = 0):
        self.name = name
        self.score = score
        self.playTime = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    def getName(self):
        return self.name

    def getTime(self):
        return self.playTime

    def getScore(self):
        return self.score

class Game():
    def __init__(self):
        self.permainan = 0
        self.lstskor = []
        self.playerz = []
        self.songs = ["a thousand years", "air", "bad day", "bohemian rhapsody",\
        "dia", "heal the world", "hello", "kau adalah", "kepompong",\
        "kesempurnaan cinta", "laskar pelangi", "lost stars", "no one else like you",\
        "pupus", "sebuah kisah klasik", "sepatu", "tak gendong",\
        "the lazy song", "upup", "welcome to my life"]

    def generateSongs(self):
        lstjudul = []
        rdm2 = random.shuffle(self.songs)
        for x in range(0,10):
            lstjudul.append(self.songs[x])
        return lstjudul
    
    def getPlayer(self):
        return self.pemain

    def startGame(self):
        print("Selamat Datang Di Game Tebak Lagu")
        self.name = input("Masukan Nama: ")
        self.skor = 0
        self.pemain = Player(self.name,self.skor)
        self.logbaru = open("log"+self.pemain.getName()+".txt","w")
        print("Tanggal Main:",self.pemain.getTime())
        print("Selamat Bermain")
        print("Nama Pemain:", self.getPlayer().getName(), file=self.logbaru)
        print("Tanggal dan Waktu Bermain:", self.getPlayer().getTime(), file=self.logbaru)
        listjudul = self.generateSongs()
        for ronde in range(0,10):
            print("\nRonde:", ronde+1)
            print("\nRonde:", ronde+1, file=self.logbaru)
            print("Lanjutkan Lirik Ini:")
            self.pemain = Player(self.name,self.skor)
            buka = open("lirik/"+listjudul[ronde]+".txt","r")
            baca = buka.readlines()
            baca[-1] = baca[1] + "\n"
            self.lagu = Lagu(listjudul[ronde],baca)
            self.lirik = self.lagu.getLyrics()
            judul = self.lagu.getTitle()
            print("Judul Lagu:", judul, file=self.logbaru)
            print(self.lirik[0]+self.lirik[1]+self.lirik[2])
            print("Lirik Soal:"+"\n"+self.lirik[0]+self.lirik[1]+self.lirik[2], file=self.logbaru)
            self.processAnswer()
        print("\nPermainan Telah Berakhir")
        print("Skor Yang Kamu Dapatkan Adalah:",self.getPlayer().getScore())
        print("Skor Akhir:", self.getPlayer().getScore(), file=self.logbaru)
        self.permainan += 1
        self.playerz.append(self.getPlayer().getName())
        self.lstskor.append(self.getPlayer().getScore())
        while True:
            ulang = input("Apakah Ingin Bermain Lagi? (Yes/No): ")
            if ulang.lower() == "yes":
                self.startGame()
                break
            elif ulang.lower() == "no":
                print("Terima Kasih Telah Bermain")
                self.statistik()
                self.logbaru.close()
                self.logstat.close()
                break
                
        
    def processAnswer(self):
        word = 1
        for i in range(4):
            jawab = input("Masukan Jawaban: ")
            jawab = jawab + "\n"
            if jawab.lower() == self.lirik[3].lower():
                print("Jawaban Benar!")
                print("Tebakan Benar","\n", file=self.logbaru)
                self.skor += 1
                break

            elif jawab.lower() != self.lirik[3].lower() and word != 4:
                print("Jawaban Salah!")
                print("\nPetunjuk: "+" ".join(self.lirik[3].split()[0:word]))
                word+=1

            else:
                print("\nKesempatan Habis")
                print("Jawabannya Adalah:", self.lirik[3])
                print("Tebakan: Salah","\n", file=self.logbaru)
                
                
            
    def statistik(self):
        self.logstat = open("log statistik.txt", "w")
        avg = sum(self.lstskor)/len(self.lstskor)
        playerwin = self.playerz[self.lstskor.index(max(self.lstskor))]
        print("Jumlah Permainan Dilakukan:", self.permainan, file=self.logstat)
        print("Rata-Rata Skor Adalah:", avg, file=self.logstat)
        print("Skor Tertinggi Adalah:", max(self.lstskor), file=self.logstat)
        print("Peraih Skor Tertinggi Adalah:", playerwin, file=self.logstat)
        
        
        
        
        
Game().startGame()
            
            
            
            
        
                
        
        
