from tkinter import *

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.master. title("GOMC HUD RPi")

        for r in range(6):
            self.master.rowconfigure(r,weight=1)
        for c in range(5):
            self.master.columnconfigure(c, weight=1)
            Button(master, text="INFO".format(c)).grid(row=6, column=c, sticky=W)
            Button(master, text="Split".format(c)).grid(row=6, column=c, sticky=W+W+W)
            Button(master, text="NAV".format(c)).grid(row=6, column=c, sticky=E)

        navFrame= Frame(master, bg="red")
        navFrame.grid(row = 0, column  = 0, rowspan = 4, columnspan = 4, sticky = W+E+N+S)
        infoFrame= Frame(master, bg="blue")
        infoFrame.grid(row = 3, column  = 0, rowspan = 4, columnspan = 4, sticky = W+E+N+S)
        splitFrame= Frame(master, bg="green")
        splitFrame.grid(row = 0, column  = 2, rowspan = 6, columnspan = 4, sticky = W+E+N+S)

root=Tk()
app = Application(master=root)
app.mainloop()
