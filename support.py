from tkinter import*
from PIL import Image,ImageTk
import webbrowser

class Helpsupport:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1500x850+0+0")
        self.root.minsize(1500,850)
        self.root.maxsize(1500,850)
        self.root.title("Face Recognition System")

        img=Image.open("6385146.jpg")
        img=img.resize((1500,650))
        self.photoimg=ImageTk.PhotoImage(img)
        label_support=Label(self.root,image=self.photoimg,bg="black",borderwidth=5, relief=SUNKEN)
        label_support.place(x=0,y=200,width=1500,height=650)

        img_support=Image.open("main_banner.jpg")
        img_support=img_support.resize((1500,200))
        self.photoimg23=ImageTk.PhotoImage(img_support)
        label4=Label(self.root,image=self.photoimg23,bg="black",borderwidth=5, relief=SUNKEN)
        label4.place(x=0,y=0,width=1500,height=200)

        # =============================X=========================
        img2=Image.open("x.png")
        img2=img2.resize((220,220))
        self.photoimg2=ImageTk.PhotoImage(img2)
        btn2=Button(label_support,command=self.x,image=self.photoimg2,bg="black",fg="white",borderwidth=5,relief=SUNKEN)
        btn2.place(x=200,y=150,width=220,height=220)
        btn2=Button(label_support,command=self.x,text="X",bg="black",fg="white",borderwidth=5,relief=SUNKEN)
        btn2.place(x=200,y=370,width=220,height=40)

        # ========================Instagram=======================
        img3=Image.open("insta.jpg")
        img3=img3.resize((220,220))
        self.photoimg3=ImageTk.PhotoImage(img3)
        btn3=Button(label_support,command=self.insta,image=self.photoimg3,bg="black",fg="white",borderwidth=5,relief=SUNKEN)
        btn3.place(x=500,y=150,width=220,height=220)
        btn3=Button(label_support,command=self.insta,text="Instagram",bg="black",fg="white",borderwidth=5,relief=SUNKEN)
        btn3.place(x=500,y=370,width=220,height=40)

        # =========================Gmail==========================
        img4=Image.open("mail.jpg")
        img4=img4.resize((220,220))
        self.photoimg4=ImageTk.PhotoImage(img4)
        btn4=Button(label_support,command=self.gmail,image=self.photoimg4,bg="black",fg="white",borderwidth=5,relief=SUNKEN)
        btn4.place(x=800,y=150,width=220,height=220)
        btn3=Button(label_support,command=self.gmail,text="Gmail",bg="black",fg="white",borderwidth=5,relief=SUNKEN)
        btn3.place(x=800,y=370,width=220,height=40)
        
        # =====================Github==============================
        img5=Image.open("github.png")
        img5=img5.resize((220,220))
        self.photoimg5=ImageTk.PhotoImage(img5)
        btn5=Button(label_support,command=self.github,image=self.photoimg5,bg="black",fg="white",borderwidth=5,relief=SUNKEN)
        btn5.place(x=1100,y=150,width=220,height=220)
        btn5=Button(label_support,command=self.github,text="Github",bg="black",fg="white",borderwidth=5,relief=SUNKEN)
        btn5.place(x=1100,y=370,width=220,height=40)
    
    # ======================Funtions========================
    def x(self):
        self.new = 1
        self.url = "https://x.com/"
        webbrowser.open(self.url,new=self.new)
    
    def insta(self):
        self.new = 1
        self.url = "https://www.instagram.com/"
        webbrowser.open(self.url,new=self.new)
    
    def gmail(self):
        self.new = 1
        self.url = "mailto:teamattendancemanagementsystem@gmail.com"
        webbrowser.open(self.url,new=self.new)
    
    def github(self):
        self.new = 1
        self.url = "https://www.github.com"
        webbrowser.open(self.url,new=self.new)

if __name__ == "__main__":
    root=Tk()
    obj=Helpsupport(root)
    root.mainloop()