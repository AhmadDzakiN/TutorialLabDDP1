def jabatTangan(orang1, orang2):
    return(orang1.getNama()+ " " +  "berjabat tangan dengan"+ orang2.getNama())

def ulangTahun(orang1):
    orang1.setUsia(orang1.getUsia()+1)
    return("Selamat ulang tahun ke-" + str(orang1.getUsia()) +" " + orang1.getNama())

def cetakKelompokUsia(orangOrang):
    Balita = []
    Anak2 = []
    Remaja = []
    Dewasa = []
    Lansia = []
    for orang1 in orangOrang:
        if orang1.getUsia() < 5:
            Balita.append(orang1.getNama())
        elif orang1.getUsia() < 14:
            Anak2.append(orang1.getNama())
        elif orang1.getUsia() < 27:
            Remaja.append(orang1.getNama())
        elif orang1.getUsia() < 70:
            Dewasa.append(orang1.getNama())
        elif orang1.getUsia() >= 70:
            Lansia.append(orang1.getNama())
    print("Balita:",",".join(Balita))
    print("Anak-anak:",",".join(Anak2))
    print("Remaja:",",".join(Remaja))
    print("Dewasa:",",".join(Dewasa))
    print("Lansia:",",".join(Lansia))

def cetakPendudukKota(orangOrang):
    city = {}
    for x in orangOrang:
        if x not in city:
            city[x.getKota()]= []
            city[x.getKota()].append(x.getNama())
        else:
            city[x.getKota()].append(x.getNama())
    for z in city:
        print("Penduduk Kota",z,":",",".join(city[z]))
