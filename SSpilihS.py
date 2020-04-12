from tkinter import*

class Pstudio:
    def __init__(self, induk, judul):
        self.induk = induk
        self.induk.title(judul)

    def pilihS(self):
        scrollbar = Scrollbar()
        scrollbar.pack(side=RIGHT, fill=Y)

        mylist = Listbox( yscrollcommand=scrollbar.set)
        for line in range(10):
            mylist.insert(END, "Studio" +" "+ str(line))


        mylist.pack(side=LEFT, fill=BOTH)
        scrollbar.config(command=mylist.yview)

        self.btnLogin = Button( text='Save Studio', command=self.prosesLogin)
        self.btnLogin.pack(side=BOTTOM,  expand=YES)

    def prosesLogin(self, event=None):
        print("Studio Berhasil Dipilih!!!")

if __name__== "__main__":
    root = Tk()

    header = Frame(root, bg='black', height=20,)
    header.pack(side=TOP, fill=X)
    ST = Label(root, text="Studio", bg="blue", fg="black")
    ST.pack(side=RIGHT, fill=Y)

    labelframe = LabelFrame(root, text = "Aplikasi Sewa Studio")
    labelframe.pack(fill = 'both', expand = 'yes')

    left = Label(labelframe, text = "Silahka Pilih Studio")
    left.pack()

    status = Label(root, text="Studio yg sudah dipilih tidak dapat diganti !!!", bd=1, relief=SUNKEN, anchor=W)
    status.pack(side=BOTTOM, fill=X)

    app = Pstudio(root, "SEWA STUDIO")
    app.pilihS()

    root.mainloop()