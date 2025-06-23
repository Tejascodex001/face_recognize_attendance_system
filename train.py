from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np



class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Train Data")



        title_lbl=Label(self.root,text="                                                    TRAIN DATASET",font=("times new roman",35,"bold"),bg="white",fg="hotpink",anchor='w')
        title_lbl.place(x=0,y=0,width=1920,height=60)

        img_top=Image.open(r"C:\Users\tejas\Desktop\face recognize\Images\train1.jpg")
        img_top=img_top.resize((1920,330),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1920,height=350)

        #button
        b1_1=Button(self.root,text="                                                                          TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="red",fg="white",anchor='w')
        b1_1.place(x=0,y=380,width=1920,height=60)

        img_bottom=Image.open(r"C:\Users\tejas\Desktop\face recognize\Images\train2.jpg")
        img_bottom=img_bottom.resize((1920,330),Image.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=440,width=1920,height=350)


    def train_classifier(self):
        data_dir = os.path.abspath("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L')   #grayscale conversion
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #==========train the classifer===========
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Datasets completed!!!",parent=self.root)
        



        




if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()