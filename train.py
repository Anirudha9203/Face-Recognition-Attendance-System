import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np




class Train(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.geometry("1920x1080")
        self.root.title("Training Data")
        #BG IMG
        img = Image.open(r"C:\Users\aniru\OneDrive\Desktop\Face Recognition System\Images\train_bg.jpg")
        img = img.resize((1920, 1080), Image.ANTIALIAS)
        self.photoimg_train = ImageTk.PhotoImage(img)

        bg_img_train = Label(self.root, image=self.photoimg_train)
        bg_img_train.place(x=0, y=0, width=1920, height=1080)

        #FG IMG AND BUTTON
        img2 = Image.open(r"C:\Users\aniru\OneDrive\Desktop\Face Recognition System\Images\train_data.png")
        img2 = img2.resize((300, 100), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b1 = Button(bg_img_train, image=self.photoimg2,command=self.train_classify,cursor="hand2")
        b1.place(x=800, y=450, width=300, height=100)


#---------- FUNCTION -----------------
    def train_classify(self):
        data_dir=("img_data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #Gray scale image
            img_np=np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])


            faces.append(img_np)
            ids.append(id)
            cv2.imshow("Training",img_np)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #------------- Training classifier and save---------------

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed")
        


        

        






if __name__ == "__main__":
    root = tk.Tk()
    obj = Train(root)
    root.mainloop()