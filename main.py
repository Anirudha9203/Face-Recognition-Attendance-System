import tkinter as tk
import tkinter.messagebox
from tkinter import *
from PIL import Image, ImageTk
import os
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from face_recognizer import Face_Recognizer
from attendance import Attendace
from about import About



class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080")
        self.root.title("Face Recognition System")

        #Banner 1

        img = Image.open(r"C:\Users\aniru\OneDrive\Desktop\Face Recognition System\Images\1.png")
        img = img.resize((960, 200), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_bnr = Label(self.root, image=self.photoimg)
        f_bnr.place(x=0, y=0, width=960, height=200)

        #Banner 2

        img1 = Image.open(r"C:\Users\aniru\OneDrive\Desktop\Face Recognition System\Images\2.png")
        img1 = img1.resize((960, 200), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_bnr = Label(self.root, image=self.photoimg1)
        f_bnr.place(x=960, y=0, width=960, height=200)

        #Background Image

        img2 = Image.open(r"C:\Users\aniru\OneDrive\Desktop\Face Recognition System\Images\newbg.jpg")
        img2 = img2.resize((1920, 1080), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        bg_img = Label(self.root, image=self.photoimg2)
        bg_img.place(x=0, y=200, width=1920, height=960)

        title_lbl=Label(bg_img,text="Face Recognition Attendance System",font=("Arial",35,"bold"),bg="black",fg="light blue")
        title_lbl.place(x=0,y=0,width=1920,height=55)
        
        #Time

        def time():
            string=strftime("%I:%M %p")
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl = Label(title_lbl,font=("Arial",15,"bold"),bg="black",fg="light blue")
        lbl.place(x=1800,y=0,width=120,height=55)
        time()

        #Student details button

        img3 = Image.open(r"C:\Users\aniru\OneDrive\Desktop\Face Recognition System\Images\stdportal.jpg")
        img3 = img3.resize((180, 180), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b1 = Button(bg_img, image=self.photoimg3, command=self.student_details,cursor="hand2")
        b1.place(x=200, y=150, width=180, height=180)

        b1_txt = Button(bg_img, text="Student Portal", command=self.student_details, cursor="hand2", font=("Arial", 15, "bold"), bg="white", fg="black")
        b1_txt.place(x=200, y=300, width=181, height=50)

        #Face Detection button

        img4 = Image.open(r"C:\Users\aniru\OneDrive\Desktop\Face Recognition System\Images\fc2.jpg")
        img4 = img4.resize((180, 180), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b2=Button(bg_img,image=self.photoimg4,command=self.face_detection,cursor="hand2")
        b2.place(x=500,y=150,width=180,height=180)

        b2_txt=Button(bg_img,text="Face Detection",command=self.face_detection,cursor="hand2",font=("Arial",15,"bold"),bg="white",fg="black")
        b2_txt.place(x=500,y=300,width=181,height=50)

        #Attendance button

        img5 = Image.open(r"C:\Users\aniru\OneDrive\Desktop\Face Recognition System\Images\attenance.jpg")
        img5 = img5.resize((180, 180), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b3=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.attendance)
        b3.place(x=800,y=150,width=180,height=180)

        b3_txt=Button(bg_img,text="Attendance System",cursor="hand2",command=self.attendance,font=("Arial",12,"bold"),bg="white",fg="black")
        b3_txt.place(x=800,y=300,width=181,height=50)

        #Training button

        img6 = Image.open(r"C:\Users\aniru\OneDrive\Desktop\Face Recognition System\Images\training.jpg")
        img6 = img6.resize((180, 250), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b4=Button(bg_img,image=self.photoimg6,command=self.train_data,cursor="hand2")
        b4.place(x=1100,y=150,width=180,height=180)

        b4_txt=Button(bg_img,text="Training Data",command=self.train_data,cursor="hand2",font=("Arial",15,"bold"),bg="white",fg="black")
        b4_txt.place(x=1100,y=300,width=181,height=50)

        # Image button
        img7 = Image.open(r"C:\Users\aniru\OneDrive\Desktop\Face Recognition System\Images\img_1.jpg")
        img7 = img7.resize((180, 180), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b5 = Button(bg_img, image=self.photoimg7,command=self.open_img, cursor="hand2")
        b5.place(x=1400, y=150, width=180, height=180)

        b5_txt = Button(bg_img, text="Images Data",command=self.open_img, cursor="hand2", font=("Arial", 15, "bold"), bg="white", fg="black")
        b5_txt.place(x=1400, y=300, width=181, height=50)


        # About button
        img8 = Image.open(r"C:\Users\aniru\OneDrive\Desktop\Face Recognition System\Images\about.jpg")
        img8 = img8.resize((180, 180), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b6 = Button(bg_img, image=self.photoimg8,command=self.about, cursor="hand2")
        b6.place(x=650, y=450, width=180, height=180)

        b6_txt = Button(bg_img, text="About",command=self.about, cursor="hand2", font=("Arial", 15, "bold"), bg="white", fg="black")
        b6_txt.place(x=650, y=600, width=181, height=50)


        # Exit button
        img9 = Image.open(r"C:\Users\aniru\OneDrive\Desktop\Face Recognition System\Images\exit_1.jpg")
        img9 = img9.resize((180, 180), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b7 = Button(bg_img, image=self.photoimg9, cursor="hand2",command=self.iExit)
        b7.place(x=950, y=450, width=180, height=180)

        b7_txt = Button(bg_img, text="Exit", cursor="hand2",command=self.iExit, font=("Arial", 15, "bold"), bg="white", fg="black")
        b7_txt.place(x=950, y=600, width=181, height=50)

    #Function for Images
    def open_img(self):
        os.startfile("img_data")

    #Exit button

    def iExit(self):
        self.iExitExit = tkinter.messagebox.askyesno("Face Recognition", "Are you sure you want to exit",parent=self.root)
        if self.iExitExit:
            self.root.destroy()
        else:
            return



        #===================Function Buttons=====================

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_detection(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognizer(self.new_window)

    def attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendace(self.new_window)

    def about(self):
        self.new_window=Toplevel(self.root)
        self.app=About(self.new_window)






if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()

    
