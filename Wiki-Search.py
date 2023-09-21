from tkinter import *
from PIL import ImageTk, Image
import wikipedia
import pyttsx3 
p=pyttsx3.init()
class Search:
    def __init__(self, win):
        self.lbl1=Label(win, text='Hi! \nWelcome to Wiki Search :) \nEnter the word you wanna search below :',font=('Helvetica 15'),justify='left',bd=3)
        self.lbl1.place(x=0, y=0,height=100,width=700)
        self.t1=Entry(win,bd=3)
        self.t1.place(x=20, y=100,height=50,width=590)
        self.photo = PhotoImage(file = "S.png")
        self.b1=Button(win,image = self.photo,bd=3, command=self.submit)
        self.b1.place(x=630, y=100,height=50,width=50)
    def submit(self):
        x=str(self.t1.get())
        result = wikipedia.summary(x, sentences = 2)
        results=result[:len(result)//9]+'\n'+result[len(result)//9:2*len(result)//9]+'\n'+result[2*len(result)//9:3*len(result)//9]+'\n'+result[3*len(result)//9:4*len(result)//9]+'\n'+result[4*len(result)//9:5*len(result)//9]+'\n'+result[5*len(result)//9:6*len(result)//9]+'\n'+result[6*len(result)//9:7*len(result)//9]+'\n'+result[7*len(result)//9:8*len(result)//9]+'\n'+result[8*len(result)//9:]
        self.lbl1=Label(window, text='Result :',font=('Helvetica 15'),justify='left',bd=3)
        self.lbl1.place(x=20, y=160,height=30,width=650)
        self.lbl2=Label(window, text=results,font=('Helvetica 15'),justify='left',bd=3)
        self.lbl2.place(x=20, y=200,height=220,width=650)
        self.photo2 = PhotoImage(file = "P.png")
        self.b2=Button(window,image = self.photo2,bd=3, command=lambda:self.play(results))
        self.b2.place(x=90, y=450,height=90,width=90)
        self.img = ImageTk.PhotoImage(Image.open("A.jpg"))
        self.lbl3=Label(window,  image = self.img,justify='left',bd=3)
        self.lbl3.place(x=230, y=450,height=90,width=300)
        
    def play(self,a):
        p.say(a)
        p.runAndWait()
        
        


window=Tk()
mywin=Search(window)
window.title('Wiki Search!')
window.geometry("700x560+200+200")
window.mainloop()
