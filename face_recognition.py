from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import csv
import os
import numpy as np
from time import strftime
from datetime import datetime
import csv

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition")

        title_lbl = Label(self.root, text="                                                     FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white",
                          fg="green", anchor='w')
        title_lbl.place(x=0, y=0, width=1920, height=60)

        # 1st image
        img_top = Image.open(r"C:\Users\tejas\Desktop\face recognize\Images\face_recognize1.png")
        img_top = img_top.resize((850, 800), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=850, height=800)

        # 2nd image
        img_bottom = Image.open(r"C:\Users\tejas\Desktop\face recognize\Images\face_recognize2.png")
        img_bottom = img_bottom.resize((850, 800), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=850, y=55, width=850, height=800)

        # button
        b1_1 = Button(f_lbl, text="Recognize Face", cursor="hand2", font=("times new roman", 20, "bold"),
                      bg="darkgreen", fg="white", anchor='w', command=self.face_recognize)
        b1_1.place(x=325, y=650, width=200, height=40)

        # =================attendance============
        self.recognized_faces = set()

    
    
    def mark_attendance(self, r,n,d,s):
        with open(r"C:\Users\tejas\Desktop\face recognize\Attendance.csv","r+",newline="\n") as f:
            mydataList=f.readlines()
            name_List=[]
	        
            for line in mydataList:
                entry=line.split((","))
                name_List.append(entry[0])
            if(((r not in name_List) and (n not in name_List) and (d not in name_List) and (s not in name_List))):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{r},{n},{d},{s},{dtString},{d1},Present")




    # face recognition
    def face_recognize(self):
        #recognized_faces=set()
        def draw_boundary(img, classifier, scaleFactor, minNeighbour, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbour)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, prediction = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - prediction / 300)))

                conn = mysql.connector.connect(host="localhost", user="root", password="Tejas@23",database="database_face_")
                my_cursor = conn.cursor()

                my_cursor.execute("select Student_name from student where Attendance_id=" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute("select Department from student where Attendance_id=" + str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                my_cursor.execute("select Semester from student where Attendance_id=" + str(id))
                s = my_cursor.fetchone()
                s = "+".join(s)

                my_cursor.execute("select USN from student where Attendance_id=" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)

                if confidence > 70:
                    cv2.putText(img, f"USN:{r}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name:{n}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{d}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Semester:{s}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(r, n, d, s)
                    self.recognized_faces.add(id)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, f"Unknown Face", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)
        

        while True:
            ret, Img = video_cap.read()
            Img = recognize(Img, clf, faceCascade)
            cv2.imshow("WELCOME TO FACE RECOGNITION", Img)

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
