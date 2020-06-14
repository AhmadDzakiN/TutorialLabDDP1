while True:
    Angka1 = int(input("Masukan Angka 1: "))
    Angka2 = int(input("Masukan Angka 2: "))
    Angka3 = int(input("Masukan Angka 3: "))
    if Angka3 == Angka1*Angka2:
        print("*")
    elif (Angka2 !=0) and (Angka3 == Angka1/Angka2):
        print("/")
    elif Angka3 == Angka1+Angka2:
        print("+")
    else:
        print("Tidak Ada Operasi")
