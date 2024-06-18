from cgitb import text
from itertools import count


def labelslider():
    global count , sliderword
    text = 'Welcome To Typing Speed Tester !!!'
    if(count >= len(text)):
        count = 0
        sliderword = ''
    sliderword += text[count]
    count += 1
    fontlabel.configure(text=sliderword)
    fontlabel.after(150,labelslider)


def timer():
    global timeleft,score,miss
    if(timeleft>=11):
        pass
    else:
        timerlabelcount.configure(fg='Red')

    if(timeleft>0):
        timeleft -= 1
        timerlabelcount.configure(text=timeleft)
        timerlabelcount.after(1000,timer)
    else:
        playdetaillabel.configure(text='Hit = {} | Missed = {} | Total ={}'.format(score, miss, score - miss))
        rr = messagebox.askretrycancel('Notification','For Test Again, Select Retry')
        if(rr==True):
            score = 0
            timeleft = 60
            miss = 0
            timerlabelcount.configure(text=timeleft)
            wordlabel.configure(text=words[0])
            scorelabelcount.configure(text=score)


def starttester(event):
    global score,miss
    if(timeleft == 60):
        timer()
    playdetaillabel.configure(text='')
    if(wordentry.get() == wordlabel['text']):
        score += 1
        scorelabelcount.configure(text=score)
       # print('Score => ',score)
    else:
        miss += 1
       # print('Missed => ',miss)
    random.shuffle(words)
    wordlabel.configure(text=words[0])    
    wordentry.delete(0,END)


from tkinter import *
import random
from tkinter import messagebox

root = Tk()
root.geometry('800x600+400+100')
root.configure(bg='black')
root.title('Typing Speed Tester')

score = 0
timeleft = 60
count = 0
sliderword = ''
miss = 0
words = ['Name','Fan','Top','Water' ,'Mango','Apple','Orange','Banana','Table','Grapes','Pizza','Okay','Never',
          'Tv','House','Ram','Hacker','Mobile','Slider','Dextop','Builds','Air','Hotels','Plate','Gate',
          'Net','work','Acid','Change','Plane','Boat','Swim','Nice','Press','Hello','Chess','Sell','Note',
          'Code','Birth','Date','Bag','Dress','Guess','Mail','Spray','Move','Shift','Back','Man','dog',
          'Cow','Cat','Rate','Plant','Lion','Women','Hand','Leg','Head','Face','Milk','Door','Mate','Empty']


fontlabel = Label(root,text='',font=('lucida calligraphy',25,'bold'), bg='black',fg='blue',width=30)
fontlabel.place(x=10,y=10)
labelslider()

random.shuffle(words)

wordlabel = Label(root, text=words[0],font=('Agency FB',40,'bold'),bg='black',fg='green',justify='center')
wordlabel.place(x=330,y=200)

scorelabel = Label(root, text='Your Score : ',font=('aerial',25,'underline bold'),bg='black',fg='sky blue')
scorelabel.place(x=10,y=100)
scorelabelcount = Label(root,text=score,font=('aerial',25,'italic bold'),bg='black',fg='yellow')
scorelabelcount.place(x=80,y=180)

timerlabel = Label(root, text='Time Left : ',font=('aerial',25,'underline bold'),bg='black',fg='sky blue')
timerlabel.place(x=600,y=100)
timerlabelcount = Label(root,text=timeleft,font=('aerial',25,'italic bold'),bg='black',fg='yellow')
timerlabelcount.place(x=680,y=170)

playdetaillabel = Label(root, text='Type Word And Hit Enter',font=('algerian',25,'bold'),bg='Black',fg='white')
playdetaillabel.place(x=190,y=450)

wordentry = Entry(root,font=('aerial',25,'bold'),bd=10,justify='center')
wordentry.place(x=225, y=300)
wordentry.focus_set()


root.bind('<Return>',starttester)
root.mainloop()