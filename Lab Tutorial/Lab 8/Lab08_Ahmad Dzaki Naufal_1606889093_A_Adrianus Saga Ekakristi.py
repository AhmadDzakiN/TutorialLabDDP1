from tkinter import *

class Kalkulator():
    def __init__(self):
        self.window = Tk()
        self.window.title("Kalkulator Cinta")
        label = Label(self.window, text = "Kalkulator Cinta", fg = "Blue", bg = "Yellow")
        label2 = Label(self.window, text = "Masukan Nama 1:", fg = "Green", bg = "Red")
        label3 = Label(self.window, text = "Masukan Nama 2:", fg = "Green", bg = "Red")
        self.label4 = Label(self.window)
        self.entry1 = Entry(self.window)
        self.entry2 = Entry(self.window)
        button1 = Button(self.window, text = "Calculate", bg = "Pink", fg = "White", command = self.pressed)
        button2 = Button(self.window, text = "Exit", bg = "Pink", fg = "White", command = self.quitz)

        label["font"] = "Times 40 bold"
        label2["font"] = "Times 20 bold"
        label3["font"] = "Times 20 bold"

        label.grid(row=0, column=0)
        label2.grid(row=1, column=0)
        label3.grid(row=2, column=0)
        self.label4.grid(row=3, column=0)
        self.entry1.grid(row=1, column=1)
        self.entry2.grid(row=2, column=1)
        button1.grid(row=4, column=0)
        button2.grid(row=4, column=1)
        self.window.mainloop()

    def pressed(self):
        Nama1 = (self.entry1.get())
        Nama2 = (self.entry2.get())
        a = 0
        b = 0
        total1 = 0
        total2 = 0

        while a < len(Nama1):
                ordnama1 = ord(Nama1[a])
                total1+=ordnama1
                a+=1
        while b < len(Nama2):
                ordnama2 = ord(Nama2[b])
                total2+= ordnama2
                b+=1

        x = ((total1) + (total2)) % 101
        if (x>=85) and (x<=100):
                self.label4["text"] = "{} dan {} Memiliki Skor {} dengan Kategori Sangat Cocok".format(Nama1, Nama2, x)
        elif (x>=70) and (x<=84):
                self.label4["text"] = "{} dan {} Memilki Skor {} dengan Kategori Sangat Biasa".format(Nama1, Nama2, x)
        elif (x>=50) and (x<=69):
                self.label4["text"] = "{} dan {} Memiliki Skor {} dengan Kategori Biasa".format(Nama1, Nama2, x)
        elif (x>=30) and (x<=49):
                self.label4["text"] = "{} dan {} Memiliki Skor {} dengan Kategori Tidak Cocok".format(Nama1, Nama2, x)
        elif (x>=0) and (x<=29):
                self.label4["text"] = "{} dan {} Memiliki Skor {} dengan Kategori  Sangat Tidak Cocok".format(Nama1, Nama2, x)

        
    def quitz(self):
        messagebox.showinfo(message = "Terima Kasih Telah Memakai Applikasi Ini. Semoga Harimu Menyenangkan")
        self.window.destroy()

        

   
coba = Kalkulator()

