from tkinter import*
from PIL import Image,ImageTk
from student import student
import os
from train import train_data
from face_recognition import Face_Reconition_main
from attendance import Attendance_main
from support import Helpsupport
from developer import developer

class Face_Reconition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x850+0+0")
        self.root.title("Landing Page")

        img=Image.open("6385146.jpg")
        img=img.resize((1500,650))
        self.photoimg=ImageTk.PhotoImage(img)
        label1=Label(self.root,image=self.photoimg,bg="black",borderwidth=5, relief=SUNKEN)
        label1.place(x=0,y=200,width=1500,height=650)

        img23=Image.open("attend_manage.jpg")
        img23=img23.resize((1500,200))
        self.photoimg23=ImageTk.PhotoImage(img23)
        label4=Label(self.root,image=self.photoimg23,bg="black",borderwidth=5, relief=SUNKEN)
        label4.place(x=0,y=0,width=1500,height=200)

        # =============student details button=========
        img2=Image.open("stud.jpg")
        img2=img2.resize((320,220))
        self.photoimg2=ImageTk.PhotoImage(img2)
        btn2=Button(label1,image=self.photoimg2,command=self.student_details,bg="black",fg="white",borderwidth=5,relief=SUNKEN)
        btn2.place(x=200,y=50,width=220,height=220)
        btn2=Button(label1,text="Students Details",command=self.student_details,bg="black",fg="white",borderwidth=5,relief=SUNKEN)
        btn2.place(x=200,y=250,width=220,height=40)

        #============ face recognition button==========
        img3=Image.open("face-detect.png")
        img3=img3.resize((320,220))
        self.photoimg3=ImageTk.PhotoImage(img3)
        btn3=Button(label1,command=self.face_check,image=self.photoimg3,bg="black",fg="white",borderwidth=5,relief=SUNKEN)
        btn3.place(x=500,y=50,width=220,height=220)
        btn3=Button(label1,command=self.face_check,text="Face Detection",bg="black",fg="white",borderwidth=5,relief=SUNKEN)
        btn3.place(x=500,y=250,width=220,height=40)

        #==========Attendance Record Button=============
        img4=Image.open("attendance.jpg")
        img4=img4.resize((320,220))
        self.photoimg4=ImageTk.PhotoImage(img4)
        btn4=Button(label1,command=self.stu_attendance,image=self.photoimg4,bg="black",borderwidth=5,relief=SUNKEN)
        btn4.place(x=800,y=50,width=220,height=220)
        btn4=Button(label1,text="Attendance",bg="black",fg="white",borderwidth=5,relief=SUNKEN)
        btn4.place(x=800,y=250,width=220,height=40)

        # =================Help Button===================
        img5=Image.open("help.jpg")
        img5=img5.resize((320,220))
        self.photoimg5=ImageTk.PhotoImage(img5)
        btn5=Button(label1,command=self.support,image=self.photoimg5,bg="black",fg="white",borderwidth=5,relief=SUNKEN)
        btn5.place(x=1100,y=50,width=220,height=220)
        btn5=Button(label1,command=self.support,text="Support",bg="black",fg="white",borderwidth=5,relief=SUNKEN)
        btn5.place(x=1100,y=250,width=220,height=40)
        # ================Row 1 END======================
        # ==================Row 2 Start==================
        # ===============Train Data Button===============
        img6=Image.open("train.webp")
        img6=img6.resize((320,220))
        self.photoimg6=ImageTk.PhotoImage(img6)
        btn6=Button(label1,command=self.train,image=self.photoimg6,bg="black",fg="white",borderwidth=5,relief=SUNKEN)
        btn6.place(x=200,y=350,width=220,height=220)
        btn6=Button(label1,command=self.train,text="Train Data",bg="black",fg="white",borderwidth=5,relief=SUNKEN)
        btn6.place(x=200,y=550,width=220,height=40)

        # =========Photo Sample Record Button============
        img7=Image.open("photo.png")
        img7=img7.resize((320,220))
        self.photoimg7=ImageTk.PhotoImage(img7)
        btn7=Button(label1,command=self.open_img,image=self.photoimg7,bg="black",fg="white",borderwidth=5,relief=SUNKEN)
        btn7.place(x=500,y=350,width=220,height=220)
        btn7=Button(label1,text="Photos",bg="black",fg="white",borderwidth=5,relief=SUNKEN)
        btn7.place(x=500,y=550,width=220,height=40)

        # ==========Developers Detail Button=============
        img8=Image.open("developer.jpg")
        img8=img8.resize((320,220))
        self.photoimg8=ImageTk.PhotoImage(img8)
        btn8=Button(label1,command=self.developer,image=self.photoimg8,bg="black",fg="white",borderwidth=5,relief=SUNKEN)
        btn8.place(x=800,y=350,width=220,height=220)
        btn8=Button(label1,command=self.developer,text="Developer",bg="black",fg="white",borderwidth=5,relief=SUNKEN)
        btn8.place(x=800,y=550,width=220,height=40)

        # =================Exit Button====================
        img9=Image.open("Exit.jpg")
        img9=img9.resize((320,220))
        self.photoimg9=ImageTk.PhotoImage(img9)
        btn9=Button(label1,image=self.photoimg9,command=self.close_all_windows,bg="black",fg="white",borderwidth=5,relief=SUNKEN)
        btn9.place(x=1100,y=350,width=220,height=220)
        btn9=Button(label1,text="Exit",bg="black",fg="white",borderwidth=5,relief=SUNKEN)
        btn9.place(x=1100,y=550,width=220,height=40)

    # ===================Function====================
    def open_img(self):
      os.startfile("data")

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=student(self.new_window)

    def train(self):
        self.new_window=Toplevel(self.root)
        self.app=train_data(self.new_window)

    def face_check(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Reconition_main(self.new_window)

    def stu_attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance_main(self.new_window)

    def support(self):
        self.new_window=Toplevel(self.root)
        self.app=Helpsupport(self.new_window)

    def developer(self):
        self.new_window=Toplevel(self.root)
        self.app=developer(self.new_window)

    def close_all_windows(self):
        self.root.destroy()

if  __name__ == "__main__":
    root = Tk()
    obj = Face_Reconition_System(root)
    root.mainloop()


