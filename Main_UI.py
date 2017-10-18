from tkinter import *

LARGE_FONT = ("Arial" , 12) #decides font for GUI

class HUDRPi(): #inherit from tk

    def __init__(self, *args, **kwargs): #initializing method
        __init__(self, *args, **kwargs ) #initializing tkinter
        container = Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container. grid_rowconfigure(0, weight = 1)
        container. grid_columnconfigure(0, weight = 1)

        self.frames = {}

        mainFrame = Main(container, self)
        navFrame = Navigation(container, self)
        infoFrame = Information(container, self)
        splitFrame = Split(container, self)
        

        self.frames[Navigation] = navFrame
        self.frames[Information] = infoFrame
        self.frames[Split] = splitFrame
        self.frames[Main] = mainFrame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Information)
        self.show_frame(Navigation)
        self.show_frame(Split)
        self.show_frame(Main)

    def show_frame(self, cont):

        frame = self.frames[cont]
       

class main(): #inherits from tk

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, controller)
        label = Label(self, text ="GOMC HUD - Main Menu", font=LARGE_FONT)
        label.pack(pady = 10, padx=10)


app = HUDRPi()
app.mainloop()
