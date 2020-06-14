jumlah=int(input("Masukan Jumlah: "))
email=[]
domain={}
for z in range(jumlah):
    mail=input("Masukan Email: ")
    mail = mail.split("@")
    email.append(mail[1])
for z in email:
    domain[z] = domain.get(z,0) + 1
for z in domain:
    print(domain[z], "address dengan domain", z)
    
