filein = input("File Input: ")
fileout = input("File Output: ")

money = []

y = open(filein, 'r')
z = open(fileout, 'w')

for wew in y :
    q = wew.split()
    if q[1] == "Underwater" or q[1] == "underwater":
        print("Sultan Menangkap", q[0], "dengan Diveball", file = z)
        money.append(5000)
    elif q[1] == "Cave" or q[1] == "cave":
        print("Sultan Menangkap", q[0], "dengan Duskball", file = z)
        money.append(7500)
    elif q[1] == "Park" or q[1] == "park":
        print("Sultan Menangkap", q[0], "dengan Parkball", file = z)
        money.append(8000)
    elif q[1] == "Jungle" or q[1] == "jungle":
        print("Sultan Menangkap", q[0], "dengan Netball", file = z)
        money.append(2500)
    elif q[1] == "Gym" or q[1] == "gym":
        print("Sultan Menangkap", q[0], "dengan Sportball", file = z)
        money.append(9000)
    else:
        print("Sultan Menangkap", q[0], "dengan Ghokeball", file = z)
        money.append(1000)
print("Sultan Harus Mengeluarkan Uang Sebanyak ", sum(money), file = z)
y.close()
z.close()
