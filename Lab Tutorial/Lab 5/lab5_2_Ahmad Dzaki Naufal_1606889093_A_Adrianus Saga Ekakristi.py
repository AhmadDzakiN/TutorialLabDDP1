dict1={}
lst=[]
name=input("Masukan Nama: ")

jml=int(input("Total Buah Dan Harga: "))
for x in range(jml):
    ket=input("Buah dan Harga: ")
    ket2=ket.split(" ")
    dict2={ket2[0]:ket2[1]}
    dict1.update(dict2)

jml2=int(input("Jumlah Buah Yang Akan Dibeli: "))
for x in range(jml2):
    nama=input("Masukan Buah Yang Akan Dibeli: ")
    lst.append(int(dict1[nama]))
print("\nHarga Yang Harus Dibayar Oleh",name,"Adalah: ",sum(lst))
