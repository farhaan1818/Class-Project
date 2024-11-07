from tkinter import*
from PIL import Image,ImageTk

class developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x850+0+0")
        self.root.minsize(1500,850)
        self.root.maxsize(1500,850)
        self.root.title("Developer")

        img=Image.open("6385146.jpg")
        img=img.resize((1500,650))
        self.photoimg=ImageTk.PhotoImage(img)
        label_train=Label(self.root,image=self.photoimg,bg="black",borderwidth=5, relief=SUNKEN)
        label_train.place(x=0,y=200,width=1500,height=650)

        img_train=Image.open("dev.jpg")
        img_train=img_train.resize((1500,200))
        self.photoimg23=ImageTk.PhotoImage(img_train)
        label4=Label(self.root,image=self.photoimg23,bg="black",borderwidth=5, relief=SUNKEN)
        label4.place(x=0,y=0,width=1500,height=200)

        #==========Data Train Button==========
        # ===================Farhan==============================
        img2=Image.open("Farhan.jpg")
        img2=img2.resize((220,220))
        self.photoimg2=ImageTk.PhotoImage(img2)
        btn2=Button(label_train,image=self.photoimg2,bg="black",fg="white",borderwidth=5,relief=SUNKEN)
        btn2.place(x=350,y=150,width=220,height=220)
        btn2=Button(label_train,text="Farhan Akhtar Khan",bg="black",fg="white",borderwidth=5,relief=SUNKEN)
        btn2.place(x=350,y=370,width=220,height=40)

        # =========================Ankit=========================
        img3=Image.open("Ankit.jpg")
        img3=img3.resize((220,220))
        self.photoimg3=ImageTk.PhotoImage(img3)
        btn3=Button(label_train,image=self.photoimg3,bg="black",fg="white",borderwidth=5,relief=SUNKEN)
        btn3.place(x=650,y=150,width=220,height=220)
        btn3=Button(label_train,text="Ankit Prajapati",bg="black",fg="white",borderwidth=5,relief=SUNKEN)
        btn3.place(x=650,y=370,width=220,height=40)
        
        # =======================Ashutosh========================
        img4=Image.open("Ashu.jpg")
        img4=img4.resize((220,220))
        self.photoimg4=ImageTk.PhotoImage(img4)
        btn4=Button(label_train,image=self.photoimg4,bg="black",fg="white",borderwidth=5,relief=SUNKEN)
        btn4.place(x=950,y=150,width=220,height=220)
        btn4=Button(label_train,text="Ashutosh Yadav",bg="black",fg="white",borderwidth=5,relief=SUNKEN)
        btn4.place(x=950,y=370,width=220,height=40) 

if  __name__ == "__main__":
    root = Tk()
    obj = developer(root)
    root.mainloop()
