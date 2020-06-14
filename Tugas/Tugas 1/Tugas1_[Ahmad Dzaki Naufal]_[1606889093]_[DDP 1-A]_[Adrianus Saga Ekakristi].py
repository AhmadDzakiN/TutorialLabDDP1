#Menu
while True:
    def intro():
        print("-------------------------------------------------------------------")
        print("Selamat Datang Di Aplikasi Konverter Decimal, Binary, Hexadecimal")
        print("""By Ahmad Dzaki Naufal
NPM :1606889093
Jurusan: Sistem Informasi
Kelas: Dasar-Dasar Pemrograman 1-A""")
        print("-------------------------------------------------------------------")
        print("Pilihan Konversi: ")
        print("1. Decimal ke Binary")
        print("2. Binary ke Decimal")
        print("3. Decimal ke Hexadecimal")
        print("4. Hexadecimal ke Decimal")
        print("5. Berhenti")

#Ini fungsi untuk mengkonversi decimal ke binary
    def deckebin(a):           
        if a > 0 :
            deckebin (a//2)
            print(a%2, end="")
            return ""

#ini fungsi untuk mengkonversi binary ke decimal          
    def binkedec():
        try:
            Inpud = input("Masukan Angka: ")
            a = int(Inpud)    
            exp = 0
            hasil = 0
            while a > 0 :
                number = a%10
                a = a//10
                answer = "Hasil Dari Konversi ini Adalah: "
                hasil = hasil + (2**exp) * number
                exp += 1
            print(answer)
            print(hasil)
        except:
            print("Input Yang Dimasukkan Salah, Silahkan Coba Kembali")
            
#Ini fungsi untuk merubah decimal ke hexadecimal
    jawaban = ""
    def deckehex(b):
        while b > 0 :
            global jawaban
            lanjutan = str(b%16)
            if lanjutan == "10":
                lanjutan = "A"
            elif lanjutan == "11":
                lanjutan = "B"
            elif lanjutan == "12":
                lanjutan = "C"
            elif lanjutan == "13":
                lanjutan = "D"
            elif lanjutan == "14":
                lanjutan = "E"
            elif lanjutan == "15":
                lanjutan = "F"
            b = (b//16)
            jawaban = lanjutan + jawaban
        return jawaban
        
#Ini fungsi untuk merubah hexadecimal ke decimal                             
    def hexkedec(c):
        exp = 0
        bilangan = 0
        for aw in c[::-1]:
            if aw == "A" or aw == "a":
                aw = 10
            elif aw == "B" or aw == "b":
                aw = 11
            elif aw == "C" or aw == "c":
                aw = 12
            elif aw == "D" or aw == "d":
                aw = 13
            elif aw == "E" or aw == "e":
                aw = 14
            elif aw == "F" or aw == "f":
                aw = 15

            hasil = int(aw) * (16**exp)
            bilangan = bilangan + hasil
            exp += 1
        return bilangan
        
                
#Menu Untuk Input     
    intro()
    masukan = int(input("Pilih Jenis Konversi: "))
    if masukan == 1:
        try:
            Angka = int(input("Masukan Angka: "))
            print("Hasil Dari Konversi Ini Adalah: ")
            print(deckebin(Angka))
        except:
            print("Input Yang Dimasukkan Salah, Silahkan Coba Kembali")
           
    elif masukan == 2:
        binkedec()
        
    elif masukan == 3:
        try:
            Angka = int(input("Masukan Angka: "))
            print("Hasil Dari Konversi Ini Adalah: ")
            print(deckehex(Angka))
        except:
            print("Input Yang Dimasukkan Salah, Silahkan Coba Kembali")
        
    elif masukan == 4:
        try:
            Angka = input("Masukan Input: ")
            print("Hasil Dari Konversi Ini Adalah: ")
            print(hexkedec(Angka))
        except:
            print("Input Yang Dimasukkan Salah, Silahkan Coba Kembali")
            
    elif masukan == 5:
        print("Terima Kasih Telah Menggunakan Aplikasi Ini")
        print("Sampai Jumpa Kembali")
        print("-------------------------------------------------------------------")
        input('Tekan Tombol Apa Saja Untuk Melanjutkan...   ')
        break
    
