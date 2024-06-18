from email.mime import application
from tkinter import *
from datetime import datetime
import tkinter.messagebox
from turtle import width

class CalDate:

    def __init__(self,root):
        self.root = root
        self.root.title("Days Calculator")
        self.root.geometry("1300x750+0+0")
        self.root.configure(background = "Black")

        mainframe = Frame(self.root)
        mainframe.grid()

        topmain1 = Frame(mainframe, bd=14,width=1350,height=550,pady=10,padx=10,relief=RIDGE,bg="black")
        topmain1.grid(row=4, column=2) 
        
        topmain2 = Frame(topmain1, bd=14,width=1300,height=500,pady=10,padx=10,relief=RIDGE,bg="black")
        topmain2.grid(row=4, column=2) 

        topmain3 = Frame(topmain2, bd=14,width=1250,height=450,pady=10,padx=10,relief=RIDGE,bg="black")
        topmain3.grid(row=4, column=2) 

        topframe = Frame(topmain3, bd=14,width=1200,height=400,pady=10,padx=10,relief=RIDGE,bg="black")
        topframe.grid(row=4, column=2) 
         
        def iexit():
            iexit=tkinter.messagebox.askyesno("Days Calculator","Confirm if you want to exit")
            if iexit > 0:
                root.destroy()
                return

        def ireset():
            CheckInDate.set("")
            CheckOutDate.set("")
            TotalDays.set("")

        def idate():
            d1 = CheckInDate.get()
            d2 = CheckOutDate.get()
            d1 = datetime.strptime(d1,"%d/%m/%Y")
            d2 = datetime.strptime(d2,"%d/%m/%Y")
            TotalDays.set(abs((d2 - d1).days))

        CheckInDate=StringVar()
        CheckOutDate=StringVar()
        TotalDays=StringVar()

        self.lblTitle = Label(topframe,font=('Brush Script Std',40,'bold'),text="Days Calculator",padx=2,pady=2,
                                       bg="black",fg="white")
        self.lblTitle.grid(row=0,column=0,columnspan=4)       

        self.lblCheck_in_date = Label(topframe,font=('Cambria',24,'bold'),text="Check In date : ",padx=2,pady=2,
                                       bg="black",fg="white") 
        self.lblCheck_in_date.grid(row=1,column=0,sticky=W) 

        self.txtCheck_in_date = Entry(topframe,font=('Cambria',24,'bold'),textvariable=CheckInDate ,bd= 7,width=41)                              
        self.txtCheck_in_date.grid(row=1,column=1,padx=21,pady=4,columnspan=3)  

        self.lblCheck_out_date = Label(topframe,font=('Cambria',24,'bold'),text="Check Out date : ",padx=2,pady=2,
                                       bg="black",fg="white")  
        self.lblCheck_out_date.grid(row=2,column=0,sticky=W)

        self.txtCheck_out_date = Entry(topframe,font=('Cambria',24,'bold'),textvariable=CheckOutDate ,bd= 7,width=41)                              
        self.txtCheck_out_date.grid(row=2,column=1,padx=21,pady=4,columnspan=3)   

        self.lblTotalCost = Label(topframe,font=('Cambria',24,'bold'),text="Calculated Days : ",bd=7,bg="black",fg="white") 
        self.lblTotalCost.grid(row=3,column=0,sticky=W) 
        self.txtTotalCost = Entry(topframe,font=('Cambria',24,'bold'),textvariable=TotalDays,bd= 7,width=41)                              
        self.txtTotalCost.grid(row=3,column=1,padx=21,pady=9,columnspan=3) 

        self.btnTotal= Button(topframe,padx=16,pady=9,bd=4,fg="red",font=('Trajan Pro',24,'bold'),width=10,height=1,bg="black",text="Total",command=idate).grid(row=5,column=1,padx=4)

        self.btnReset= Button(topframe,padx=16,pady=9,bd=4,fg="red",font=('Trajan Pro',24,'bold'),width=10,height=1,bg="black",text="Reset",command=ireset).grid(row=5,column=2,padx=5)

        self.btnExit= Button(topframe,padx=16,pady=9,bd=4,fg="red",font=('Trajan Pro',24,'bold'),width=10,height=1,bg="black",text="Exit",command=iexit).grid(row=5,column=3,padx=5)

if __name__=='__main__':
    root= Tk()
    application= CalDate(root)
    root.mainloop()    
