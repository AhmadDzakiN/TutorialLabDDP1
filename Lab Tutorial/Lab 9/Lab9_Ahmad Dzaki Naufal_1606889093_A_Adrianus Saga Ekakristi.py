from tkinter import *

class BetaMart():
    def __init__(self):
        window = Tk()
        window.title("Beta Mart")
        frame1 = Frame(window)
        frame1.pack()
        frame2 = Frame(window)
        frame2.pack()
        canvas = Canvas(frame1, width = 200, height = 150)
        canvas.create_oval(10,10,140,120, fill="cyan", activefill="White")
        canvas.create_text(75,65, text="Beta Mart", font="Times 20 bold")
        canvas.create_text(75,90, text="Murah Bgt", font="Times 10 bold")
        canvas.pack()
        
        
        self.Ctrl1 = IntVar()
        self.Ctrl2 = IntVar()
        self.Ctrl3 = IntVar()
        cbt1 = Checkbutton(frame2, text = "Beras", variable = self.Ctrl1)
        cbt2 = Checkbutton(frame2, text = "Indomie", variable = self.Ctrl2)
        cbt3 = Checkbutton(frame2, text = "Nutrilion", variable = self.Ctrl3)
        cbt1.grid(row=2, column=1)
        cbt2.grid(row=3, column=1)
        cbt3.grid(row=4, column=1)

        self.Ctrl4 = IntVar()
        rb1 = Radiobutton(frame2, text = "Dengan Kantong Plastik", bg = "red", variable = self.Ctrl4, value = 1)
        rb2 = Radiobutton(frame2, text = "Tanpa Kantong Plastik", bg = "yellow", variable = self.Ctrl4, value = 2)
        rb1.grid(row=5,column=2)
        rb2.grid(row=6,column=2)


        self.Ctrl5 = IntVar()
        self.Ctrl6 = IntVar()
        self.Ctrl7 = IntVar()
        self.ent1 = Entry(frame2, textvariable = self.Ctrl5, bg="Grey")
        self.ent2 = Entry(frame2, textvariable = self.Ctrl6, bg="Grey")
        self.ent3 = Entry(frame2, textvariable = self.Ctrl7, bg="Grey")
        self.ent1.grid(row=2, column=3, padx=10)
        self.ent2.grid(row=3, column=3, padx=10)
        self.ent3.grid(row=4, column=3, padx=10)

        bt = Button(frame2, text = "Hitung", bg = "Green", command= self.jumlah)
        bt.grid(row=7, column=2)

        lbl1 = Label(frame2, text= "30000")
        lbl2 = Label(frame2, text= "3000")
        lbl3 = Label(frame2, text= "130000")
        self.lbl4 = Label(frame2, text= "Total:")
        lbl1.grid(row=2, column=2)
        lbl2.grid(row=3, column=2)
        lbl3.grid(row=4, column=2)
        self.lbl4.grid(row=8, column=2)


    def jumlah(self):
        total = 0
        if self.Ctrl1.get() == 1:
            total += int(self.ent1.get())*30000
        if self.Ctrl2.get() == 1:
            total += int(self.ent2.get())*3000
        if self.Ctrl3.get() == 1:
            total += int(self.ent3.get())*130000
        if self.Ctrl4.get() == 1:
            total+=200
        self.lbl4["text"]="Total {}".format(total)
        

BetaMart()
