import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime

class Face_Recognizer(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.geometry("1920x1080")
        self.root.title("Face Detection")

        # BG IMG
        img = Image.open(r"C:\Users\aniru\OneDrive\Desktop\Face Recognition System\Images\face_detect.png")
        img = img.resize((1920, 1080), Image.ANTIALIAS)
        self.photoimg_train = ImageTk.PhotoImage(img)

        bg_img_detect = Label(self.root, image=self.photoimg_train)
        bg_img_detect.place(x=0, y=0, width=1920, height=1080)

        # BUTTON IMG AND BUTTON
        img2 = Image.open(r"C:\Users\aniru\OneDrive\Desktop\Face Recognition System\Images\face_icon_detect.png")
        img2 = img2.resize((300, 500), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b1 = Button(bg_img_detect, image=self.photoimg2, command=self.face_recognition, cursor="hand2")
        b1.place(x=1400, y=250, width=300, height=500)

        b1_txt = Button(bg_img_detect, text="Face Detection", command=self.face_recognition, cursor="hand2",
                        font=("Arial", 15, "bold"), bg="black", fg="light blue")
        b1_txt.place(x=1400, y=700, width=302, height=50)

    # --------------- Attendance ------------------------

    def mark_attendace(self,a,b,c,d):
        with open("attendance.csv","r+",newline="\n") as f:
            mydatalist=f.readlines()
            name_list=[]
            for line in mydatalist:
                entry=line.split((","))
                name_list.append(entry[0])
            if((a not in name_list) and (b not in name_list) and (c not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dstring=now.strftime("%I:%M:%S %p")
                f.writelines(f"\n{c},{a},{b},{d},{dstring},{d1},Present")


    # --------------- Face Recognition Function ------------------

    def face_recognition(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbours, color, text, clf):
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbours)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_img[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="Ani9203", database="face_recognition")
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT Student_Name FROM student WHERE Student_ID=" + str(id))
                a = my_cursor.fetchone()
                a = "+".join(a)
                
                my_cursor.execute("SELECT Roll_No FROM student WHERE Student_ID=" + str(id))
                b = my_cursor.fetchone()
                b = "+".join(b)

                my_cursor.execute("SELECT Student_ID FROM student WHERE Student_ID=" + str(id))
                c = my_cursor.fetchone()
                c = "+".join(c)

                my_cursor.execute("SELECT Department FROM student WHERE Student_ID=" + str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                if confidence > 79:
                    cv2.putText(img, f"Student ID: {c}", (x, y - 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255),2)
                    cv2.putText(img, f"Student Name: {a}", (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255),2)
                    cv2.putText(img, f"Roll No: {b}", (x, y - 55), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                    cv2.putText(img, f"Department: {d}", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                    self.mark_attendace(c,a,b,d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()

        # Load the trained classifier
        if os.path.isfile("classifier.xml"):
            clf.read("classifier.xml")
        else:
            messagebox.showerror("Error", "Trained classifier not found!")
            return

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()

            if not ret:
                messagebox.showerror("Error", "Failed to capture video!")
                break

            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)
            

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()


            




if __name__ == "__main__":
    root = tk.Tk()
    obj = Face_Recognizer(root)
    root.mainloop()