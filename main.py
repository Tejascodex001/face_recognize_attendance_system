from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
from student import Student
import os
from time import strftime
from datetime import datetime
from train import Train
from face_recognition import Face_Recognition
from attendance import ATTENDANCE
from developer import Developer
from help import Help

class Face_recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition Sytem")

        #background image
        img=Image.open(r"C:\Users\tejas\Desktop\face recognize\Images\background2.jpg")
        img=img.resize((1920,1080),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=130,width=1920,height=950)

        #1st image
        img1=Image.open(r"C:\Users\tejas\Desktop\face recognize\Images\Background.jpg")
        img1=img1.resize((650,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=650,height=130)

        #2nd image
        img2=Image.open(r"C:\Users\tejas\Desktop\face recognize\Images\Background.jpg")
        img2=img2.resize((650,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=650,y=0,width=650,height=130)

        #3rd imag3
        img3=Image.open(r"C:\Users\tejas\Desktop\face recognize\Images\Background.jpg")
        img3=img3.resize((650,130),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1300,y=0,width=650,height=130)

        title_lbl=Label(bg_img,text="                        FACE RECOGNITION ATTENDENCE SOFTWARE",font=("times new roman",35,"bold"),bg="purple",fg="white",anchor='w')
        title_lbl.place(x=0,y=0,width=1920,height=60)

        #time
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=("times new roman",14,"bold"),background='white',foreground='blue')
        time()


        #student button
        img4=Image.open(r"C:\Users\tejas\Desktop\face recognize\Images\student.jpg")
        img4=img4.resize((220,220),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.Student_det_,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.Student_det_,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)

         #detect face button
        img5=Image.open(r"C:\Users\tejas\Desktop\face recognize\Images\face_id.jpg")
        img5=img5.resize((220,220),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b2=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.Face_data)
        b2.place(x=550,y=100,width=220,height=220)

        b2_1=Button(bg_img,text="Face Recognition",cursor="hand2",command=self.Face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_1.place(x=550,y=300,width=220,height=40)

         #Attendance button
        img6=Image.open(r"C:\Users\tejas\Desktop\face recognize\Images\attendance.jpg")
        img6=img6.resize((220,220),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b3=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b3.place(x=900,y=100,width=220,height=220)

        b3_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b3_1.place(x=900,y=300,width=220,height=40)

        #Helpdesk button
        img7=Image.open(r"C:\Users\tejas\Desktop\face recognize\Images\helpdesk.png")
        img7=img7.resize((220,220),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b4=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b4.place(x=1250,y=100,width=220,height=220)

        b4_1=Button(bg_img,text="Helpdesk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b4_1.place(x=1250,y=300,width=220,height=40)

        #image trainer button
        img8=Image.open(r"C:\Users\tejas\Desktop\face recognize\Images\trainer_img.jpg")
        img8=img8.resize((220,220),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b5=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.Train_data)
        b5.place(x=200,y=400,width=220,height=220)

        b5_1=Button(bg_img,text="Data Trainer",cursor="hand2",command=self.Train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b5_1.place(x=200,y=600,width=220,height=40)

         #photos face button
        img9=Image.open(r"C:\Users\tejas\Desktop\face recognize\Images\photos.jpg")
        img9=img9.resize((220,220),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b6=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b6.place(x=550,y=400,width=220,height=220)

        b6_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b6_1.place(x=550,y=600,width=220,height=40)

         #Developer button
        img10=Image.open(r"C:\Users\tejas\Desktop\face recognize\Images\developer.jpg")
        img10=img10.resize((220,220),Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b7=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b7.place(x=900,y=400,width=220,height=220)

        b7_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b7_1.place(x=900,y=600,width=220,height=40)

        #Exit button
        img11=Image.open(r"C:\Users\tejas\Desktop\face recognize\Images\exit.png")
        img11=img11.resize((220,220),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b8=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.Iexit)
        b8.place(x=1250,y=400,width=220,height=220)

        b8_1=Button(bg_img,text="Exit",cursor="hand2",command=self.Iexit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b8_1.place(x=1250,y=600,width=220,height=40)


    def open_img(self):
        os.startfile("Data")

    def Iexit(self):
        self.Iexit=tkinter.messagebox.askyesno("Face Recognisition","Are You Sure to Exit the App",parent=self.root)
        if self.Iexit>0:
            self.root.destroy()
        else:
            return

#==============Function button===============
    def Student_det_(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def Train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def Face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = ATTENDANCE(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)


    
    


if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition_System(root)
    root.mainloop()
