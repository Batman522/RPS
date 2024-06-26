from tkinter import *
from PIL import ImageTk,Image
from pygame import  mixer
import tkinter.font as font
import time,random

root=Tk()
root.title("Rock Paper Scissors")
#root.iconbitmap('Letter-A-icon_34765.ico')
root.geometry("720x480")
root.config(bg="Firebrick")
root.resizable(0,0)
i=0
my_font=font.Font(family="Helvetica",size=18,weight="bold")
mixer.init()
mixer.music.load("dance-all-day-156448.mp3")
mixer.music.play(loops=50000)

def logic1():
       global l1,l2,l3,b2,l4,b1,p,c,l5,l6,l7,e,l8,l9
       c=random.randint(1,9)
       l1.place_forget()
       l1=Label(image=i1)
       l1.place(x=60,y=150)
       l3.place_forget()
       if c==1 or c==4 or c==7:
        l3=Label(image=i1)
        l3.place(x=480,y=150)
        mixer.init()
        mixer.music.load("draw.wav")
        mixer.music.play()

       elif c==2 or c==5 or c==8:
        l3=Label(image=i2)
        l3.place(x=480,y=150)
        mixer.init()
        mixer.music.load("dailure.mp3")
        mixer.music.play()
        l7.place_forget()
        e+=1
        l7=Label(text=str(e),font=my_font,fg="Red")
        l7.place(x=560,y=80)
       else:
        l3=Label(image=i3)
        l3.place(x=480,y=150)
        mixer.init()
        mixer.music.load("success-1-6297.mp3")
        mixer.music.play()
        l5.place_forget()
        p+=1
        l5=Label(text=str(p),font=my_font,fg="Red")
        l5.place(x=150,y=80)

def logic2():
       global l1,l2,l3,b2,l4,b1,p,c,e,l5,l6,l7,l8,l9,l10
       c=random.randint(1,9)
       l1.place_forget()
       l1=Label(image=i2)
       l1.place(x=60,y=150)
       l3.place_forget()
       if c==1 or c==4 or c==7:
        l3=Label(image=i1)
        l3.place(x=480,y=150)
        mixer.init()
        mixer.music.load("success-1-6297.mp3")
        mixer.music.play()
        l5.place_forget()
        p+=1
        l5=Label(text=str(p),font=my_font,fg="Red")
        l5.place(x=150,y=80)
       elif c==2 or c==5 or c==8:
        l3=Label(image=i2)
        l3.place(x=480,y=150)
        mixer.init()
        mixer.music.load("draw.wav")
        mixer.music.play()
       else:
        l3=Label(image=i3)
        l3.place(x=480,y=150)
        mixer.init()
        mixer.music.load("dailure.mp3")
        mixer.music.play()
        l7.place_forget()
        e+=1
        l7=Label(text=str(e),font=my_font,fg="Red")
        l7.place(x=560,y=80)
def back():
    global l1,l2,l3,b2,l4,b1,p,c,b4,b5,b6,b3,p,e
    mixer.init()
    mixer.music.load("_Cameraclick.mp3")
    mixer.music.play()
    time.sleep(1)
    l1.place_forget()
    l2.place_forget()
    l3.place_forget()
    l4.place_forget()
    b1.place_forget()
    b2.place_forget()
    b4.place_forget()
    b5.place_forget()
    b6.place_forget()
    l5.place_forget()
    l6.place_forget()
    l9.place_forget()
    l7.place_forget()
    l8.place_forget()
    l1=Label(image=i1)
    l1.place(x=60,y=150)
    l2=Label(image=i2)
    l2.place(x=270,y=150)
    l3=Label(image=i3)
    l3.place(x=480,y=150)
    mixer.init()
    mixer.music.load("dance-all-day-156448.mp3")
    mixer.music.play(loops=50000)

    b1=Button(text="PLAY GAME",font=my_font,width=9,bg="Green",highlightcolor="Blue",highlightbackground="Blue",fg="Blue",borderwidth=5,relief="solid",command=play)
    b1.place(x=290,y=340)
    b2=Button(text="QUIT GAME",font=my_font,width=9,bg="Green",highlightcolor="Blue",highlightbackground="Blue",fg="Blue",relief="solid",borderwidth=5,command=quit)
    b2.place(x=290,y=400)
    b3=Button(command=music,image=i4,bg="Green",relief="solid")
    b3.place(x=10,y=10)
    l4=Label(image=i6,bg="Black",relief="sunken")
    l4.place(x=230,y=10)


def logic3():
       global l1,l2,l3,b2,l4,b1,p,c,e,l5,l6,l7,l8,l9,l10
       c=random.randint(1,9)
       l1.place_forget()
       l1=Label(image=i3)
       l1.place(x=60,y=150)
       l3.place_forget()
       if c==1 or c==4 or c==7:
        l3=Label(image=i1)
        l3.place(x=480,y=150)
        mixer.init()
        mixer.music.load("dailure.mp3")
        mixer.music.play()
        l7.place_forget()
        e+=1
        l7=Label(text=str(e),font=my_font,fg="Red")
        l7.place(x=560,y=80)
       elif c==2 or c==5 or c==8:
        l3=Label(image=i2)
        l3.place(x=480,y=150)
        mixer.init()
        mixer.music.load("success-1-6297.mp3")
        mixer.music.play()
        l5.place_forget()
        p+=1
        l5=Label(text=str(p),font=my_font,fg="Red")
        l5.place(x=150,y=80)
       else:
        l3=Label(image=i3)
        l3.place(x=480,y=150)
        mixer.init()
        mixer.music.load("draw.wav")
        mixer.music.play()

