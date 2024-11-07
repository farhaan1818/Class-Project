from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
import os
import numpy as n 
import cv2

class train_data:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x850+0+0")
        self.root.minsize(1500,850)
        self.root.maxsize(1500,850)
        self.root.title("Train Dataset")

        img=Image.open("6385146.jpg")
        img=img.resize((1500,650))
        self.photoimg=ImageTk.PhotoImage(img)
        label_train=Label(self.root,image=self.photoimg,bg="black",borderwidth=5, relief=SUNKEN)
        label_train.place(x=0,y=200,width=1500,height=650)

        img_train=Image.open("sample_train.jpg")
        img_train=img_train.resize((1500,200))
        self.photoimg23=ImageTk.PhotoImage(img_train)
        label4=Label(self.root,image=self.photoimg23,bg="black",borderwidth=5, relief=SUNKEN)
        label4.place(x=0,y=0,width=1500,height=200)

        #==========Data Train Button==========
        img2=Image.open("train.png")
        img2=img2.resize((320,220))
        self.photoimg2=ImageTk.PhotoImage(img2)
        btn2=Button(label_train,command=self.train_data,image=self.photoimg2,bg="black",borderwidth=5, relief=SUNKEN)
        btn2.place(x=650,y=200,width=220,height=220)
        btn2=Button(label_train,command=self.train_data,text="Train Dataset",bg="black",borderwidth=5, relief=SUNKEN,fg="white")
        btn2.place(x=650,y=400,width=220,height=40)

    # ===============Data Train Function================
    def train_data(self):
        data_path=("data")
        path=[os.path.join(data_path,file) for file in os.listdir(data_path)]
        faces=[]
        ides=[]

        for  i in path:
            img=Image.open(i).convert("L")
            # img=face_recognition.load_image_file(i)
            image_numpy=n.array(img,"uint8")
            id=int(os.path.split(i)[1].split('.')[1])
            faces.append(image_numpy)
            ides.append(id)
            cv2.imshow("Training",image_numpy)
            cv2.waitKey(1)==13
        ides=n.array(ides)

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ides)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Done","Done")

if  __name__ == "__main__":
    root = Tk()
    obj = train_data(root)
    root.mainloop()
