import os
import cv2
if os.path.exists("classifier.xml"):
    clf = cv2.face.LBPHFaceRecognizer_create()
        
    clf.read("classifier.xml")
else:
    print("Error: classifier.xml not found.")