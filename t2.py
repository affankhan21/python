from tkinter import *
if __name__ == '__main__':

    wind = Tk()
    wind.geometry("600x600")
    wind.title("my program")
    wind.config(bg="#FF5733")
    l1=Label(wind,text="MY FIRST PROGRAM")
    l2=Label(wind,text="WELCOME TO PYTHON")
    l3=Label(wind,text="PYTHON IS THE BEST LANGUAGE")
    l4=Label(wind,text="ORGANIZATION WORLD")
    l1.pack(side="right")
    l2.pack(side="left")
    l3.pack(side="top")
    l4.pack(side="bottom")
    

    wind.mainloop()