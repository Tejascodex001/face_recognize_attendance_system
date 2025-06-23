from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import filedialog
import mysql.connector
import cv2
import os
import glob
import shutil




class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Student Details")


        #==============variables=============
        self.var_dep=StringVar()
        self.var_Year=StringVar()
        self.var_Semester=StringVar()
        self.var_AttendanceID=StringVar()
        self.var_Student_Name=StringVar()
        self.var_Gender=StringVar()
        self.var_email=StringVar()
        self.var_Phone_no=StringVar()
        self.var_DOB=StringVar()
        self.var_Mentor=StringVar()
        self.var_USN=StringVar()
        self.var_Search = StringVar()
        self.var_Search_by = StringVar()
        

        #background image
        img=Image.open(r"C:\Users\tejas\Desktop\face recognize\Images\background2.jpg")
        img=img.resize((1920,1080),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=130,width=1920,height=950)

         #1st image
        img1=Image.open(r"C:\Users\tejas\Desktop\face recognize\Images\studentimg1.jpg")
        img1=img1.resize((650,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=650,height=130)

        #2nd image
        img2=Image.open(r"C:\Users\tejas\Desktop\face recognize\Images\studentimg2.jpg")
        img2=img2.resize((650,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=650,y=0,width=650,height=130)

        #3rd imag3
        img3=Image.open(r"C:\Users\tejas\Desktop\face recognize\Images\studentimg3.jpg")
        img3=img3.resize((650,130),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1300,y=0,width=650,height=130)

        title_lbl=Label(bg_img,text="                                       STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen",anchor='w')
        title_lbl.place(x=0,y=0,width=1920,height=60)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=-1,y=65,width=1860,height=910)

        #left frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=850,height=650)

        img_left=Image.open(r"C:\Users\tejas\Desktop\face recognize\Images\studentimg4.jpg")
        img_left=img_left.resize((830,130),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=830,height=130)

        #current department
        _department_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Department Info",font=("times new roman",12,"bold"))
        _department_frame.place(x=5,y=135,width=830,height=150)

        #department
        dep_label=Label(_department_frame,text="Department",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(_department_frame,textvariable=self.var_dep,font=("times new roman",13,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","CSE","ISE","Civil","Mechanical","AI-Data Science","AI-ML","EEE","ECE")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Year
        dep_label=Label(_department_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=2,padx=10,sticky=W)

        dep_combo=ttk.Combobox(_department_frame,textvariable=self.var_Year,font=("times new roman",13,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Year","2020-2021","2021-2022","2022-2023","2023-2024","2024-2025")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

         #Semester
        dep_label=Label(_department_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=1,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(_department_frame,textvariable=self.var_Semester,font=("times new roman",13,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        
        #class student information
        class_Student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Info",font=("times new roman",12,"bold"))
        class_Student_frame.place(x=5,y=285,width=830,height=330)

        #Attendance id
        Attendance_label=Label(class_Student_frame,text="AttendanceID",font=("times new roman",13,"bold"),bg="white")
        Attendance_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        Attendance_entry=ttk.Entry(class_Student_frame,textvariable=self.var_AttendanceID,width=20,font=("times new roman",13,"bold"))
        Attendance_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student name
        Studentname_label=Label(class_Student_frame,text="Student Name",font=("times new roman",13,"bold"),bg="white")
        Studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentname_entry=ttk.Entry(class_Student_frame,textvariable=self.var_Student_Name,width=20,font=("times new roman",13,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Gender
        Studentgender_label=Label(class_Student_frame,text="Gender",font=("times new roman",13,"bold"),bg="white")
        Studentgender_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        

        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_Gender,font=("times new roman",13,"bold"),state="readonly",width=18)
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)


        #Email
        Studentmail_label=Label(class_Student_frame,text="email",font=("times new roman",13,"bold"),bg="white")
        Studentmail_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        studentmail_entry=ttk.Entry(class_Student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        studentmail_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Phone no
        Studentph_label=Label(class_Student_frame,text="Phone number",font=("times new roman",13,"bold"),bg="white")
        Studentph_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        studentph_entry=ttk.Entry(class_Student_frame,textvariable=self.var_Phone_no,width=20,font=("times new roman",13,"bold"))
        studentph_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #DOB
        Studentdob_label=Label(class_Student_frame,text="DOB",font=("times new roman",13,"bold"),bg="white")
        Studentdob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        studentdob_entry=ttk.Entry(class_Student_frame,textvariable=self.var_DOB,width=20,font=("times new roman",13,"bold"))
        studentdob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)


        #Mentor
        Studentadd_label=Label(class_Student_frame,text="Mentor",font=("times new roman",13,"bold"),bg="white")
        Studentadd_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        studentadd_entry=ttk.Entry(class_Student_frame,textvariable=self.var_Mentor,width=20,font=("times new roman",13,"bold"))
        studentadd_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #USN
        USN_label=Label(class_Student_frame,text="USN",font=("times new roman",13,"bold"),bg="white")
        USN_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        USN_entry=ttk.Entry(class_Student_frame,textvariable=self.var_USN,width=20,font=("times new roman",13,"bold"))
        USN_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)



        #radio buttons
        self.var_radio1=StringVar()
        Radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="TAKE PHOTO SAMPLE",value="Yes")
        Radiobtn1.grid(row=6,column=0)

        Radiobtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="NO PHOTO SAMPLE",value="No")
        Radiobtn2.grid(row=6,column=1)

        #button frame
        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=825,height=40)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=20,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=20,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        Delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=20,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Delete_btn.grid(row=0,column=2)

        Reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=20,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Reset_btn.grid(row=0,column=3)

        btn1_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn1_frame.place(x=0,y=240,width=825,height=40)

        take_photo_btn=Button(btn1_frame,command=self.generate_dataset,text="Take Photo Sample",width=40,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        Update_photo_btn=Button(btn1_frame,text="Update Photo Sample",command=self.update_photos,width=40,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Update_photo_btn.grid(row=0,column=1)




        #right frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=870,y=10,width=800,height=650)

        #right frame
        img_right=Image.open(r"C:\Users\tejas\Desktop\face recognize\Images\std5.jpeg")
        img_right=img_right.resize((830,130),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=830,height=130)

        #=========Search System=========

        Search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=135,width=790,height=100)

        Search_label=Label(Search_frame,text="Search by:",font=("times new roman",15,"bold"),bg="red",fg="white")
        Search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        Search_combo=ttk.Combobox(Search_frame,font=("times new roman",13,"bold"),state="readonly",width=15,textvariable=self.var_Search_by)
        Search_combo["values"]=("Select","USN","Student Name","Mentor")
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        Search_entry=ttk.Entry(Search_frame,width=18,font=("times new roman",13,"bold"),textvariable=self.var_Search)
        Search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        Search_btn=Button(Search_frame,text="Search",command=self.search_data,width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Search_btn.grid(row=0,column=3,padx=4)

        ShowAll_btn=Button(Search_frame,text="Show All",command=self.show_all_data,width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        ShowAll_btn.grid(row=0,column=4,padx=4)

        #==========table frame==========
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=245,width=790,height=370)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,columns=("Dep","Year","Sem","aID","Name","Gender","Email","PH.no","DOB","Mentor","USN","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Dep",text="Department")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Sem",text="Semester")
        self.student_table.heading("aID",text="AttendanceID")
        self.student_table.heading("Name",text="Student Name")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("PH.no",text="Phone number")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Mentor",text="Mentor")
        self.student_table.heading("USN",text="USN")
        self.student_table.heading("Photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("Dep",width=180)
        self.student_table.column("Year",width=180)
        self.student_table.column("Sem",width=180)
        self.student_table.column("aID",width=180)
        self.student_table.column("Name",width=180)
        self.student_table.column("Gender",width=180)
        self.student_table.column("Email",width=180)
        self.student_table.column("PH.no",width=180)
        self.student_table.column("DOB",width=180)
        self.student_table.column("Mentor",width=180)
        self.student_table.column("USN",width=180)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()


    #==============function declaration=========    
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_AttendanceID.get() == "" or self.var_Student_Name.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Tejas@23", database="database_face_")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_dep.get(),
                    self.var_Year.get(),
                    self.var_Semester.get(),
                    self.var_AttendanceID.get(),
                    self.var_Student_Name.get(),
                    self.var_Gender.get(),
                    self.var_email.get(),
                    self.var_Phone_no.get(),
                    self.var_DOB.get(),
                    self.var_Mentor.get(),
                    self.var_USN.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details have been added successfully", parent=self.root)
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Database Error: {err}", parent=self.root)




   #=================fetch data==============
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="Tejas@23", database="database_face_")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #===========get cursor=============
    def get_cursor(self, event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data1=content["values"]
        
        self.var_dep.set(data1[0]),
        self.var_Year.set(data1[1]),
        self.var_Semester.set(data1[2]),
        self.var_AttendanceID.set(data1[3]),
        self.var_Student_Name.set(data1[4]),
        self.var_Gender.set(data1[5]),
        self.var_email.set(data1[6]),
        self.var_Phone_no.set(data1[7]),
        self.var_DOB.set(data1[8]),
        self.var_Mentor.set(data1[9]),
        self.var_USN.set(data1[10]),
        self.var_radio1.set(data1[11])

        #update function
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_AttendanceID.get() == "" or self.var_Student_Name.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if update:
                    conn = mysql.connector.connect(host="localhost", user="root", password="Tejas@23", database="database_face_")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Department=%s,Year=%s,Semester=%s,Attendance_id=%s,Student_name=%s,Gender=%s,Email=%s,Phone_no=%s,DOB=%s,Mentor=%s,USN=%s,PhotoSample=%s where Attendance_id=%s",(
                    self.var_dep.get(),
                    self.var_Year.get(),
                    self.var_Semester.get(),
                    self.var_AttendanceID.get(),
                    self.var_Student_Name.get(),
                    self.var_Gender.get(),
                    self.var_email.get(),
                    self.var_Phone_no.get(),
                    self.var_DOB.get(),
                    self.var_Mentor.get(),
                    self.var_USN.get(),
                    self.var_radio1.get(),
                    self.var_AttendanceID.get()
                    ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Database Error: {err}", parent=self.root)


    #delete function
    def delete_data(self):
        if self.var_AttendanceID.get()=="":
            messagebox.showerror("Error","Student id is required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete:
                    conn = mysql.connector.connect(host="localhost", user="root", password="Tejas@23", database="database_face_")
                    my_cursor = conn.cursor()
                    sql="delete from student where Attendance_id=%s"
                    val=(self.var_AttendanceID.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)   
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Database Error: {err}", parent=self.root)

    #reset fucntion
    def reset_data(self):
         self.var_dep.set("Select Department"),
         self.var_Year.set("select Year"),
         self.var_Semester.set("Select Semester"),
         self.var_AttendanceID.set(""),
         self.var_Student_Name.set(""),
         self.var_Gender.set("Male"),
         self.var_email.set(""),
         self.var_Phone_no.set(""),
         self.var_DOB.set(""),
         self.var_Mentor.set(""),
         self.var_USN.set(""),
         self.var_radio1.set("")


    #===============generate data set or take photo samples=================
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_AttendanceID.get() == "" or self.var_Student_Name.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Tejas@23", database="database_face_")
                my_cursor = conn.cursor()

                selected_id = self.var_AttendanceID.get()  # Get selected Attendance ID

                # Update student data using selected ID
                my_cursor.execute("update student set Department=%s,Year=%s,Semester=%s,Attendance_id=%s,Student_name=%s,Gender=%s,Email=%s,Phone_no=%s,DOB=%s,Mentor=%s,USN=%s,PhotoSample=%s where Attendance_id=%s", (
                    self.var_dep.get(),
                    self.var_Year.get(),
                    self.var_Semester.get(),
                    self.var_AttendanceID.get(),
                    self.var_Student_Name.get(),
                    self.var_Gender.get(),
                    self.var_email.get(),
                    self.var_Phone_no.get(),
                    self.var_DOB.get(),
                    self.var_Mentor.get(),
                    self.var_USN.get(),
                    self.var_radio1.get(),
                    selected_id
                ))
                conn.commit()


                face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0

                while True:
                    ret, myframe = cap.read()
                    if face_cropped(myframe) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(myframe), (500, 500))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "Data/user." + str(selected_id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating Dataset Completed!!!", parent=self.root)

            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Database Error: {err}", parent=self.root)
            except Exception as e:  # Additional change for generic error handling
                messagebox.showerror("Error", f"Error: {e}", parent=self.root)
                conn.close()  # Close connection even on errors



    def update_photos(self):
        if self.var_AttendanceID.get() == "":
            messagebox.showerror("Error", "Please select a student to update photos", parent=self.root)
        else:
            try:
                folder_path = "Data"
                student_id = self.var_AttendanceID.get()

                existing_photos = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

                if existing_photos:
                    response = messagebox.askyesno("Action", "Photos for this student already exist. Do you want to delete and retake the photos?", parent=self.root)
                    if response:
                        for photo in existing_photos:
                            if photo.startswith(f"user.{student_id}."):
                                os.remove(os.path.join(folder_path, photo))
                        
                        return
                    else:
                        messagebox.showinfo("Info", "Existing photos will be kept.", parent=self.root)
                        return

                self.take_or_update_photos(folder_path, student_id)

            except Exception as e:
                messagebox.showerror("Error", f"Error: {e}", parent=self.root)


    def take_or_update_photos(self, folder_path, student_id):
        try:
            face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

            cap = cv2.VideoCapture(0)
            img_id = 0

            existing_photos = glob.glob(os.path.join(folder_path, f"user.{student_id}.*.jpg"))

            if existing_photos:
                img_id = max([int(os.path.splitext(os.path.basename(photo))[0].split(".")[-1]) for photo in existing_photos])

            while True:
                ret, myframe = cap.read()

                # Convert to grayscale before processing
                gray = cv2.cvtColor(myframe, cv2.COLOR_BGR2GRAY)

                # Detect faces in the grayscale image
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)

                if len(faces) > 0:  # Check if any faces are detected
                    for (x, y, w, h) in faces:
                        # Combine cropping and conversion in one step
                        face_cropped = cv2.cvtColor(myframe[y:y + h, x:x + w], cv2.COLOR_BGR2GRAY)

                        img_id += 1
                        face = cv2.resize(face_cropped, (500, 500))  # Resize the grayscale image

                        new_file_name = f"user.{student_id}.{img_id}.jpg"
                        new_file_path = os.path.join(folder_path, new_file_name)

                        cv2.imwrite(new_file_path, face)
                        cv2.putText(myframe, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                        cv2.imshow('Face Cropper', myframe)
                        break  # Exit the loop after capturing one face

                if cv2.waitKey(1) == 13 or int(img_id) == 100:
                    break

            cap.release()
            cv2.destroyAllWindows()

        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}", parent=self.root)


    def face_cropped(self, img):
        face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            face_cropped = img[y:y + h, x:x + w]
            return face_cropped

            
    
    



# ===========Search function=============
    def search_data(self):
        if self.var_Search.get() == "":
            messagebox.showerror("Error", "Please enter a value to search", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Tejas@23", database="database_face_")
                my_cursor = conn.cursor()

                if self.var_Search_by.get() == "USN":
                    my_cursor.execute("select * from student where USN=%s", (self.var_Search.get(),))
                elif self.var_Search_by.get() == "Student Name":
                    my_cursor.execute("select * from student where Student_name=%s", (self.var_Search.get(),))
                elif self.var_Search_by.get() == "Mentor":
                    my_cursor.execute("select * from student where Mentor=%s", (self.var_Search.get(),))
                else:
                    messagebox.showerror("Error", "Please select a valid search criteria", parent=self.root)
                    return

                data = my_cursor.fetchall()

                if len(data) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("", END, values=i)
                    conn.commit()
                else:
                    messagebox.showinfo("Info", "No matching records found", parent=self.root)

                conn.close()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Database Error: {err}", parent=self.root)


    def show_all_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="Tejas@23", database="database_face_")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from student")
            data = my_cursor.fetchall()

            if len(data) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("", END, values=i)
                conn.commit()
            else:
                messagebox.showinfo("Info", "No records found", parent=self.root)

            conn.close()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database Error: {err}", parent=self.root)
















if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()