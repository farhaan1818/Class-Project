from tkinter import*
from PIL import Image,ImageTk
import csv
from datetime import datetime
import mysql.connector
from mysql.connector import Error
import cv2

class Face_Reconition_main:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x850+0+0")
        self.root.title("Face Recognition System")

        img=Image.open("6385146.jpg")
        img=img.resize((1500,650))
        self.photoimg=ImageTk.PhotoImage(img)
        label_face_recognition=Label(self.root,image=self.photoimg,bg="black",borderwidth=5, relief=SUNKEN)
        label_face_recognition.place(x=0,y=200,width=1500,height=650)

        img_train=Image.open("face_detection.jpg")
        img_train=img_train.resize((1500,200))
        self.photoimg23=ImageTk.PhotoImage(img_train)
        label4=Label(self.root,image=self.photoimg23,bg="black",borderwidth=5, relief=SUNKEN)
        label4.place(x=0,y=0,width=1500,height=200)

        # ================face_recognition button==============
        img3=Image.open("face-detect.png")
        img3=img3.resize((320,220))
        self.photoimg3=ImageTk.PhotoImage(img3)
        btn3=Button(label_face_recognition,command=self.face_detect,image=self.photoimg3,bg="black",borderwidth=5, relief=SUNKEN)
        btn3.place(x=620,y=200,width=220,height=220)
        btn3=Button(label_face_recognition,command=self.face_detect,text="Face Detection",bg="black",borderwidth=5, relief=SUNKEN,fg="white")
        btn3.place(x=620,y=400,width=220,height=40)
        
    # ================Attendance Mark Function=====================
    def mark_attendance(self, i, r, n, j):
        if isinstance(i, tuple):
            i = i[0]
        if isinstance(r, tuple):
            r = r[0]
        if isinstance(n, tuple):
            n = n[0]
        if isinstance(j, tuple):
            j = j[0]
        i, r, n, j = str(i), str(r), str(n), str(j)
        now = datetime.now()
        date = now.strftime("%d/%m/%Y")
        time = now.strftime("%H:%M:%S")
        # Open the file in append mode to add only new data
        with open("attendance.csv", "a", newline="") as f:
            writer = csv.writer(f)
        # Read existing entries to check if the data is already present
            with open("attendance.csv", "r", newline="") as read_f:
                existing_data = csv.reader(read_f)
                name_list = [(row[0] , row[5])for row in existing_data if len(row) > 0 and row[5]==date]       
        # Check if the student's ID, roll number, name, and class are already recorded
            if  date not in name_list and i not in name_list and r not in name_list and n not in name_list and j not in name_list:
                now = datetime.now()
                date = now.strftime("%d/%m/%Y")
                time = now.strftime("%H:%M:%S")
            # Write the new attendance record as a single row
            if (i, date) not in name_list:
                writer.writerow([i, r, n, j, time, date, "Present"])

    # ==================Face Recognition Function========================
    def face_detect(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(grey_img, scaleFactor, minNeighbors)
            coord = []
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                id, predict = clf.predict(grey_img[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))
                print(f"Detected ID: {id}, Confidence: {confidence}")
                try:
                    # Connect to the database
                    connection = mysql.connector.connect(host="localhost",user="root",password="123456",database="face_recognition")
                    cursor = connection.cursor()
                    # Execute queries to fetch data
                    cursor.execute("SELECT stu_name FROM student_data WHERE stu_id = %s", (id,))
                    name_result = cursor.fetchone()
                    name = name_result[0] if name_result else "Unknown"
                    cursor.execute("SELECT roll_no FROM student_data WHERE stu_id = %s", (id,))
                    roll_result = cursor.fetchone()
                    roll_no = roll_result[0] if roll_result else "Unknown"
                    cursor.execute("SELECT Class FROM student_data WHERE stu_id = %s", (id,))
                    class_result = cursor.fetchone()
                    student_class = class_result[0] if class_result else "Unknown"
                except Error as e:
                    print(f"Error while connecting to database: {e}")
                finally:
                    if connection.is_connected():
                        cursor.close()
                        connection.close()

                # Display data if confidence is >77
                if confidence > 77:
                    cv2.putText(img, f"ID: {id}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.7, color, 1)
                    cv2.putText(img, f"Roll: {roll_no}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.7, color, 1)
                    cv2.putText(img, f"Name: {name}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.7, color, 1)
                    cv2.putText(img, f"Class: {student_class}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.7, color, 1)
                    self.mark_attendance(id, roll_no, name, student_class)
                else:
                    cv2.putText(img, "Unknown", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 2, color, 2)
                coord = [x, y, w, h]
            return coord
        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        video_camera = cv2.VideoCapture(0)
        while True:
            ret, img = video_camera.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Face Recognition", img)
            if cv2.waitKey(1) == 13:
                break
        video_camera.release()
        cv2.destroyAllWindows()

if  __name__ == "__main__":
    root = Tk()
    obj = Face_Reconition_main(root)
    root.mainloop()