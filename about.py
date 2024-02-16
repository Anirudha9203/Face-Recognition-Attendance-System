import tkinter as ttk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import random




class About:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080")
        self.root.title("About")

    #Background Image

        img2 = Image.open(r"C:\Users\aniru\OneDrive\Desktop\Face Recognition System\Images\aboutbg.jpg")
        img2 = img2.resize((1920, 1080), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        bg_img = Label(self.root, image=self.photoimg2)
        bg_img.place(x=0, y=0, width=1920, height=1080)

        flabel=(Label(self.root,image=self.photoimg2))
        flabel.place(x=0,y=0,width=1920,height=1080)

        #Frame

        main_frame=Frame(flabel,bd=2,bg="#18191A")
        main_frame.place(x=700,y=340,width=500,height=370)

        # img3 = Image.open(r"C:\Users\aniru\OneDrive\Desktop\Face Recognition System\Images\aboutbg.jpg")
        # img3 = img3.resize((200, 200), Image.ANTIALIAS)
        # self.photoimg3 = ImageTk.PhotoImage(img3)

        # lbl=Label(main_frame,image=self.photoimg3)
        # lbl.place(x=700,y=150,width=500,height=600)

        name_lbl=Label(main_frame,text=" Name : Anirudha M. Chavan",font=("Arial",15,"bold"),bg="#18191A",fg="white")
        name_lbl.place(x=0,y=5)

        dep_lbl=Label(main_frame,text=" TY BSc Data Science",font=("Arial",15,"bold"),bg="#18191A",fg="white")
        dep_lbl.place(x=0,y=40)

        clg_lbl=Label(main_frame,text=" Pillai College of Arts,Science and Commerce,",font=("Arial",15,"bold"),bg="#18191A",fg="white")
        clg_lbl.place(x=0,y=75)

        add_lbl=Label(main_frame,text=" Rasayani, Navi Mumbai.",font=("Arial",15,"bold"),bg="#18191A",fg="white")
        add_lbl.place(x=0,y=110)

        prj_lbl=Label(main_frame,text=" Project: Face Attendance Recognition System",font=("Arial",15,"bold"),bg="#18191A",fg="#63C5DA")
        prj_lbl.place(x=0,y=145)

        des1_lbl=Label(main_frame,text=" A face recognition system is a technology that identifies and",font=("Arial",13,"bold"),bg="#18191A",fg="white")
        des1_lbl.place(x=0,y=180)

        des2_lbl=Label(main_frame,text=" verifies individuals based on their unique facial features.",font=("Arial",13,"bold"),bg="#18191A",fg="white")
        des2_lbl.place(x=0,y=200)

        des3_lbl=Label(main_frame,text=" It extracts facial data, creates a digital template and matches",font=("Arial",13,"bold"),bg="#18191A",fg="white")
        des3_lbl.place(x=0,y=220)

        des4_lbl=Label(main_frame,text=" it with stored templates for identification. It finds applications",font=("Arial",13,"bold"),bg="#18191A",fg="white")
        des4_lbl.place(x=0,y=240)

        des5_lbl=Label(main_frame,text=" in security, access control, and authentication but raises",font=("Arial",13,"bold"),bg="#18191A",fg="white")
        des5_lbl.place(x=0,y=260)

        des6_lbl=Label(main_frame,text=" about privacy and ethics. Advances in AI improve accuracy",font=("Arial",13,"bold"),bg="#18191A",fg="white")
        des6_lbl.place(x=0,y=280)

        des7_lbl=Label(main_frame,text=" and performance.",font=("Arial",13,"bold"),bg="#18191A",fg="white")
        des7_lbl.place(x=0,y=300)

        email_lbl=Label(main_frame,text=" Email : chavananiman21hds@student.mes.ac.in",font=("Arial",15,"bold"),bg="#18191A",fg="white")
        email_lbl.place(x=0,y=330)


if __name__ == "__main__":
    root = Tk()
    obj = About(root)
    root.mainloop()