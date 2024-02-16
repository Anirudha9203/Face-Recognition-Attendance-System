import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import random
import os
import csv
from tkinter import filedialog


mydata=[]

class Attendace:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080")
        self.root.title("Attendance")

        #------------------ VARIABLES ----------------
        self.var_attend_id=StringVar()
        self.var_attend_name=StringVar()
        self.var_attend_dept=StringVar()
        self.var_attend_roll_no=StringVar()
        self.var_attend_date=StringVar()
        self.var_attend_time=StringVar()
        self.var_attend_attendance=StringVar()

        #Banner 1

        img = Image.open(r"C:\Users\aniru\OneDrive\Desktop\Face Recognition System\Images\5.png")
        img = img.resize((960, 200), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_bnr = Label(self.root, image=self.photoimg)
        f_bnr.place(x=0, y=0, width=960, height=200)

        #Banner 2

        img1 = Image.open(r"C:\Users\aniru\OneDrive\Desktop\Face Recognition System\Images\6.png")
        img1 = img1.resize((960, 200), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_bnr = Label(self.root, image=self.photoimg1)
        f_bnr.place(x=960, y=0, width=960, height=200)

        #Background Image

        img2 = Image.open(r"C:\Users\aniru\OneDrive\Desktop\Face Recognition System\Images\atdbnr.jpg")
        img2 = img2.resize((1920, 1080), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        bg_img = Label(self.root, image=self.photoimg2)
        bg_img.place(x=0, y=200, width=1920, height=960)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=3,y=68,width=1900,height=1000)

        #Left label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE)
        Left_frame.place(x=10,y=15,width=960,height=700)

        img_lft = Image.open(r"C:\Users\aniru\OneDrive\Desktop\Face Recognition System\Images\atd2.png")
        img_lft = img_lft.resize((900, 135), Image.ANTIALIAS)
        self.photoimg_lft = ImageTk.PhotoImage(img_lft)

        f_bnr = Label(Left_frame, image=self.photoimg_lft)
        f_bnr.place(x=10, y=0, width=900, height=140)

        img_lft2 = Image.open(r"C:\Users\aniru\OneDrive\Desktop\Face Recognition System\Images\btn_mock.png")
        img_lft2 = img_lft2.resize((900, 45), Image.ANTIALIAS)
        self.photoimg_lft2 = ImageTk.PhotoImage(img_lft2)

        f_bnr2 = Label(Left_frame, image=self.photoimg_lft2)
        f_bnr2.place(x=10, y=640, width=900, height=50)

        lft_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="#18191A")
        lft_inside_frame.place(x=10,y=130,width=935,height=500)


        #Label & entry

        # Attendance ID
        attendanceID_label = Label(lft_inside_frame, text="  Attendance ID:", bg="#18191A", fg="white", font=("Arial", 14, "bold"))
        attendanceID_label.grid(row=0, column=0, padx=5, pady=15, sticky=W)

        attendanceID_entry = ttk.Entry(lft_inside_frame,textvariable=self.var_attend_id, width=20, font=("Arial", 14, "bold"))
        attendanceID_entry.grid(row=0, column=1, padx=20, pady=15, sticky=W)

        # Name
        name_label = Label(lft_inside_frame, text="  Name:", bg="#18191A", fg="white", font=("Arial", 14, "bold"))
        name_label.grid(row=0, column=2, padx=5, pady=15, sticky=W)

        name_entry = ttk.Entry(lft_inside_frame,textvariable=self.var_attend_name, width=20, font=("Arial", 14, "bold"))
        name_entry.grid(row=0, column=3, padx=20, pady=15, sticky=W)


        #Department

        dept_label = Label(lft_inside_frame, text="  Department:",bg="#18191A",fg="white", font=("Arial", 14, "bold"))
        dept_label.grid(row=1, column=0,padx=5,pady=15,sticky=W)

        dept_entry=ttk.Entry(lft_inside_frame,textvariable=self.var_attend_dept, width=20,font=("Arial", 14, "bold"))
        dept_entry.grid(row=1,column=1,padx=20, pady=15, sticky=W)
        
        #Roll No

        rollno_label = Label(lft_inside_frame, text="  Roll No:",bg="#18191A",fg="white", font=("Arial", 14, "bold"))
        rollno_label.grid(row=1, column=2,padx=5,pady=15,sticky=W)

        rollno_entry=ttk.Entry(lft_inside_frame,textvariable=self.var_attend_roll_no, width=20,font=("Arial", 14, "bold"))
        rollno_entry.grid(row=1,column=3,padx=20, pady=15, sticky=W)

        #Date

        date_label = Label(lft_inside_frame, text="  Date:",bg="#18191A",fg="white", font=("Arial", 14, "bold"))
        date_label.grid(row=2, column=0,padx=5,pady=15,sticky=W)

        date_entry=ttk.Entry(lft_inside_frame,textvariable=self.var_attend_date, width=20,font=("Arial", 14, "bold"))
        date_entry.grid(row=2,column=1,padx=20, pady=15, sticky=W)

        #Time

        time_label = Label(lft_inside_frame, text="  Time:",bg="#18191A",fg="white", font=("Arial", 14, "bold"))
        time_label.grid(row=2, column=2,padx=5,pady=15,sticky=W)

        time_entry=ttk.Entry(lft_inside_frame,textvariable=self.var_attend_time, width=20,font=("Arial", 14, "bold"))
        time_entry.grid(row=2,column=3,padx=20, pady=15, sticky=W)

        #Attendance Status
        attendance_sts_label = Label(lft_inside_frame, text="  Attendance Status:",bg="#18191A",fg="white", font=("Arial", 14, "bold"))
        attendance_sts_label.grid(row=3, column=0, padx=5, pady=15, sticky=tk.W)

        self.atten_status = ttk.Combobox(lft_inside_frame,textvariable=self.var_attend_attendance, width=20, font=("Arial", 14), state="readonly")
        self.atten_status["values"] = ("None", "Present", "Absent")
        self.atten_status.grid(row=3, column=1, padx=20, pady=15, sticky=tk.W)
        self.atten_status.current(0)

        #button frames

        Button_frame=Frame(lft_inside_frame,bd=2,relief=RIDGE,bg="#18191A")
        Button_frame.place(x=0, y=460, width=932, height=40)

        import_btn=Button(Button_frame,text="Import csv",command=self.importCSV, width=19,font=("Arial", 14, "bold"),bg="#18191A",fg="#00FFFF")
        import_btn.grid(row=0,column=0)

        export_btn=Button(Button_frame,text="Export csv",command=self.exportCSV,width=19,font=("Arial", 14, "bold"),bg="#18191A",fg="#00FFFF")
        export_btn.grid(row=0,column=1)

        update_btn = Button(Button_frame,text="Update",command=self.update_data,bg="#18191A",fg="#00FFFF",width=17,font=("Arial",14,"bold"))
        update_btn.grid(row=0,column=2)

        reset_btn=Button(Button_frame,text="Reset",command=self.reset_data,width=20,font=("Arial", 14, "bold"),bg="#18191A",fg="#00FFFF")
        reset_btn.grid(row=0,column=3)


        #Right label frame

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Information",font=("Arial",15,"bold"))
        Right_frame.place(x=980,y=5,width=920,height=710)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5, y=5, width=910, height=670)

        #======= Scroll bar & table ===========

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("ID","Roll No","Name","Department","Time","Date","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        #Adding header columns
        self.AttendanceReportTable.heading("ID",text="Attendance ID")
        self.AttendanceReportTable.heading("Roll No",text="Roll No")
        self.AttendanceReportTable.heading("Name",text="Name")
        self.AttendanceReportTable.heading("Department",text="Department")
        self.AttendanceReportTable.heading("Time",text="Time")
        self.AttendanceReportTable.heading("Date",text="Date")
        self.AttendanceReportTable.heading("Attendance",text="Attendance")

        #Setting width
        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("ID",width=100)
        self.AttendanceReportTable.column("Roll No",width=100)
        self.AttendanceReportTable.column("Name",width=100)
        self.AttendanceReportTable.column("Department",width=100)
        self.AttendanceReportTable.column("Time",width=100)
        self.AttendanceReportTable.column("Date",width=100)
        self.AttendanceReportTable.column("Attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

        #------------------ FETCH DATA --------------------

    def fetchdata(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)


    #Import data 

    def importCSV(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)

    #Export Data
    def exportCSV(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","There's no data to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Export data","The data "+os.path.basename(fln)+" has been exported successfully")
        except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    #Get Cursor

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_attend_id.set(rows[0])
        self.var_attend_roll_no.set(rows[1])
        self.var_attend_name.set(rows[2])
        self.var_attend_dept.set(rows[3])
        self.var_attend_time.set(rows[4])
        self.var_attend_date.set(rows[5])
        self.var_attend_attendance.set(rows[6])

    #Update Data
    def update_data(self):
        try:
            selected_id = self.var_attend_id.get()

            if selected_id == "":
                messagebox.showerror("Error", "Please select a record to update", parent=self.root)
                return

            for index, row in enumerate(mydata):
                if row[0] == selected_id:
                    mydata[index] = [
                        self.var_attend_id.get(),
                        self.var_attend_roll_no.get(),
                        self.var_attend_name.get(),
                        self.var_attend_dept.get(),
                        self.var_attend_time.get(),
                        self.var_attend_date.get(),
                        self.var_attend_attendance.get(),
                ]
                found = True
                break
            
            if not found:
                messagebox.showerror("Error", "Selected ID not found in the data", parent=self.root)
                return

            with open('attendance.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(mydata)

            self.fetchdata(mydata)
            messagebox.showinfo("Success", "Data updated successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Error updating data: {str(e)}", parent=self.root)

    #Reset Data

    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_roll_no.set("")
        self.var_attend_name.set("")
        self.var_attend_dept.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_attendance.set("")
    






if __name__ == "__main__":
    root = Tk()
    obj = Attendace(root)
    root.mainloop()