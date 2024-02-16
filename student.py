import tkinter as ttk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import random




class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080")
        self.root.title("Student Portal")

        #-------------- VARIABLES -------------
        self.var_Department=StringVar()
        self.var_Course=StringVar()
        self.var_Year=StringVar()
        self.var_Semester=StringVar()
        self.var_ID=StringVar()
        self.var_Name=StringVar()
        self.var_Div=StringVar()
        self.var_DOB=StringVar()
        self.var_RollNo=StringVar()
        self.var_Contact_No=StringVar()
        self.var_Email_ID=StringVar()
        self.var_Faculty_name=StringVar()


        #Banner 1

        img = Image.open(r"C:\Users\aniru\OneDrive\Desktop\Face Recognition System\Images\3.png")
        img = img.resize((960, 200), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_bnr = Label(self.root, image=self.photoimg)
        f_bnr.place(x=0, y=0, width=960, height=200)

        #Banner 2

        img1 = Image.open(r"C:\Users\aniru\OneDrive\Desktop\Face Recognition System\Images\4.png")
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

        title_lbl=Label(bg_img,text="Student Management System",font=("Arial",35,"bold"),bg="light blue",fg="black")
        title_lbl.place(x=0,y=0,width=1920,height=65)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=3,y=68,width=1900,height=1000)

        #Left label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE)
        Left_frame.place(x=10,y=15,width=960,height=700)

        img_lft = Image.open(r"C:\Users\aniru\OneDrive\Desktop\Face Recognition System\Images\PHCASC-Header.png")
        img_lft = img_lft.resize((750, 100), Image.ANTIALIAS)
        self.photoimg_lft = ImageTk.PhotoImage(img_lft)

        f_bnr = Label(Left_frame, image=self.photoimg_lft)
        f_bnr.place(x=10, y=0, width=900, height=140)

        #Current Course
        from tkinter import ttk

        Course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Course Information", font=("Arial", 15, "bold"))
        Course_frame.place(x=10, y=135, width=920, height=160)

        # Department
        department_label = Label(Course_frame, text="Department", font=("Arial", 14, "bold"))
        department_label.grid(row=0, column=0,padx=5,pady=15,sticky=W)

        department_combo = ttk.Combobox(Course_frame, textvariable=self.var_Department, font=("Arial", 14), state="readonly")
        department_combo['values'] = ("Select Department", "Arts", "Science", "Commerce", "Others")
        department_combo.grid(row=0, column=1, padx=20, pady=10, sticky=W)
        department_combo.current(0)

        #Courses
        course_label = Label(Course_frame, text="Course", font=("Arial", 14, "bold"))
        course_label.grid(row=0, column=2,padx=5,pady=15,sticky=W)

        course_combo = ttk.Combobox(Course_frame,textvariable=self.var_Course, font=("Arial", 14), state="readonly")
        course_combo['values'] = ("Select Course", "BSc Chem","BSc Phy","BA", "BAF", "BCom","BSc","BSc Computer Science","Bsc IT","Bsc Data Science")
        course_combo.grid(row=0, column=3, padx=20, pady=20,sticky=W)
        course_combo.current(0)

        # Year
        year_label = Label(Course_frame, text="Year", font=("Arial", 14, "bold"))
        year_label.grid(row=1, column=0,padx=5,pady=15,sticky=W)

        year_combo = ttk.Combobox(Course_frame,textvariable=self.var_Year, font=("Arial", 14), state="readonly")
        year_combo['values'] = ("Select Year", "FY", "SY", "TY")
        year_combo.grid(row=1, column=1, padx=20, pady=15, sticky=W)
        year_combo.current(0)

        # Semester
        sem_label = Label(Course_frame, text="Semester", font=("Arial", 14, "bold"))
        sem_label.grid(row=1, column=2,padx=5,pady=15,sticky=W)

        sem_combo = ttk.Combobox(Course_frame,textvariable=self.var_Semester, font=("Arial", 14), state="readonly")
        sem_combo['values'] = ("Select Semester", "Sem 1", "Sem 2", "Sem 3", "Sem 4", "Sem 5", "Sem 6")
        sem_combo.grid(row=1, column=3, padx=20, pady=0, sticky=W)
        sem_combo.current(0)

        #Student Information
        student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Student Information", font=("Arial", 15, "bold"))
        student_frame.place(x=10, y=300, width=920, height=360)

        #Student ID
        studentID_label = Label(student_frame, text="  Student ID:", font=("Arial", 14, "bold"))
        studentID_label.grid(row=0, column=0,padx=5,pady=15,sticky=W)

        studentID_entry=ttk.Entry(student_frame,textvariable=self.var_ID, width=20,font=("Arial", 14, "bold"))
        studentID_entry.grid(row=0,column=1,padx=20, pady=15, sticky=W)

        #Student Name
        studentName_label = Label(student_frame, text=" Student Name:", font=("Arial", 14, "bold"))
        studentName_label.grid(row=0, column=2,padx=5,pady=15,sticky=W)

        studentName_entry=ttk.Entry(student_frame,textvariable=self.var_Name, width=20,font=("Arial", 14, "bold"))
        studentName_entry.grid(row=0,column=3,padx=20, pady=15, sticky=W)

        #Class division
        class_div__label = Label(student_frame, text="  Class/Division:", font=("Arial", 14, "bold"))
        class_div__label.grid(row=1, column=0,padx=5,pady=15,sticky=W)

        class_div_combo = ttk.Combobox(student_frame,textvariable=self.var_Div, font=("Arial", 14), state="readonly",width=18)
        class_div_combo['values'] = ("None", "A", "B", "C", "D", "E")
        class_div_combo.grid(row=1, column=1, padx=20, pady=0, sticky=W)
        class_div_combo.current(0)

        #DOB
        DOB__label = Label(student_frame, text="  DOB:", font=("Arial", 14, "bold"))
        DOB__label.grid(row=1, column=2,padx=5,pady=15,sticky=W)

        DOB_entry=ttk.Entry(student_frame,textvariable=self.var_DOB, width=20,font=("Arial", 14, "bold"))
        DOB_entry.grid(row=1,column=3,padx=20, pady=15, sticky=W)

        #Roll no
        Roll_no_label = Label(student_frame, text="  Roll No:", font=("Arial", 14, "bold"))
        Roll_no_label.grid(row=2, column=0,padx=5,pady=15,sticky=W)

        Roll_no_entry=ttk.Entry(student_frame,textvariable=self.var_RollNo, width=20,font=("Arial", 14, "bold"))
        Roll_no_entry.grid(row=2,column=1,padx=20, pady=15, sticky=W)

        #Email ID
        Email_ID_label = Label(student_frame, text="  Email ID:", font=("Arial", 14, "bold"))
        Email_ID_label.grid(row=2, column=2,padx=5,pady=15,sticky=W)

        Email_ID_entry=ttk.Entry(student_frame,textvariable=self.var_Email_ID,width=20,font=("Arial", 14, "bold"))
        Email_ID_entry.grid(row=2,column=3,padx=20, pady=15, sticky=W)

        #Contact_No
        Contact_No_label = Label(student_frame, text="  Contact No:", font=("Arial", 14, "bold"))
        Contact_No_label.grid(row=3, column=0,padx=5,pady=15,sticky=W)

        Contact_No_entry=ttk.Entry(student_frame,textvariable=self.var_Contact_No, width=20,font=("Arial", 14, "bold"))
        Contact_No_entry.grid(row=3,column=1,padx=20, pady=15, sticky=W)

        #Faculty_Name
        Faculty_Name_label = Label(student_frame, text="  Faculty Name:", font=("Arial", 14, "bold"))
        Faculty_Name_label.grid(row=3, column=2,padx=5,pady=15,sticky=W)

        Faculty_Name_entry=ttk.Entry(student_frame,textvariable=self.var_Faculty_name, width=20,font=("Arial", 14, "bold"))
        Faculty_Name_entry.grid(row=3,column=3,padx=20, pady=15, sticky=W)

        #Radio buttons
        self.var_radio1 = StringVar()
        Radiobutton1 = ttk.Radiobutton(student_frame, variable=self.var_radio1, text="Take a picture", value="Yes")
        Radiobutton1.grid(row=4, column=0, padx=0, pady=0)

        Radiobutton2 = ttk.Radiobutton(student_frame, variable=self.var_radio1, text="No picture", value="No")
        Radiobutton2.grid(row=4, column=1, padx=0, pady=0)

        #button frames

        Button_frame=Frame(student_frame,bd=2,relief=RIDGE,bg="white")
        Button_frame.place(x=0, y=260, width=920, height=40)

        save_btn=Button(Button_frame,text="Save",command=self.add_data, width=19,font=("Arial", 14, "bold"),bg="light blue",fg="black")
        save_btn.grid(row=0,column=0)

        delete_btn=Button(Button_frame,text="Delete",command=self.delete_data,width=19,font=("Arial", 14, "bold"),bg="red",fg="white")
        delete_btn.grid(row=0,column=1)

        update_btn = Button(Button_frame,text="Update",bg="light blue",fg="black",width=17,command=self.update_data,font=("Arial",14,"bold"))
        update_btn.grid(row=0,column=2)

        reset_btn=Button(Button_frame,text="Reset",command=self.reset_data,width=19,font=("Arial", 14, "bold"),bg="red",fg="white")
        reset_btn.grid(row=0,column=3)

        #Photo frame

        photo_frame=Frame(student_frame,bd=2,relief=RIDGE,bg="white")
        photo_frame.place(x=0, y=300, width=920, height=60)

        take_pic_btn=Button(photo_frame,command=self.generate_dataset,text="Take Sample Photo",width=38,font=("Arial", 14, "bold"),bg="black",fg="white")
        take_pic_btn.grid(row=0,column=0)

        update_pic_btn=Button(photo_frame,text="Update Sample Photo",width=38,font=("Arial", 14, "bold"),bg="black",fg="white")
        update_pic_btn.grid(row=0,column=1)

        
        # -------------------------Right label frame---------------------------

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,font=("Arial",15,"bold"))
        Right_frame.place(x=980,y=15,width=920,height=700)

        img_rgt = Image.open(r"C:\Users\aniru\OneDrive\Desktop\Face Recognition System\Images\clg.jpg")
        img_rgt = img_rgt.resize((960, 200), Image.ANTIALIAS)
        self.photoimg_rgt = ImageTk.PhotoImage(img_rgt)

        f_bnr = Label(Right_frame, image=self.photoimg_rgt)
        f_bnr.place(x=0, y=0, width=920, height=150)

        #=================Search system=====================
        search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("Arial", 15, "bold"))
        search_frame.place(x=5, y=150, width=913, height=90)

        Search_label = Label(search_frame, text="  Search By:  ", font=("Arial", 14, "bold"),bg="black",fg="white")
        Search_label.grid(row=0, column=0,padx=15,pady=10)

        self.var_combo_search=StringVar()

        search_combo = ttk.Combobox(search_frame,textvariable=self.var_combo_search, font=("Arial", 14), state="readonly",width=15)
        search_combo['values'] = ("Select Semester", "Roll_No", "Phone_No", "Student_Name")
        search_combo.grid(row=0, column=1, padx=5, pady=10, sticky=W)
        search_combo.current(0)

        self.var_search=StringVar()

        search_entry=ttk.Entry(search_frame,textvariable=self.var_search, width=14,font=("Arial", 14, "bold"))
        search_entry.grid(row=0,column=2,padx=20, pady=15, sticky=W)

        search_btn=Button(search_frame,command=self.search_data,text="Search",width=14, font=("Arial", 13, "bold"),bg="light blue",fg="black")
        search_btn.grid(row=0,column=3,padx=5, pady=10)

        ShowAll_btn=Button(search_frame,command=self.fetch_data,text="Show All",width=14,font=("Arial", 13, "bold"),bg="red",fg="white")
        ShowAll_btn.grid(row=0,column=4,padx=5, pady=10)

        #===============Table Frame===============
        table_frame=Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=250, width=913, height=450)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("Department","Course","Year","Semester","ID","Name","Div","DOB","RollNo","Contact_No","Email_ID","Faculty_name","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("ID",text="StudentID")
        self.student_table.heading("Name",text="StudentName")
        self.student_table.heading("Div",text="Division")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("RollNo",text="RollNo")
        self.student_table.heading("Contact_No",text="ContactNo")
        self.student_table.heading("Email_ID",text="Email_ID")
        self.student_table.heading("Faculty_name",text="Faculty_name")
        self.student_table.heading("Photo",text="PhotoSample")
        self.student_table["show"]="headings"

        self.student_table.column("Department",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Semester",width=100)
        self.student_table.column("ID",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Div",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("RollNo",width=100)
        self.student_table.column("Contact_No",width=100)
        self.student_table.column("Email_ID",width=100)
        self.student_table.column("Faculty_name",width=100)
        self.student_table.column("Photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #===========Function Declaration==================

    def add_data(self):
        if self.var_Department.get()=="Select Department" or self.var_Name.get()=="" or self.var_ID.get()=="":
            messagebox.showerror("Error","Kindly fill all require fields",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Ani9203",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.var_Department.get(),
                                                                                                        self.var_Course.get(),
                                                                                                        self.var_Year.get(),
                                                                                                        self.var_Semester.get(),
                                                                                                        self.var_ID.get(),
                                                                                                        self.var_Name.get(),
                                                                                                        self.var_Div.get(),
                                                                                                        self.var_DOB.get(),
                                                                                                        self.var_RollNo.get(),
                                                                                                        self.var_Contact_No.get(),
                                                                                                        self.var_Email_ID.get(),
                                                                                                        self.var_Faculty_name.get(),
                                                                                                        self.var_radio1.get()
                                        
                                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    #================Fetch Database==================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Ani9203",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
            conn.close()



    #----------------------Get Cursor---------------------
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_Department.set(data[0]),
        self.var_Course.set(data[1]),
        self.var_Semester.set(data[2]),
        self.var_Year.set(data[3]),
        self.var_ID.set(data[4]),
        self.var_Name.set(data[5]),
        self.var_Div.set(data[6]),  
        self.var_DOB.set(data[7]),
        self.var_RollNo.set(data[8]),
        self.var_Contact_No.set(data[9]),
        self.var_Email_ID.set(data[10]),
        self.var_Faculty_name.set(data[11]),  
        self.var_radio1.set(data[12])
        


    # Update Function
    def update_data(self):
        if self.var_Department.get() == "Select Department" or self.var_Name.get() == "" or self.var_ID.get() == "":
            messagebox.showerror("Error", "Kindly fill all required fields", parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update", "Do you want to update the new information", parent=self.root)
                if Update>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Ani9203", database="face_recognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute("Update student set Department=%s, Course=%s, Year=%s, Semester=%s, Student_Name=%s, Division=%s, DOB=%s, Roll_No=%s, Contact_No=%s, Email_ID=%s, Faculty_Name=%s, Photo_Sample=%s where Student_ID=%s", (
                                                                                                                                                                                                                                                self.var_Department.get(),
                                                                                                                                                                                                                                                self.var_Course.get(),
                                                                                                                                                                                                                                                self.var_Year.get(),
                                                                                                                                                                                                                                                self.var_Semester.get(),
                                                                                                                                                                                                                                                self.var_Name.get(),
                                                                                                                                                                                                                                                self.var_Div.get(),
                                                                                                                                                                                                                                                self.var_DOB.get(),
                                                                                                                                                                                                                                                self.var_RollNo.get(),
                                                                                                                                                                                                                                                self.var_Contact_No.get(),
                                                                                                                                                                                                                                                self.var_Email_ID.get(),
                                                                                                                                                                                                                                                self.var_Faculty_name.get(),
                                                                                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                                                                                self.var_ID.get()
                                                                                                                                                                                                                                                ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "The information has been successfully updated", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)


    #Delete Function
    
    def delete_data(self):
        if self.var_ID.get()=="":
            messagebox.showerror("Error","Student ID must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete information","Do you want to delete this student details",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Ani9203", database="face_recognition")
                    my_cursor = conn.cursor()
                    sql="Delete from student where Student_ID=%s"
                    val=(self.var_ID.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","The details have been deleted successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    #Reset function

    def reset_data(self):
        self.var_Department.set("Select Department")
        self.var_Course.set("Select Course")
        self.var_Semester.set("Select Semester")
        self.var_Year.set("Select Year")
        self.var_ID.set("")
        self.var_Name.set("")
        self.var_Div.set("None")
        self.var_DOB.set("")
        self.var_RollNo.set("")
        self.var_Contact_No.set("")
        self.var_Email_ID.set("")
        self.var_Faculty_name.set("") 
        self.var_radio1.set("")

    #Search Function
    def search_data(self):
        if self.var_combo_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please select an option")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Ani9203", database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("Select * from Student where "+str(self.var_combo_search.get()+" LIKE  '%"+str(self.var_search.get()))+"%'")
                data=my_cursor.fetchall()
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)






    #------------------------- TAKE PHOTO SAMPLE ------------------------------
    
    def generate_dataset(self):
        if self.var_Department.get() == "Select Department" or self.var_Name.get() == "" or self.var_ID.get() == "":
            messagebox.showerror("Error", "Kindly fill all required fields", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Ani9203", database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("Update student set Department=%s, Course=%s, Year=%s, Semester=%s, Student_Name=%s, Division=%s, DOB=%s, Roll_No=%s, Contact_No=%s, Email_ID=%s, Faculty_Name=%s, Photo_Sample=%s where Student_ID=%s",(
                                                                                                                                                                                                                                            self.var_Department.get(),
                                                                                                                                                                                                                                            self.var_Course.get(),
                                                                                                                                                                                                                                            self.var_Year.get(),
                                                                                                                                                                                                                                            self.var_Semester.get(),
                                                                                                                                                                                                                                            self.var_Name.get(),
                                                                                                                                                                                                                                            self.var_Div.get(),
                                                                                                                                                                                                                                            self.var_DOB.get(),
                                                                                                                                                                                                                                            self.var_RollNo.get(),
                                                                                                                                                                                                                                            self.var_Contact_No.get(),
                                                                                                                                                                                                                                            self.var_Email_ID.get(),
                                                                                                                                                                                                                                            self.var_Faculty_name.get(),
                                                                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                                                                            self.var_ID.get()==id+1
                                                                                                                                                                                                                                            ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # LOAD OPENCV FILE

                face_classify = cv2.CascadeClassifier("C:\\Users\\aniru\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")

                def face_crop(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classify.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum neighbour =5

                    for (x, y, w, h) in faces:
                        face_crop = img[y:y + h, x:x + w]
                        return face_crop

                    
                cap=cv2.VideoCapture(0)
                img_id=0
                ran = random.randint(0, 22) * random.randint(0, 100)
                while True:
                    ret,my_frame=cap.read()
                    if face_crop(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_crop(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path = "img_data/student." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Capture Images",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Images captured successfully",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)





        
        

        













if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()