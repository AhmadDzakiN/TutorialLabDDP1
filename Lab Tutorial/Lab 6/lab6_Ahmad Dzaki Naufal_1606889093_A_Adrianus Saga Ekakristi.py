class Monster():
    def __str__(self):
        return self.nama

    def getBerat(self):
        return self.berat

    def getBunyi(self):
        return self.bunyi

    def getHP(self):
        return self.HP

class ElderDragon(Monster):
    def __init__(self, nama, berat):
        self.berat = berat
        self.nama = nama
        self.HP = 100*berat
        self.bunyi = "Groooooaaaaaaarr"
class BirdWyvern(Monster):
    def __init__(self, nama, berat):
        self.berat = berat
        self.nama = nama
        self.HP = 10*berat
        self.bunyi = "Wrauuuuuu uuu uu u"
class Herbivore(Monster):
    def __init__(self, nama, berat):
        self.berat = berat
        self.nama = nama
        self.HP = 0.5*berat
        self.bunyi = ""
        if self.HP > 150:
            self.HP = 150

class Conductor():
    def __init__(self):
        self.monster = []
        
    def tambahMonster(self, tipeMonster, namaMonster, beratMonster):
        if tipeMonster == "ElderDragon" and beratMonster > 1500:
            pass
        elif tipeMonster == "ElderDragon" and beratMonster <= 1500:
            self.monster.append(ElderDragon(namaMonster, beratMonster))
        elif tipeMonster == "BirdWyvern":
            self.monster.append(BirdWyvern(namaMonster, beratMonster))
        elif tipeMonster == "Herbivore":
            self.monster.append(Herbivore(namaMonster, beratMonster))

    def totalBerat(self):
        jumlahberat = 0
        for a in self.monster:
            jumlahberat+=a.getBerat()
        return jumlahberat

    def totalHP(self):
        jumlahHP = 0
        for a in self.monster:
            jumlahHP+=a.getHP()
        return jumlahHP

    def bunyi(self):
        bunyi = " "
        for a in self.monster:
            bunyi += a.getBunyi()+" "
        if not("a" in bunyi):
            return "Sunyi Senyap"
        return bunyi
