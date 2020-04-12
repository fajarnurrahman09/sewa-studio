from tkinter import *


class DemoLogin:
    def __init__(self, induk, judul):

        self.induk = induk

        self.induk.title(judul)
        self.aturKomponen()

        self.entUser.focus_set()

    def aturKomponen(self):

        # atur frame utama
        frameUtama = Frame(self.induk, bd=20)
        frameUtama.pack(fill=BOTH, expand=YES)

        # atur frame data
        frData = Frame(frameUtama, bd=10)
        frData.pack(fill=BOTH, expand=YES)

        # atur input username
        Label(frData, text='Username:').grid(row=0, column=0, sticky=W)
        self.entUser = Entry(frData)
        self.entUser.grid(row=0, column=1)

        # atur input password
        Label(frData, text='Password:').grid(row=1, column=0, sticky=W)
        self.entPass = Entry(frData, show='*')
        self.entPass.grid(row=1, column=1)

        # atur frame tombol
        frTombol = Frame(frameUtama, bd=5)
        frTombol.pack(fill=BOTH, expand=YES)

        # atur tombol login
        self.btnLogin = Button(frTombol, text='Login', command=self.prosesLogin)
        self.btnLogin.pack(side=LEFT, fill=BOTH, expand=YES)

        self.btnBatal = Button(frTombol, text='Batal', command=self.Tutup)
        self.btnBatal.pack(side=LEFT, fill=BOTH, expand=YES)

    def prosesLogin(self, event=None):
        # ambil data input dari pengguna
        nmUser = self.entUser.get()
        passUser = self.entPass.get()
        print("Berhasil Login!!!")


    def lihatPassword(self, event=None):
        nilaiCek = self.cek.get()

        if nilaiCek == 1:
            self.entPass['show'] = ''
        else:
            self.entPass['show'] = '*'

    def Tutup(self, event=None):
        self.induk.destroy()

    def Hapus(self, event=None):
        self.entUser.delete(0, END)
        self.entPass.delete(0, END)
        self.entUser.focus_set()


if __name__ == '__main__':
    root = Tk()

    header = Frame(root, bg='black', height=20, )
    header.pack(side=TOP, fill=X)
    ST = Label(root, text="Studio", bg="blue", fg="black")
    ST.pack(side=RIGHT, fill=Y)

    status = Label(root, text = "Silahkan Hubungi Operator...", bd = 1, relief = SUNKEN, anchor = W)
    status.pack(side = BOTTOM, fill = X)

    labelframe = LabelFrame(root,text = "Silahkan Login")
    labelframe.pack(fill = "both", expand = "yes")

    left = Label(labelframe, text = "Aplikasi Sewa Studio", fg = "black")
    left.pack()

    app = DemoLogin(root, "SEWA STUDIO")

    root.mainloop()
