from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2




class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Developer")

        title_lbl=Label(self.root,text="                                                            HELP DESK ",font=("times new roman",35,"bold"),bg="white",fg="blue",anchor='w')
        title_lbl.place(x=0,y=0,width=1920,height=60)

        img_top=Image.open(r"C:\Users\tejas\Desktop\face recognize\Images\Hbackground.jpg")
        img_top=img_top.resize((1920,1080),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1920,height=800)
        dev_label=Label(f_lbl,text="HelpLine No:0000 0000\nEmail:xyz@gmail.com\nvisit www.abc.co.in for more info",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=650,y=300)






if __name__ == "__main__":
    root = Tk()
    obj = help(root)
    root.mainloop()