def reset():
    global l1,l2,l3,b2,l4,b1,p,c,b5,b6,b4,l5,l6,l7,e
    p=0
    e=0
    mixer.init()
    mixer.music.load("_reset.wav")
    l1.place_forget()
    l3.place_forget()
    l5.place_forget()
    l7.place_forget()
    l1=Label(image=i7)
    l1.place(x=60,y=150)
    l3=Label(image=i7)
    l3.place(x=480,y=150)
    l5=Label(text=str(p),font=my_font,fg="Red")
    l5.place(x=150,y=80)
    l7=Label(text=str(e),font=my_font,fg="Red")
    l7.place(x=560,y=80)

def music():
   global b3,b4,i
   mixer.music.stop()
   i+=1
   b3.place_forget()
   b4=Button(command=music,image=i5,bg="Green")
   b4.place(x=10,y=10)

   if i%2==0:
       b4.place_forget()
       b3=Button(command=music,image=i4,bg="Green")
       b3.place(x=10,y=10)
       mixer.music.play(loops=5000)

def play():
    mixer.init()
    mixer.music.load("play.mp3")
    mixer.music.play()
    global l1,l2,l3,b2,l4,b1,p,c,b5,b6,b4,l5,l6,l7,e,l8,l9,l10
    p=0
    e=0
    time.sleep(1)
    l1.place_forget()
    l2.place_forget()
    l3.place_forget()
    l4.place_forget()
    b1.place_forget()
    b2.place_forget()
    time.sleep(0.5)
    l1=Label(image=i7)
    l1.place(x=60,y=150)
    l2=Label(image=i8)
    l2.place(x=270,y=150)
    l3=Label(image=i7)
    l3.place(x=480,y=150)
    l5=Label(text=str(p),font=my_font,fg="Red")
    l5.place(x=150,y=80)
    l6=Label(text="-SCORE-",font=my_font,bg="Green")
    l6.place(x=310,y=80)
    l7=Label(text=str(e),font=my_font,fg="Red")
    l7.place(x=560,y=80)
    l8=Label(text="PLAYER",font=("Helvetica",15),bg="Blue",relief="solid",borderwidth=5)
    l8.place(x=110,y=40)
    l9=Label(text="COMPUTER",font=("Helvetica",15),bg="Blue",relief="solid",borderwidth=5)
    l9.place(x=510,y=40)
    b1=Button(text="Rock",width=9,font=my_font,command=logic1,relief="solid",borderwidth=5)
    b1.place(x=80,y=340)
    b2=Button(text="Paper",width=9,font=my_font,command=logic2,relief="solid",borderwidth=5)
    b2.place(x=290,y=340)
    b4=Button(text="Scissor",width=9,font=my_font,command=logic3,relief="solid",borderwidth=5)
    b4.place(x=500,y=340)
    b5=Button(text="Reset",width=9,font=my_font,command=reset,relief="solid",borderwidth=5,bg="Red")
    b5.place(x=290,y=420)
    b6=Button(command=back,image=i9,bg="Green",relief="solid")
    b6.place(x=670,y=10)







img1=Image.open("rock.png")
img1=img1.resize((180,140))
img2=Image.open("paper.png")
img2=img2.resize((180,140))
img3=Image.open("scissors.png")
img3=img3.resize((180,140))
img4=Image.open("vol.png")
img4=img4.resize((30,30))
img5=Image.open("nvol.png")
img5=img5.resize((30,30))
img6=Image.open("rpslogp.png")
img6=img6.resize((260,120))
img9=Image.open("bk.png")
img9=img9.resize((30,30))
img10=Image.open("win.jpg")
img10=img10.resize((480,360))
img11=Image.open("lose.png")
img11=img11.resize((480,360))
img12=Image.open("draw.jpg")
img12=img12.resize((480,360))
i1=ImageTk.PhotoImage(img1)
i2=ImageTk.PhotoImage(img2)
i3=ImageTk.PhotoImage(img3)
i4=ImageTk.PhotoImage(img4)
i5=ImageTk.PhotoImage(img5)
i6=ImageTk.PhotoImage(img6)
i10=ImageTk.PhotoImage(img10)
i11=ImageTk.PhotoImage(img11)
i12=ImageTk.PhotoImage(img12)
img7=Image.open("wb.png")
img7=img7.resize((180,140))
img8=Image.open("vsl.png")
img8=img8.resize((180,140))
i7=ImageTk.PhotoImage(img7)
i8=ImageTk.PhotoImage(img8)
i9=ImageTk.PhotoImage(img9)

l1=Label(image=i1)
l1.place(x=60,y=150)
l2=Label(image=i2)
l2.place(x=270,y=150)
l3=Label(image=i3)
l3.place(x=480,y=150)

b1=Button(text="PLAY GAME",font=my_font,width=9,bg="Green",highlightcolor="Blue",highlightbackground="Blue",fg="Blue",borderwidth=5,relief="solid",command=play)
b1.place(x=290,y=340)
b2=Button(text="QUIT GAME",font=my_font,width=9,bg="Green",highlightcolor="Blue",highlightbackground="Blue",fg="Blue",relief="solid",borderwidth=5,command=quit)
b2.place(x=290,y=400)
b3=Button(command=music,image=i4,bg="Green",relief="solid")
b3.place(x=10,y=10)
l4=Label(image=i6,bg="Black",relief="sunken")
l4.place(x=230,y=10)


root.mainloop()