from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import messagebox
from datetime import datetime
import csv
import csv
from datetime import datetime
from collections import defaultdict

class Attendance_main:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x850+0+0")
        self.root.title("Attendance Panel")

        # Background image
        img = Image.open("6385146.jpg")
        img = img.resize((1500, 650))
        self.photoimg = ImageTk.PhotoImage(img)
        label_attendance = Label(self.root, image=self.photoimg, bg="black", borderwidth=5, relief=SUNKEN)
        label_attendance.place(x=0, y=200, width=1500, height=650)

        # Header image
        img_train = Image.open("attend.jpg")
        img_train = img_train.resize((1500, 200))
        self.photoimg23 = ImageTk.PhotoImage(img_train)
        label4 = Label(self.root, image=self.photoimg23, bg="black", borderwidth=5, relief=SUNKEN)
        label4.place(x=0, y=0, width=1500, height=200)

        # Button image for face detection
        img3 = Image.open("banner3.jpg")
        img3 = img3.resize((320, 220))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        # Button to open CSV in Excel
        btn3 = Button(label_attendance, command=self.open_csv_in_excel, image=self.photoimg3,bg="black",borderwidth=5, relief=SUNKEN)
        btn3.place(x=620, y=200, width=220, height=220)

        # Text label button
        btn3_text = Button(label_attendance, command=self.open_csv_in_excel, text="Attendance Record",bg="black",borderwidth=5, relief=SUNKEN,fg="white")
        btn3_text.place(x=620, y=400, width=220, height=40)

    @staticmethod
    def count_monthly_attendance(input_file, output_file):
        attendance_count = defaultdict(int)

        with open(input_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if not row or len(row) < 6:
                    continue
                student_id = row[0]
                try:
                    date = datetime.strptime(row[5], '%d/%m/%Y')
                    month = date.strftime('%Y-%m')
                except ValueError as e:
                    print(f"Skipping row with invalid date format: {row} ({e})")
                    continue
                attendance_count[(student_id, month)] += 1

        with open(output_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['student_id', 'month', 'total_attendance'])
            for (student_id, month), total_attendance in attendance_count.items():
                writer.writerow([student_id, month, total_attendance])

    def open_csv_in_excel(self, file_path="total.csv"):
        try:
            os.startfile(file_path)
            print("File opened successfully in Excel or the default CSV viewer.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

Attendance_main.count_monthly_attendance(r'C:\Users\akhte\Downloads\New folder (6)\attendance.csv', 'total.csv')

if __name__ == "__main__":
    root = Tk()
    obj = Attendance_main(root)
    root.mainloop()
