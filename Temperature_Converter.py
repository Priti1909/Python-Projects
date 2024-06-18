
from tkinter import *
root = Tk()
root.title("Temperature Converter")
root['bg']='yellow'

text= Label(root,text='Temperature Converter !',font=('Brush Script Std',35),bg='yellow')
text.place(x=450,y=20)

h1=Label(root,text='Temperature in Celcius :- ',font=('Cambria',25,'bold'),bg='yellow')
h1.place(x=300,y=194)

h2=Label(root,text='Temperature in Kelvin :- ',font=('Cambria',25,'bold'),bg='yellow')
h2.place(x=300,y=290)

scl = Scale(root,from_=0,to=100,length=300,orient=HORIZONTAL,font=('arial',20))
scl.place(x=680,y=190)

def sclget():
    h2.config(text='Temperature in Kelvin :- '+ str(scl.get() + 273.15)+ 'K')

button = Button(root,text='Convert',font=('arial',15),bg='cyan',activebackground='blue',command=sclget)
button.place(x=1010,y=190)

root.mainloop()