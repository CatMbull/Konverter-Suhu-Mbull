import sys
import tkinter as tk 
from tkinter import *


def value1 () :
    a = float(num1.get())
    b = int (4/5 * a)
    label1 = Label(root,bg='#FFA500', text = "Reamur : %.i °R" % b).pack(side = BOTTOM)
    return

def value2 () :
    a = float(num1.get())
    b = int (a + 273);
    c = int (9.0 / 5.0);
    d = int (c * b);
    label1 = Label(root,bg='#FFA500', text = "Kelvin : %.i °K" % b).pack(side = BOTTOM)
    return

root=tk.Tk()
root.title ("Suhu Converter")
root.geometry('450x450+400+150')

canvas =tk.Canvas(root,bg='#BCC6CC')
canvas.place(relwidth=7, relheight=7)

num1 = StringVar()
radbtn = StringVar()
radbtn.set(None)

frame = tk.Frame(root, bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.90, relheight=0.15, anchor='n')

frame2 = tk.Frame(root,bg='#FFA500', bd=10, padx=16, pady=16, relief=RAISED)
frame2.place(relx=0.5, rely=0.3, relwidth=0.5, relheight=0.27,anchor='n')

label2 = tk.Label(root, bg= '#FFA500', text= "konversi suhu °C", fg="white", relief=RAISED, font=('arial',14,"bold"))
label2.pack(side=TOP)

txtdisplay = tk.Entry(frame, bg='#FFA500', textvariable= num1,bd=18, insertwidth=0.6, font=('arial',15,"bold"))
txtdisplay.place(relwidth=0.65, relheight=1)

label3 =tk.Label(root, bg= '#FFA500',padx=16, pady=16, bd=8, text= "°C", fg="white", relief=RAISED, font=('arial',30,"bold"))
label3.place(relx=0.7,rely=0.110, relheight=0.125, relwidth=0.2)

radio1 = Radiobutton(frame2, bg='#FFA500', text="konversi °R", variable=radbtn, value="REAMUR", command=value1, font=('arial',10,"bold")).pack(side=TOP)
radio1 = Radiobutton(frame2, bg='#FFA500', text="konversi °K", variable=radbtn, value="KELVIN", command=value2, font=('arial',10,"bold")).pack(side=TOP)

root.mainloop()

###Buatan Mbull, by mbull, for mbull, with mbull###


