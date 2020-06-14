import aktivitas
class Orang():
    def __init__(self, nama, usia, kota):
        self.nama = nama
        self.usia = usia
        self.kota = kota
    def getNama(self):
        return self.nama
    def getUsia(self):
        return self.usia
    def getKota(self):
        return self.kota
    def setNama(self, nama):
        self.nama = nama
    def setUsia(self, usia):
        self.usia = usia
    def setKota(self, kota):
        self.kota = kota


orang1 = Orang("Saga", 17, "Jakarta")
orang2 = Orang("Halim", 3, "Jakarta")
orang3 = Orang("Stephen", 4, "Bandung")
orang4 = Orang("Elang", 4, "Depok")
print(aktivitas.jabatTangan(orang1,orang2))
aktivitas.ulangTahun(orang1)
print(aktivitas.ulangTahun(orang1))
listOrang = [orang1,orang2,orang3,orang4]
aktivitas.cetakKelompokUsia(listOrang)
aktivitas.ulangTahun(orang3)
orang5 = Orang("Christian", 27, "Surabaya")
orang6 = Orang("Jaya", 78, "Semarang")
listOrang.append(orang5)
listOrang.append(orang6)
aktivitas.cetakKelompokUsia(listOrang)
aktivitas.cetakPendudukKota(listOrang)
