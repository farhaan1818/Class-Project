import cv2
import numpy as np

# Load the image
image_path = r"C:\Users\akhte\Downloads\New folder (6)\exit.jpg"
image = cv2.imread(image_path)

# Step 1: Confirm if the image is loaded correctly
if image is None:
    print("Error: Image not loaded. Please check the image path.")
else:
    print("Image loaded successfully")

# Step 2: Check if the image is a NumPy array
print("Image type:", type(image))
print("Image shape:", image.shape if isinstance(image, np.ndarray) else "Not an ndarray")

# Step 3: Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print("Grayscale conversion successful")

# Step 4: Load the face cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
if face_cascade.empty():
    print("Error: Cascade classifier not loaded. Check the path to haarcascade.")
else:
    print("Cascade classifier loaded successfully")

# Step 5: Attempt face detection
try:
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    print("Faces detected:", len(faces))
except Exception as e:
    print("Error during face detection:", e)












































    # def dataset(self):
    #   if self.var_stu_id.get() == "":
    #       messagebox.showerror("Error", "Select Class and Stream")
    #   else:
    #       try:
    #           connection = mysql.connector.connect(
    #               host="localhost", user="root", password="123456", port=3306, database="face_recognition"
    #           )
    #           my_cursor = connection.cursor()
    #           my_cursor.execute("SELECT * FROM student_data")
    #           my_result = my_cursor.fetchall()

    #           for student_record in my_result:
    #               stu_id = student_record[4]  # Assuming stu_id is the first column in `student_data`
    #               my_cursor.execute(
    #                   "UPDATE student_data SET Class=%s, section=%s, stream=%s, optional=%s, stu_name=%s, session=%s, roll_no=%s, gender=%s, dob=%s, email=%s, contact=%s, address=%s, teacher=%s, photo=%s WHERE stu_id=%s",
    #                   (
    #                       self.var_class.get(),
    #                       self.var_section.get(),
    #                       self.var_stream.get(),
    #                       self.var_optional_sub.get(),
    #                       self.var_stu_name.get(),
    #                       self.var_session.get(),
    #                       self.var_roll_no.get(),
    #                       self.var_gender.get(),
    #                       self.var_dob.get(),
    #                       self.var_email.get(),
    #                       self.var_contact.get(),
    #                       self.var_address.get(),
    #                       self.var_teacher.get(),
    #                       self.var_radio1.get(),
    #                       stu_id,  # Corrected to use the actual student ID
    #                   ),
    #               )
    #           connection.commit()
    #           self.fetch_data()
    #           self.reset()
    #           connection.close()

    #           # ==============================================================

    #           face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    #           def cropped_img(img):
    #               gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #               faces = face_classifier.detectMultiScale(gray_img, 1.3, 5)
    #               for (x, y, w, h) in faces:
    #                   return img[y:y + h, x:x + w]  # Return the cropped face
    #               return None  # Return None if no face is detected

    #           cap = cv2.VideoCapture(0)
    #           img_id = 0
    #           while True:
    #               ret, my_frame = cap.read()
    #               if not ret:
    #                   break  # Exit loop if the frame could not be read

    #               face = cropped_img(my_frame)
    #               if face is not None:
    #                   img_id += 1
    #                   face = cv2.resize(face, (450, 450))  # Resize only if face is detected
    #                   face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
    #                   file_name = f"data/user.{stu_id}.{img_id}.jpg"  # Use student ID in filename
    #                   cv2.imwrite(file_name, face)
                      
    #                   # Display the image ID on the window
    #                   cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (98, 233, 169), 2)
    #                   cv2.imshow("Cropped_face", face)

    #               if cv2.waitKey(1) == 13 or img_id == 100:  # Press Enter key to exit or after capturing 100 images
    #                   break

    #           cap.release()
    #           cv2.destroyAllWindows()
    #           messagebox.showinfo("Result", "Success")

    #       except Exception as e:
    #           messagebox.showerror("Error", str(e))


#  photo sample
    # def dataset(self):
    #   if self.var_stu_id.get() == "":
    #     messagebox.showerror("Error", "Select Class and Stream")
    #   else:
    #     try:
    #         connection = mysql.connector.connect(
    #             host="localhost", user="root", password="123456", port=3306, database="face_recognition"
    #         )
    #         my_cursor = connection.cursor()
    #         my_cursor.execute("SELECT * FROM student_data")
    #         my_result = my_cursor.fetchall()
    #         id = 0
    #         for i in my_result:
    #             id += 1
    #             my_cursor.execute(
    #                 "UPDATE student_data SET Class=%s, section=%s, stream=%s, optional=%s, stu_name=%s, session=%s, roll_no=%s, gender=%s, dob=%s, email=%s, contact=%s, address=%s, teacher=%s, photo=%s WHERE stu_id=%s",
    #                 (
    #                     self.var_class.get(),
    #                     self.var_section.get(),
    #                     self.var_stream.get(),
    #                     self.var_optional_sub.get(),
    #                     self.var_stu_name.get(),
    #                     self.var_session.get(),
    #                     self.var_roll_no.get(),
    #                     self.var_gender.get(),
    #                     self.var_dob.get(),
    #                     self.var_email.get(),
    #                     self.var_contact.get(),
    #                     self.var_address.get(),
    #                     self.var_teacher.get(),
    #                     self.var_radio1.get(),
    #                     id + 1,
    #                 ),
    #             )
    #         connection.commit()
    #         self.fetch_data()
    #         self.reset()
    #         connection.close()

    #         # ==============================================================
    #         face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    #         def cropped_img(img):
    #             gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #             faces = face_classifier.detectMultiScale(gray_img, 1.3, 5)
    #             for (x, y, w, h) in faces:
    #                 return img[y:y + h, x:x + w]  # Return the cropped face
    #             return None  # Return None if no face is detected

    #         cap = cv2.VideoCapture(0)
    #         img_id = 0
    #         while True:
    #             ret, my_frame = cap.read()
    #             if not ret:
    #                 break  # Exit loop if the frame could not be read

    #             face = cropped_img(my_frame)
    #             if face is not None:
    #                 img_id += 1
    #                 face = cv2.resize(face, (450, 450))  # Resize only if face is detected
    #                 face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
    #                 file_name = f"data/user.{id}.{img_id}.jpg"
    #                 cv2.imwrite(file_name, face)
                    
    #                 # Corrected cv2.putText() call
    #                 cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (98, 233, 169), 2)
    #                 cv2.imshow("Cropped_face", face)

    #             if cv2.waitKey(1) == 13 or img_id == 100:  # Press Enter key to exit or after capturing 100 images
    #                 break

    #         cap.release()
    #         cv2.destroyAllWindows()
    #         messagebox.showinfo("Result", "Success")

    #     except Exception as e:
    #         messagebox.showerror("Error", str(e))
        

   
