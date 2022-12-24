from tkinter import *
from tkinter import ttk


class GUI(Tk):
    """The Graphical user Interface for the program"""

    def __init__(self):
        super(GUI, self).__init__()
        self.title("Encription & Decryption")
        self.geometry("800x800")
        # self.configure(bg="gray")
        self.resizable(0,0)
        self.minsize(640, 400)
        self.algorithms = ["OTP", "3DES", "AES"]

        #Right Frames

        ### colomun 1
        self.encript = ttk.LabelFrame(self, text="Encryption", borderwidth=0,width=40, height= 10)
        self.encript.grid(row=0,column=0, padx=20, pady=0)
        self.ftitle = Label(self.encript, text="Message to Encrypt")
        self.ftitle.pack(side=TOP)
        self.ff = ttk.LabelFrame(self.encript,)
        self.textbox1 = Text(self.encript, width=40, height=10,bg="grey")
        self.textbox1.pack()
        
        
        self.rsecond_row = ttk.LabelFrame(self,width=400, height= 10)
        self.rsecond_row.grid(row=1,column=0, padx=0, pady=0)
        self.label = Label(self.rsecond_row, text="Encryption Key", fg="Red",borderwidth=0)
        self.label.grid(row=0,column=0)
        self.label = Entry(self.rsecond_row,width=32, bg="grey")
        self.label.grid(row=0,column=1, padx=20)
        self.encrypt = Button(self.rsecond_row,text="Encrypt", fg="white", bg="blue")
        self.encrypt.grid(row=2, column=0, padx= 0, pady= 20)
        self.Copyencrypt = Button(self.rsecond_row,text="Copy Encryption", fg="white", bg="green")
        self.Copyencrypt.grid(row=2, column=1, padx= 0, pady= 20)


        self.Encrypted_text = ttk.LabelFrame(self, borderwidth=0,width=40, height= 10)
        self.Encrypted_text.grid(row=2,column=0, padx=20, pady=0)
        self.h_s = Scrollbar(self.Encrypted_text, orient='horizontal')
        self.h_s.pack(side=BOTTOM,fill=X)
        self.display_box1 = Text(self.Encrypted_text, width=40, height=10, wrap=NONE,xscrollcommand=self.h_s.set,bg="grey")
        self.display_box1.pack()

        ### column 2
        self.decrypt = ttk.LabelFrame(self, text="Decryption", borderwidth=0,width=40, height= 10)
        self.decrypt.grid(row=0,column=1, padx=20, pady=0)
        self.label = Label(self.decrypt, text="Message to Decrypt")
        self.label.pack(side=TOP)
        self.h_s = Scrollbar(self.decrypt, orient='horizontal')
        self.h_s.pack(side=BOTTOM,fill=X)
        self.textbox1 = Text(self.decrypt, width=40, height=10, wrap=NONE,xscrollcommand=self.h_s.set,bg="grey")
        self.textbox1.pack()

        self.lsecond_row = ttk.LabelFrame(self,width=400, height= 10)
        self.lsecond_row.grid(row=1,column=1, padx=2, pady=0)
        self.label = Label(self.lsecond_row, text="Decription Key", fg="Red",borderwidth=0)
        self.label.grid(row=0,column=0)
        self.label = Entry(self.lsecond_row,width=32)
        self.label.grid(row=0,column=1, padx=20)
        self.encrypt = Button(self.lsecond_row,text="Decrypt", fg="white", bg="blue")
        self.encrypt.grid(row=2, column=0, padx= 0, pady= 20)
        self.Copyencrypt = Button(self.lsecond_row,text="Copy Decryption", fg="white", bg="green")
        self.Copyencrypt.grid(row=2, column=1, padx= 0, pady= 20)

        self.Decrypted_text = ttk.LabelFrame(self, borderwidth=0,width=40, height= 10, bg="grey")
        self.Decrypted_text.grid(row=2,column=1, padx=20, pady=0)
        self.Displaybox2 = Text(self.Decrypted_text, width=40, height=10)
        self.Displaybox2.pack()


        #bottom of screen
        self.bottom = ttk.LabelFrame(self,width=400, height= 10)
        self.bottom.grid(row=3,column=0, padx=20, pady=0)
        self.label = Label(self.bottom, text="Choose Algorithms")
        self.label.grid(row=0,column=0)
        self.combo_box = ttk.Combobox(self.bottom,value=self.algorithms)
        self.combo_box.grid(row=0,column=1, padx=20)
        
        



if __name__ == "__main__":
    window = GUI()
    window.mainloop()