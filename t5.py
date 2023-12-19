from tkinter import *
from tkinter import messagebox
if __name__ == '__main__':
    def add():
        num1=int(t1.get())
        num2=int(t2.get())
        ans=num1+num2
        t1.delete(0,END)
        t2.delete(0,END)
        messagebox.showinfo(title="output",message="addition is "+str(ans))


wind = Tk()
wind.geometry("600x600")
wind.title("my program")
wind.config(bg="#F5DEB3")
t1=Entry(wind)
t2=Entry(wind)
btn=Button(wind,text="Add",command=add)
l1=Label(wind,text="ENTER FIRST NUMBER")
l2=Label(wind,text="ENTER SECOND NUMBER")

l1.grid(row=1,column=1)

t1.grid(row=1,column=2)

l2.grid(row=2,column=1)

t2.grid(row=2,column=2)

btn.grid(row=3,column=2)






wind.mainloop()