from tkinter import *
if __name__ == '__main__':

    wind = Tk()
    wind.geometry("600x600")
    wind.title("my program")
    wind.config(bg="#FDD835")
    t1=Entry(wind)
    t2=Entry(wind)
    btn=Button(wind,text="Add")
    l1=Label(wind,text="ENTER FIRST NUMBER")
    l2=Label(wind,text="ENTER SECOND NUMBER")

    l1.pack()
    l2.pack()
    t1.pack()
    t2.pack()
    btn.pack()
    

    wind.mainloop()