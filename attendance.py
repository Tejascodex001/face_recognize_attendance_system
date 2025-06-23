from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]


class ATTENDANCE:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Student Details")


        #variables=====================
        self.var_Name=StringVar()
        self.var_date=StringVar()
        self.var_dep=StringVar()
        self.var_sem=StringVar()
        self.var_time=StringVar()
        self.var_USN=StringVar()
        self.var_attend_stat=StringVar()

        #1st image
        img1=Image.open(r"C:\Users\tejas\Desktop\face recognize\Images\attendance100.jpg")
        img1=img1.resize((950,200),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=850,height=200)

        #2nd image
        img2=Image.open(r"C:\Users\tejas\Desktop\face recognize\Images\attendance200.jpg")
        img2=img2.resize((950,200),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=850,y=0,width=850,height=200)

        #background image
        img=Image.open(r"C:\Users\tejas\Desktop\face recognize\Images\background2.jpg")
        img=img.resize((1920,1080),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=200,width=1920,height=950)

        title_lbl=Label(bg_img,text="                                           ATTENDANCE MANAGEMENT",font=("times new roman",35,"bold"),bg="white",fg="orange",anchor='w')
        title_lbl.place(x=0,y=0,width=1920,height=60)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=-1,y=65,width=1860,height=910)

        #left frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=850,height=600)

        img_left=Image.open(r"C:\Users\tejas\Desktop\face recognize\Images\studentimg4.jpg")
        img_left=img_left.resize((830,130),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=830,height=130)

        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=135,width=840,height=430)

        #labels and entries

        #USN
        attendanceid_label=Label(left_inside_frame,text="USN:",font=("times new roman",13,"bold"),bg="white")
        attendanceid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceid_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_USN,font=("times new roman",13,"bold"))
        attendanceid_entry.grid(row=0,column=1,padx=10,pady=8,sticky=W)

        #Name
        Nameid_label=Label(left_inside_frame,text="Name:",font=("comicsansns",11,"bold"),bg="white")
        Nameid_label.grid(row=0,column=2,padx=10,pady=8,sticky=W)

        Nameid_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_Name,font=("comicsansns",13,"bold"))
        Nameid_entry.grid(row=0,column=3,padx=10,pady=8,sticky=W)

        #Date
        Date_label=Label(left_inside_frame,text="Date:",font=("comicsansns",11,"bold"),bg="white")
        Date_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        Date_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_date,font=("comicsansns",13,"bold"))
        Date_entry.grid(row=1,column=1,padx=10,pady=8,sticky=W)

        #Time
        Sem_label=Label(left_inside_frame,text="Time:",font=("comicsansns",11,"bold"),bg="white")
        Sem_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        Sem_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_time,font=("comicsansns",13,"bold"))
        Sem_entry.grid(row=1,column=3,padx=10,pady=8,sticky=W)

        #Department
        time_label=Label(left_inside_frame,text="Department:",font=("comicsansns",11,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        time_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_dep,font=("comicsansns",13,"bold"))
        time_entry.grid(row=2,column=1,padx=10,pady=8,sticky=W)

        #semester
        Date_label=Label(left_inside_frame,text="Semester:",font=("comicsansns",11,"bold"),bg="white")
        Date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        Date_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_sem,font=("comicsansns",13,"bold"))
        Date_entry.grid(row=2,column=3,padx=10,pady=8,sticky=W)

        #Attendance status
        Status_label=Label(left_inside_frame,text="Attendance Status:",font=("comicsansns",11,"bold"),bg="white")
        Status_label.grid(row=3,column=0,padx=10,pady=8,sticky=W)

        

        Status_combo=ttk.Combobox(left_inside_frame,font=("comicsansns",13,"bold"),state="readonly",width=20,textvariable=self.var_attend_stat)
        Status_combo["values"]=("Present","Absent")
        Status_combo.current(0)
        Status_combo.grid(row=3,column=1,padx=10,pady=8,sticky=W)
        Status_combo.current(0)

         #button frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=350,width=625,height=40)

        save_btn=Button(btn_frame,text="Import CSV",command=self.importCSV,width=20,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export CSV",command=self.exportCSV,width=20,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        

        Reset_btn=Button(btn_frame,text="Reset",width=20,command=self.reset_data,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Reset_btn.grid(row=0,column=3)






        #right frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        right_frame.place(x=870,y=10,width=800,height=600)

        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=780,height=565)

        #============scroll bar table===========

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("USN","Name","Department","Semester","Time","Date","Status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("USN",text="USN")
        self.AttendanceReportTable.heading("Name",text="Name")
        self.AttendanceReportTable.heading("Department",text="Department")
        self.AttendanceReportTable.heading("Semester",text="Semester")
        self.AttendanceReportTable.heading("Time",text="Time")
        self.AttendanceReportTable.heading("Date",text="Date")
        self.AttendanceReportTable.heading("Status",text="Attendance Status")

        self.AttendanceReportTable["show"]="headings"
        
        self.AttendanceReportTable.column("USN",width=100)
        self.AttendanceReportTable.column("Name",width=100)
        self.AttendanceReportTable.column("Department",width=100)
        self.AttendanceReportTable.column("Semester",width=100)
        self.AttendanceReportTable.column("Time",width=100)
        self.AttendanceReportTable.column("Date",width=100)
        self.AttendanceReportTable.column("Status",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

        #=====================Fetch data=================

    def fetchdata(self,rows):
            self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
            for i in rows:
                 self.AttendanceReportTable.insert("",END,values=i)


#import csv
    def importCSV(self):
         global mydata
         mydata.clear()
         Fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
         with open(Fln) as myfile:
              csvread=csv.reader(myfile,delimiter=",")
              for i in csvread:
                   mydata.append(i)
              self.fetchdata(mydata)


#export csv
    def exportCSV(self):
         try:
              if len(mydata)<1:
                   messagebox.showerror("NO DATA","No Data Found to export",parent=self.root)
                   return False
              fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
              with open(fln,mode="w",newline="") as myfile:
                   exp_write=csv.writer(myfile,delimiter=",")
                   for i in mydata:
                        exp_write.writerow(i)
                   messagebox.showinfo("DATA EXPORT","Your data exported to "+os.path.basename(fln)+" successfully",parent=self.root)
         except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Database Error: {err}", parent=self.root)


    def get_cursor(self, event=""):
         cursor_row=self.AttendanceReportTable.focus()
         if cursor_row:
               content=self.AttendanceReportTable.item(cursor_row)
               rows=content["values"]
               self.var_USN.set(rows[0])
               self.var_Name.set(rows[1])
               self.var_dep.set(rows[2])
               self.var_sem.set(rows[3])
               self.var_time.set(rows[4])
               self.var_date.set(rows[5])
               self.var_attend_stat.set(rows[6])
         else:
              messagebox.showerror("No selection","Please select a row from table!",parent=self.root)
              



    def reset_data(self):
         self.var_USN.set("")
         self.var_Name.set("")
         self.var_dep.set("")
         self.var_sem.set("")
         self.var_time.set("")
         self.var_date.set("")
         self.var_attend_stat.set("")


    









if __name__ == "__main__":
    root = Tk()
    obj = ATTENDANCE(root)
    root.mainloop()