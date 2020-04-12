from tkinter import*

class Pelanggan:
    def __init__(self, induk, judul):
        self.induk = induk
        self.induk.title(judul)

    def Edata(self):
        frameUtama = Frame(self.induk, bd = 20)
        frameUtama.pack(fill = "both", expand = "yes")

        frData = Frame(frameUtama, bd = 10)
        frData.pack(fill = "both", expand = "yes")

        #atur inpit data
        Label(frData, text = "Nama ").grid(row = 0, column = 0, sticky = W)
        self.entnama = Entry(frData)
        self.entnama.grid(row = 0, column = 1)

        Label(frData, text = "Tanggal Sewa ").grid(row = 1, column = 0, sticky = W)
        self.enttg = Entry(frData)
        self.enttg.grid(row = 1, column = 1)

        Label(frData, text = "jam sewa ").grid(row = 2, column = 0, sticky = W)
        self.jamw = Entry(frData)
        self.jamw.grid(row = 2, column = 1)

        Label(frData, text="lama sewa ").grid(row=3, column=0, sticky=W)
        self.lamaw = Entry(frData)
        self.lamaw.grid(row=3, column=1)


        Label(frData, text="no telepon ").grid(row=4, column=0, sticky=W)
        self.ntlp = Entry(frData)
        self.ntlp.grid(row=4, column=1)

        #atur tombol save
        frTombol = Frame(frameUtama, bd = 10)
        frTombol.pack(fill = BOTH, expand = YES)

        self.btnsave = Button(frTombol, text = "Save Data", command = self.ProsesLogin)
        self.btnsave.pack(side = LEFT, fill = BOTH, expand = YES)

    def ProsesLogin(self, event=None):
        print ("berhasil menyimpan data!!!")

    def Tutup(self, event = None):
        self.induk.destroy()

    def Hapus(self, event = None):
        self.entnama.delete(0, END)
        self.enttg.delete(0, END)
        self.jamw.delete(0, END)
        self.lamaw.delete(0, END)
        self.ntlp.delete(0, END)
        self.entnama.focus_set()

if __name__== "__main__":
    root = Tk()

    header = Frame(root, bg='black', height=20,)
    header.pack(side=TOP, fill=X)
    ST = Label(root, text="Studio", bg="blue", fg="black")
    ST.pack(side=RIGHT, fill=Y)

    labelframe = LabelFrame(root, text = "Aplikasi Sewa Studio")
    labelframe.pack(fill = 'both', expand = 'yes')

    left = Label(labelframe, text = "Masukan Data Untuk Menyewa Studio")
    left.pack()

    status = Label(root, text="Masukan Data Dengan Benar!!!", bd=1, relief=SUNKEN, anchor=W)
    status.pack(side=BOTTOM, fill=X)

    app = Pelanggan(root, "SEWA STUDIO")
    app.Edata()

    root.mainloop()
