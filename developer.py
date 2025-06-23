from tkinter import *
from PIL import Image, ImageTk

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080")
        self.root.title("Developer Information")

        # Title Label
        title_lbl = Label(self.root, text="Meet the Developers", font=("Helvetica", 30, "bold"), bg="#3498db", fg="white", anchor='w')
        title_lbl.pack(fill=X, pady=10)

        # Background Image
        img_top = Image.open(r"C:\Users\tejas\Desktop\face recognize\Images\developer.jpg")
        img_top = img_top.resize((1920, 800), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.pack(side=TOP, fill=BOTH)

        # Frame for Developer Info
        main_frame = Frame(f_lbl, bd=2, bg="#2c3e50")
        main_frame.place(x=250, y=150, width=1200, height=400)

        # Developer Info Labels
        dev_label = Label(main_frame, text="Meet the Team", font=("Helvetica", 25, "bold"), bg="#3498db", fg="white")
        dev_label.pack(fill=X, pady=10)

        self.create_dev_label(main_frame, "Member 1", "Gaurava Mavaji", 80)
        self.create_dev_label(main_frame, "Member 2", "Tejas Gowda S", 150)
        self.create_dev_label(main_frame, "Department     ", "Artificial Intelligence and Data Science", 220)
        self.create_dev_label(main_frame, "Semester", "3", 290)

    def create_dev_label(self, frame, member_text, name_text, y_position):
        dev_label_member = Label(frame, text=member_text, font=("Helvetica", 20, "bold"), bg="#e74c3c", fg="white", width=15)
        dev_label_member.place(x=50, y=y_position)

        dev_label_name = Label(frame, text=name_text, font=("Helvetica", 20, "bold"), bg="#ecf0f1", width=45)
        dev_label_name.place(x=250, y=y_position)

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
