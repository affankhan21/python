from tkinter import *
from tkinter import messagebox
if __name__ == '__main__':
    def multiply():
        num1=int(t1.get())
        num2=int(t2.get())
        ans=num1*num2
        t1.delete(0,END)
        t2.delete(0,END)
        l3.configure(text="multiplication is "+str(ans))
        t1.focus()


wind = Tk()
wind.geometry("600x600")
wind.title("my program")
wind.config(bg="#FFCDD2")
t1=Entry(wind)
t2=Entry(wind)
btn=Button(wind,text="MULTIPLICATION",command=multiply)
l1=Label(wind,text="ENTER FIRST NUMBER")
l2=Label(wind,text="ENTER SECOND NUMBER")
l3=Label(wind)

l1.grid(row=1,column=1)

t1.grid(row=1,column=2)

l2.grid(row=2,column=1)

t2.grid(row=2,column=2)

btn.grid(row=3,column=2)
l3.grid(row=4,column=2)






wind.mainloop()