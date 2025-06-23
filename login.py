from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_recognition_System


def Main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()


class Login_window:
    def __init__(self, root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1920x1080+0+0")

        

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\tejas\Desktop\face recognize\Images\bg_login.jpg")
        lbl1_bg=Label(self.root,image=self.bg)
        lbl1_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=690,y=210,width=340,height=450)

        img1=Image.open(r"C:\Users\tejas\Desktop\face recognize\Images\login_i.png")
        img1=img1.resize((75,75),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg1=Label(image=self.photoimg1,bg="black", borderwidth=0)
        lblimg1.place(x=805,y=215,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #label
        useremail_lbl=Label(frame,text="User Email",font=("times new roman",15,"bold"),fg="white",bg="black")
        useremail_lbl.place(x=70,y=149)

        self.txtuser=ttk.Entry(frame,font=("times new roman",20,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        pass_lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        pass_lbl.place(x=70,y=220)

        self.txtpass=ttk.Entry(frame,font=("times new roman",20,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        #=========icon images=========

        img2=Image.open(r"C:\Users\tejas\Desktop\face recognize\Images\login_i.png")
        img2=img2.resize((25,25),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg2=Label(image=self.photoimg2,bg="black", borderwidth=0)
        lblimg2.place(x=731,y=359,width=25,height=25)

        img3=Image.open(r"C:\Users\tejas\Desktop\face recognize\Images\pass_.png")
        img3=img3.resize((25,25),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg3=Label(image=self.photoimg3,bg="black", borderwidth=0)
        lblimg3.place(x=731,y=429,width=25,height=25)

        #===============buttons==================

        #login button

        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),border=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=85,y=300,width=170,height=35)

        #register button

        registerbtn=Button(frame,text="New User? Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=20,y=350,width=170)

        #forgot passs button

        forg_pass_btn=Button(frame,command=self.forgot_pass_window,text="Forgot Password",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forg_pass_btn.place(x=10,y=370,width=170)



    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)




    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("error","All fields are required")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Tejas@23", database="database_face_")
            mycursor=conn.cursor()
            mycursor.execute("select * from user_data where Email=%s and Password=%s",(
                self.txtuser.get(),
                self.txtpass.get()
            ))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Email and Password")
            else:
                open_main=messagebox.askyesno("Info","Do you want to continue")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

#======================reset password=========================
    
    def reset_pass(self):
        if self.combo_security.get()=="Select":
            messagebox.showerror("Error","Select the Security Question",parent=self.root2)
        elif self.txt_securityans_entry.get()=="":
            messagebox.showerror("Error","Please Enter security answer",parent=self.root2)
        elif self.txt_new_pass_entry.get()=="":
            messagebox.showerror("Error","Please enter new password",parent=self.root2)
        else:
             conn = mysql.connector.connect(host="localhost", user="root", password="Tejas@23", database="database_face_")
             mycursor=conn.cursor()
             query=("select * from user_data where Email=%s and SecurityQ=%s and SecurityA=%s")
             value=(self.txtuser.get(),self.combo_security.get(),self.txt_securityans_entry.get())
             mycursor.execute(query,value)
             row=mycursor.fetchone()
             if row==None:
                 messagebox.showerror("Error","Please enter correct answer",parent=self.root2)
             else:
                 query1=("update user_data set Password=%s where Email=%s")
                 value1=(self.txt_new_pass_entry.get(),self.txtuser.get())
                 mycursor.execute(query1,value1)

                 conn.commit()
                 conn.close()
                 messagebox.showinfo("Info","Your Password has been Reset, Please login using New password",parent=self.root2)
                 self.root2.destroy()
                






#=======================forg pass window=====================
    def forgot_pass_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter your Email to address to reset password")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Tejas@23", database="database_face_")
            mycursor=conn.cursor()
            query=("select * from user_data where email=%s")
            value=(self.txtuser.get(),)
            mycursor.execute(query, value)
            row=mycursor.fetchone()
            #print(row)
            if(row==None):
                messagebox.showerror("Error","Please Enter Valid Email")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+690+200")

                l=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security=Label(self.root2,text="Select security questions",font=("times new roman",17,"bold"),bg="white",fg="black")
                security.place(x=50,y=80)

                self.combo_security=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security["values"]=("Select","Your Birth Place","Your favourite animal","Your favourite subject")
                self.combo_security.place(x=50,y=110,width=250)
                self.combo_security.current(0)


                self.txt_securityans=Label(self.root2,text="Security answer",font=("times new roman",20,"bold"),bg="white",fg="black")
                self.txt_securityans.place(x=50,y=150)

                self.txt_securityans_entry=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_securityans_entry.place(x=50,y=180,width=250)

                self.txt_new_pass=Label(self.root2,text="New Password",font=("times new roman",20,"bold"),bg="white",fg="black")
                self.txt_new_pass.place(x=50,y=220)

                self.txt_new_pass_entry=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_new_pass_entry.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",20,"bold"),bg="green",fg="white")
                btn.place(x=80,y=300,width=170)





class Register:
    def __init__(self, root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1920x1080+0+0")


    #===============variables=============== 

        self.var_fname=StringVar() 
        self.var_lname=StringVar() 
        self.var_contact=StringVar() 
        self.var_email=StringVar() 
        self.var_security=StringVar() 
        self.var_securityans=StringVar() 
        self.var_password=StringVar() 
        self.var_confpass=StringVar() 


        #======bgimg=========

        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\tejas\Desktop\face recognize\Images\register_bg.jpg")
        bg_lbl=Label(self.root,image=self.bg1)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        #=======man frame========

        frame=Frame(self.root,bg="purple")
        frame.place(x=425,y=170,width=800,height=550)


        register_lbl=Label(frame,text="REGISTER HERE", font=("times new roman",20,"bold"),fg="yellow",bg="purple")
        register_lbl.place(x=20,y=20)

        #============labels and entries===========

        fname=Label(frame,text="First name",font=("times new roman",20,"bold"),bg="purple",fg="White")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        lname=Label(frame,text="Last name",font=("times new roman",20,"bold"),bg="purple",fg="White")
        lname.place(x=370,y=100)

        lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        lname_entry.place(x=370,y=130,width=250)

        #==2nd row=========

        contact=Label(frame,text="Contact no",font=("times new roman",20,"bold"),bg="purple",fg="White")
        contact.place(x=50,y=170)

        contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        contact_entry.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",20,"bold"),bg="purple",fg="White")
        email.place(x=370,y=170)

        email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        email_entry.place(x=370,y=200,width=250)


        #===3rd row==========

        security=Label(frame,text="Select security questions",font=("times new roman",17,"bold"),bg="purple",fg="White")
        security.place(x=50,y=240)

        self.combo_security=ttk.Combobox(frame,textvariable=self.var_security,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security["values"]=("Select","Your Birth Place","Your favourite animal","Your favourite subject")
        self.combo_security.place(x=50,y=270,width=250)
        self.combo_security.current(0)


        securityans=Label(frame,text="Security answer",font=("times new roman",20,"bold"),bg="purple",fg="White")
        securityans.place(x=370,y=240)

        securityans_entry=ttk.Entry(frame,textvariable=self.var_securityans,font=("times new roman",15))
        securityans_entry.place(x=370,y=270,width=250)

        #===4th row==========

        password=Label(frame,text="Password",font=("times new roman",20,"bold"),bg="purple",fg="White")
        password.place(x=50,y=310)

        password_entry=ttk.Entry(frame,textvariable=self.var_password,font=("times new roman",15,"bold"))
        password_entry.place(x=50,y=340,width=250)

        confpass=Label(frame,text="Confirm Password",font=("times new roman",18,"bold"),bg="purple",fg="White")
        confpass.place(x=370,y=310)

        confpass_entry=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        confpass_entry.place(x=370,y=340,width=250)

        #===============check button=============
        self.var_check=IntVar()
        check_btn=Checkbutton(frame,variable=self.var_check,text="I Agree the Terms and Conditions",font=("times new roman",13,"bold"),bg="purple",fg="black",activebackground="purple",activeforeground="black",onvalue=1,offvalue=0)
        check_btn.place(x=50,y=380)

        #===============Buttons=====================

        img=Image.open(r"C:\Users\tejas\Desktop\face recognize\Images\register-button.png")
        img=img.resize((200,50),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        b1=Button(frame,image=self.photoimg,command=self.register_data,borderwidth=0,bg="purple",activebackground="purple",cursor="hand2")
        b1.place(x=30,y=440,width=200)

        img1=Image.open(r"C:\Users\tejas\Desktop\face recognize\Images\login-button.png")
        img1=img1.resize((200,50),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        b2=Button(frame,command=self.switch_to_login,image=self.photoimg1,borderwidth=0,bg="purple",activebackground="purple",cursor="hand2")
        b2.place(x=350,y=440,width=200)


    def switch_to_login(self):
        self.root.destroy()
        



#====fuction for registration===============
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_security.get()=="Select":
            messagebox.showerror("Error","All fields are required",parent=self.root)

        elif self.var_securityans.get()=="":
                messagebox.showerror("Error","Please enter the answer for the security question",parent=self.root)

        elif self.var_password.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password is not Matching",parent=self.root)

        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Accept the Terms and Condtions to Continue",parent=self.root)

        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Tejas@23", database="database_face_")
            mycursor=conn.cursor()
            query=("select * from user_data where Email=%s")
            value=(self.var_email.get(),)
            mycursor.execute(query, value)
            row=mycursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already Exists with the Same Email, Please Try another Email",parent=self.root)
            else:
                mycursor.execute("insert into user_data values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_security.get(),
                    self.var_securityans.get(),
                    self.var_password.get()
                                         ))
            
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered Successfully")
            


    



    

               





if __name__=="__main__":
    Main()