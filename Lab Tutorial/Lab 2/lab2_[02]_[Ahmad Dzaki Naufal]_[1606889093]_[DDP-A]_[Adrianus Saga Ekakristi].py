while True:
	print("Kalkulator Cinta (Free Version)")
	Nama1= input("Masukan Nama: ")
	Nama2= input("Masukan Nama: ")
	if len(Nama1) and len(Nama2) == 4: 
	
		Hasil1= ord(Nama1[0]) + ord(Nama1[1]) + ord(Nama1[2]) + ord(Nama1[3])
		Hasil2= ord(Nama2[0]) + ord(Nama2[1]) + ord(Nama2[2]) + ord(Nama2[3])
		
		x = (Hasil1 + Hasil2)%101
		
		if (x>=85) and (x<=100):
			print("Sangat Cocok")
		elif (x>=70) and (x<=84):
			print("Biasa")
		elif (x>=50) and (x<=69):
			print("Sangat Biasa")
		elif (x>=30) and (x<=49):
			print("Tidak Cocok")
		elif (x>=0) and (x<=29):
			print("Sangat Tidak Cocok")
	else:
		print("Hanya Dapat Memakai 4 Karakter Untuk Free Version")