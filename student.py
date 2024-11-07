from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x900+0+0")
        self.root.title("Student  Management System")
        # =============Label1_Background image===================
        img=Image.open("6385146.jpg")
        img=img.resize((1500,700))
        self.photoimg=ImageTk.PhotoImage(img)
        label1=Label(self.root,image=self.photoimg,bg="black",borderwidth=5, relief=SUNKEN)
        label1.place(x=0,y=200,width=1500,height=700)

        # ====================Heading banner======================
        img_train=Image.open("stu_detail.jpg")
        img_train=img_train.resize((1500,200))
        self.photoimg23=ImageTk.PhotoImage(img_train)
        label4=Label(self.root,image=self.photoimg23,bg="black",borderwidth=5, relief=SUNKEN)
        label4.place(x=0,y=0,width=1500,height=200)

        # =========Variables for storing Students details==========
        self.var_class=StringVar()
        self.var_section=StringVar()
        self.var_stream=StringVar()
        self.var_optional_sub=StringVar()
        self.var_stu_id=StringVar()
        self.var_stu_name=StringVar()
        self.var_session=StringVar()
        self.var_roll_no=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_contact=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_radio1=StringVar()
        
        # ==================Main frame =================
        main_frame=Frame(label1,bd=2,bg="white")
        main_frame.place(x=20,y=20,width=1450,height=650)

        # ================left label====================
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RAISED,text="Student Details",font=("Times New Roman",15,"bold"))
        left_frame.place(x=10,y=10 ,width=700,height=630)

        # ===============Course Frame===================
        course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RAISED,text="Course Details",font=("Times New Roman",15,"bold"))
        course_frame.place(x=10,y=10 ,width=670,height=150)

        # ====================Class===================== 
        class_label=Label(course_frame,text="Class",font=("Times New Roman",15,"bold"),bg="white")
        class_label.grid(row=0,column=0,padx=10,pady=10)
        class_combo=ttk.Combobox(course_frame,textvariable=self.var_class,font=("Times New Roman",15,"bold"),width=17,state="readonly")
        class_combo["values"]=("Select Class","1","2","3","4","5","6","7","8","9","10","11","12")
        class_combo.current(0)
        class_combo.grid(row=0,column=1,padx=10,pady=10)

        # ====================Section===================
        class_label=Label(course_frame,text="Section",font=("Times New Roman",15,"bold"),bg="white")        
        class_label.grid(row=0,column=2,padx=10,pady=10,sticky=W)
        class_combo=ttk.Combobox(course_frame,textvariable=self.var_section,font=("Times New Roman",15,"bold"),width=17,state="readonly")
        class_combo["values"]=("Select Section","A","B","C","D","E","F","G","H")
        class_combo.current(0)
        class_combo.grid(row=0,column=3,padx=10,pady=10,sticky=W)

        # =====================Stream====================
        class_label=Label(course_frame,text="Stream",font=("Times New Roman",15,"bold"),bg="white")        
        class_label.grid(row=1,column=0,padx=10,pady=10)
        class_combo=ttk.Combobox(course_frame,textvariable=self.var_stream,font=("Times New Roman",15,"bold"),width=17,state="readonly")
        class_combo["values"]=("Select Stream","PCM","PCB","Arts","None")
        class_combo.current(0)
        class_combo.grid(row=1,column=1,padx=10,pady=10)

        # ============Optional Subject===================
        class_label=Label(course_frame,text="Optional Sub",font=("Times New Roman",15,"bold"),bg="white")       
        class_label.grid(row=1,column=2,padx=10,pady=10,sticky=W)
        class_combo=ttk.Combobox(course_frame,textvariable=self.var_optional_sub,font=("Times New Roman",15,"bold"),width=17,state="readonly")
        class_combo["values"]=("Select Optional","Computer Science","Hindi","Not Applicable")
        class_combo.current(0)
        class_combo.grid(row=1,column=3,padx=10,pady=10,sticky=W)

        # ===============Student info Frame==============
        student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RAISED,text="Class Student Information",font=("Times New Roman",15,"bold"))
        student_frame.place(x=10,y=180,width=670,height=400)

        # ==================Student id===================
        student_id=Label(student_frame,text="StudentID:",font=("Times New Roman",15,"bold"),bg="white" )
        student_id.grid(row=0,column=0,padx=10,pady=10)
        student_id_entry=ttk.Entry(student_frame,textvariable=self.var_stu_id,width=16,font=("Times New Roman",15,"bold"))
        student_id_entry.grid(row=0,column=1,padx=10,pady=10)
       
        # =================Student_name==================
        student_name=Label(student_frame,text="Student Name:",font=("Times New Roman",15,"bold"),bg="white" )
        student_name.grid(row=0,column=2,padx=10,pady=10)
        student_name_entry=ttk.Entry(student_frame,textvariable=self.var_stu_name,width=16,font=("Times New Roman",15,"bold"))
        student_name_entry.grid(row=0,column=3,padx=10,pady=10)

        # ==================Session===================== 
        student_addmission_year=Label(student_frame,text="Session:",font=("Times New Roman",15,"bold"),bg="white" )
        student_addmission_year.grid(row=1,column=0,padx=10,pady=10)
        student_addmission_year_entry=ttk.Entry(student_frame,textvariable=self.var_session,width=16,font=("Times New Roman",15,"bold"))
        student_addmission_year_entry.grid(row=1,column=1,padx=10,pady=10)

        # ================Roll Number===================
        student_roll_no=Label(student_frame,text="Roll No.:",font=("Times New Roman",15,"bold"),bg="white" )
        student_roll_no.grid(row=1,column=2,padx=10,pady=10)
        student_roll_no_entry=ttk.Entry(student_frame,textvariable=self.var_roll_no,width=16,font=("Times New Roman",15,"bold"))
        student_roll_no_entry.grid(row=1,column=3,padx=10,pady=10)

        # ===================Gender=====================
        student_gender=Label(student_frame,text="Gender:",font=("Times New Roman",15,"bold"),bg="white" )
        student_gender.grid(row=2,column=0,padx=10,pady=10)
        gender_combo=ttk.Combobox(student_frame,textvariable=self.var_gender,font=("Times New Roman",15,"bold"),width=14,state="readonly")
        gender_combo["values"]=("Select Gender","Male","Female","Rcbians")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        # ====================DOB======================= 
        student_dob=Label(student_frame,text="D.O.B.:",font=("Times New Roman",15,"bold"),bg="white" )
        student_dob.grid(row=2,column=2,padx=10,pady=10)
        student_dob_entry=ttk.Entry(student_frame,textvariable=self.var_dob,width=16,font=("Times New Roman",15,"bold"))
        student_dob_entry.grid(row=2,column=3,padx=10,pady=10)

        # ====================Email=====================
        student_email=Label(student_frame,text="Email:",font=("Times New Roman",15,"bold"),bg="white" )
        student_email.grid(row=3,column=0,padx=10,pady=10)
        student_email_entry=ttk.Entry(student_frame,textvariable=self.var_email,width=16,font=("Times New Roman",15,"bold"))
        student_email_entry.grid(row=3,column=1,padx=10,pady=10)

        # =================Phone Number================= 
        student_phone=Label(student_frame,text="Contact:",font=("Times New Roman",15,"bold"),bg="white" )
        student_phone.grid(row=3,column=2,padx=10,pady=10)
        student_phone_entry=ttk.Entry(student_frame,textvariable=self.var_contact,width=16,font=("Times New Roman",15,"bold"))
        student_phone_entry.grid(row=3,column=3,padx=10,pady=10)

        # ===================Address====================
        student_address=Label(student_frame,text="Address:",font=("Times New Roman",15,"bold"),bg="white" )
        student_address.grid(row=4,column=0,padx=10,pady=10)
        student_address_entry=ttk.Entry(student_frame,textvariable=self.var_address,width=16,font=("Times New Roman",15,"bold"))
        student_address_entry.grid(row=4,column=1,padx=10,pady=10)

        # ================Class Teacher=================
        student_teacher=Label(student_frame,text="Class Teacher:",font=("Times New Roman",15,"bold"),bg="white" )
        student_teacher.grid(row=4,column=2,padx=10,pady=10)
        student_teacher_entry=ttk.Entry(student_frame,textvariable=self.var_teacher,width=16,font=("Times New Roman",15,"bold"))
        student_teacher_entry.grid(row=4,column=3,padx=10,pady=10)

        # =================Radio Buttons================ 
        # ==============Take Student Photo==============
        radio1=ttk.Radiobutton(student_frame,variable=self.var_radio1,text="Take Student Photo",value="yes")
        radio1.grid(row=5,column=0,padx=10,pady=10)
        # ================No Student Photo==============
        radio2=ttk.Radiobutton(student_frame,variable=self.var_radio1,text="No Student Photo",value="no")
        radio2.grid(row=5,column=1,padx=10,pady=10)

        # ===========Opretions Buttons Frame============
        btn_frame=Frame(student_frame,bg="white",bd=0)
        btn_frame.place(x=20,y=280,height=80,width=620)

        # ===================Save Button=================
        img1=Image.open("save.png")
        img1=img1.resize((70,70))
        self.photoimg1=ImageTk.PhotoImage(img1)
        btn1=Button(btn_frame,command=self.add_data,image=self.photoimg1,bg="white",bd=0)
        btn1.grid(row=0,column=0,padx=25,pady=0)

        #  ==================Update Button===============
        img2=Image.open("update.png")
        img2=img2.resize((70,70))
        self.photoimg2=ImageTk.PhotoImage(img2)
        btn2=Button(btn_frame,command=self.update_data,image=self.photoimg2,bg="white",bd=0)
        btn2.grid(row=0,column=1,padx=25,pady=0)

        #  ==================Delete Button================
        img3=Image.open("delete.png")
        img3=img3.resize((70,70))
        self.photoimg3=ImageTk.PhotoImage(img3)
        btn3=Button(btn_frame,command=self.delete_data,image=self.photoimg3,bg="white",bd=0)
        btn3.grid(row=0,column=2,padx=25,pady=0)

        #  ===================Reset Button=================
        img4=Image.open("reset.png")
        img4=img4.resize((70,70))
        self.photoimg4=ImageTk.PhotoImage(img4)
        btn4=Button(btn_frame,command=self.reset,image=self.photoimg4,bg="white",bd=0)
        btn4.grid(row=0,column=3,padx=25,pady=0)

        #  ===============Take Photo Button================
        img5=Image.open("take photo.png")
        img5=img5.resize((70,70))
        self.photoimg5=ImageTk.PhotoImage(img5)
        btn5=Button(btn_frame,command=self.dataset,image=self.photoimg5,bg="white",bd=0)
        btn5.grid(row=0,column=5,padx=25,pady=0)
        # ============Left Label Frame END===================

        # ============Right Label Frame Starts===============
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RAISED,text="Search Student Details",font=("Times New Roman",15,"bold"))
        right_frame.place(x=730,y=10 ,width=700,height=630)

        # =================Detail Table Frame====================
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RAISED)
        table_frame.place(x=10,y=20 ,width=670,height=560)

        # ======================Detail Scroll=====================
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,columns=("class","section","stream","optional_sub","stu_id","stu_name","session","roll_no","gender","dob","email","contact","address","class_teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        # ===================Column Heading=======================
        self.student_table.heading("class",text="Class")
        self.student_table.heading("section",text="Section")
        self.student_table.heading("stream",text="Stream")
        self.student_table.heading("optional_sub",text="Optional")
        self.student_table.heading("stu_id",text="Student_id")  
        self.student_table.heading("stu_name",text="Student Name")
        self.student_table.heading("session",text="Session")
        self.student_table.heading("roll_no",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("contact",text="Contact")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("class_teacher",text="Class Teacher")
        self.student_table.heading("photo",text="Photo")
        self.student_table["show"]="headings"
      
        # ======================Column Width======================
        self.student_table.column("class",width=100)
        self.student_table.column("section",width=100)
        self.student_table.column("stream",width=100)
        self.student_table.column("optional_sub",width=100)
        self.student_table.column("stu_id",width=100)
        self.student_table.column("stu_name",width=100)
        self.student_table.column("session",width=100)
        self.student_table.column("roll_no",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("contact",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("class_teacher",width=100)
        self.student_table.column("photo",width=100)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        # ==============Fetch data Calling=======================
        self.fetch_data()

    #  ======================= Add Data Function=================
    def add_data(self):
        if self.var_class.get()=="Select Class" or self.var_stu_id.get()=="" or self.var_stu_name.get()=="":
          messagebox.showerror("Error","All field should be filled")
        else:
            try:
                connetion=mysql.connector.connect(host="localhost",user="root",password=str(123456),port=3306,database="face_recognition")
                my_cursor=connetion.cursor()
                my_cursor.execute("insert into student_data values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                  self.var_class.get(),
                  self.var_section.get(),
                  self.var_stream.get(),
                  self.var_optional_sub.get(),
                  self.var_stu_id.get(),
                  self.var_stu_name.get(),
                  self.var_session.get(),
                  self.var_roll_no.get(),
                  self.var_gender.get(),
                  self.var_dob.get(),
                  self.var_email.get(),
                  self.var_contact.get(),
                  self.var_address.get(),
                  self.var_teacher.get(),
                  self.var_radio1.get()))
                connetion.commit()
                self.fetch_data()
                connetion.close()
                messagebox.showinfo("Success","Your Data Inserted Successfully")
            except Exception as e:
              messagebox.showerror("Error",f"Due to {str(e)}")
                
    # =================Fetch Data Function=========================
    def fetch_data(self):
      connetion=mysql.connector.connect(host="localhost",user="root",password=str(123456),port=3306,database="face_recognition")
      my_cursor=connetion.cursor()
      my_cursor.execute("Select * from student_data")
      data=my_cursor.fetchall()
      if len(data) != 0:
        self.student_table.delete(*self.student_table.get_children())
        for i in data:
          self.student_table.insert("",END,values=i)
        connetion.commit()
      connetion.close()

    # ==================Get cursor Function========================
    def get_cursor(self,event=None):
      cursor_focus=self.student_table.focus()
      content=self.student_table.item(cursor_focus)
      data=content["values"]
      if data:
        self.var_class.set(data[0])
      else:
        self.var_class.set('')
        print("Warning: No data available to set var_class.")
      self.var_section.set(data[1])
      self.var_stream.set(data[2])
      self.var_optional_sub.set(data[3])
      self.var_stu_id.set(data[4])
      self.var_stu_name.set(data[5])
      self.var_session.set(data[6])
      self.var_roll_no.set(data[7])
      self.var_gender.set(data[8])
      self.var_dob.set(data[9])
      self.var_email.set(data[10])
      self.var_contact.set(data[11])
      self.var_address.set(data[12])
      self.var_teacher.set(data[13])
      self.var_radio1.set(data[14])
      
    # =====================Data Update Function====================
    def update_data(self):
      if self.var_class.get()=="Select Class" or self.var_stu_id.get()=="" or self.var_stu_name.get()=="":
          messagebox.showerror("Error","All field should be filled")
      else:
        try:
          update_msg=messagebox.askyesno("update","Do you want to update")
          if update_msg>0:
            connetion=mysql.connector.connect(host="localhost",user="root",password=str(123456),port=3306,database="face_recognition")
            my_cursor=connetion.cursor()
            my_cursor.execute("update student_data set Class=%s,section=%s,stream=%s,optional=%s,stu_name=%s,session=%s,roll_no=%s,gender=%s,dob=%s,email=%s,contact=%s,address=%s,teacher=%s,photo=%s where stu_id=%s",(
                  self.var_class.get(),
                  self.var_section.get(),
                  self.var_stream.get(),
                  self.var_optional_sub.get(),
                  self.var_stu_name.get(),
                  self.var_session.get(),
                  self.var_roll_no.get(),
                  self.var_gender.get(),
                  self.var_dob.get(),
                  self.var_email.get(),
                  self.var_contact.get(),
                  self.var_address.get(),
                  self.var_teacher.get(),
                  self.var_radio1.get(),
                  self.var_stu_id.get()
                  ) ) 
          else:
            if not update_msg:
              return  
          messagebox.showinfo("Success","Your data Updated Successfully")
          connetion.commit()
          self.fetch_data()
          connetion.close()
        except Exception as e:
          messagebox.showerror("Error",f"Error{e}")

    #=============Delete Function==================
    def delete_data(self):
      if self.var_stu_id.get()=="":
        messagebox.showerror("Error","Student id must be required")
      else:
        try:
          delete_msg=messagebox.askyesno("delete","Do you want to delete")
          if delete_msg>0:
            connetion=mysql.connector.connect(host="localhost",user="root",password=str(123456),port=3306,database="face_recognition")
            my_cursor=connetion.cursor()
            query="delete from student_data where stu_id=%s"
            value=(self.var_stu_id.get(),)
            my_cursor.execute(query,value)
          else:
            if not delete_msg:
              return
          connetion.commit()
          self.fetch_data()
          connetion.close()
          messagebox.showinfo("Delete","Successfully deleted")
        except Exception as e:
          messagebox.showerror("Error",f"Error{e}")

    #=================Data Reset Function===================
    def reset(self):
      self.var_class.set("Select Class")
      self.var_section.set("Select Section")
      self.var_stream.set("Select Stream")
      self.var_optional_sub.set("Select Optional")
      self.var_stu_id.set("")
      self.var_stu_name.set("")
      self.var_session.set("")
      self.var_roll_no.set("")
      self.var_gender.set("Select Gender ")
      self.var_dob.set("")
      self.var_email.set("")
      self.var_contact.set("")
      self.var_address.set("")
      self.var_teacher.set("")
      self.var_radio1.set("")

    # ================Image Data Function=====================
    def dataset(self):
      if self.var_stu_id.get() == "":
          messagebox.showerror("Error", "Select Class and Stream")
      else:
          try:
              connection = mysql.connector.connect(
                  host="localhost", user="root", password="123456", port=3306, database="face_recognition"
              )
              my_cursor = connection.cursor()
              stu_id = self.var_stu_id.get()
              my_cursor.execute(
                  "UPDATE student_data SET Class=%s, section=%s, stream=%s, optional=%s, stu_name=%s, session=%s, roll_no=%s, gender=%s, dob=%s, email=%s, contact=%s, address=%s, teacher=%s, photo=%s WHERE stu_id=%s",
                  (
                      self.var_class.get(),
                      self.var_section.get(),
                      self.var_stream.get(),
                      self.var_optional_sub.get(),
                      self.var_stu_name.get(),
                      self.var_session.get(),
                      self.var_roll_no.get(),
                      self.var_gender.get(),
                      self.var_dob.get(),
                      self.var_email.get(),
                      self.var_contact.get(),
                      self.var_address.get(),
                      self.var_teacher.get(),
                      self.var_radio1.get(),
                      stu_id,
                  ),
              )
              connection.commit()
              self.fetch_data()
              self.reset()
              connection.close()

              face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
              # ===============Image cropping Function======================
              def cropped_img(img):
                  gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                  faces = face_classifier.detectMultiScale(gray_img, 1.3, 5)
                  for (x, y, w, h) in faces:
                      return img[y:y + h, x:x + w]
                  return None 
              # ============Web Cam Accessing================
              cap = cv2.VideoCapture(0)
              img_id = 0
              while True:
                  ret, my_frame = cap.read()
                  if not ret:
                      break
                  face = cropped_img(my_frame)
                  if face is not None:
                      img_id += 1
                      face = cv2.resize(face, (450, 450))
                      face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                      file_name = f"data/user.{stu_id}.{img_id}.jpg"
                      cv2.imwrite(file_name, face)
                      cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (98, 233, 169), 2)
                      cv2.imshow("Cropped_face", face)
                  if cv2.waitKey(1) == 13 or img_id == 100:
                      break
              cap.release()
              cv2.destroyAllWindows()
              messagebox.showinfo("Result", "Success")
          except Exception as e:
              messagebox.showerror("Error", str(e))

if  __name__ == "__main__":
    root = Tk()
    obj = student(root)
    root.mainloop()