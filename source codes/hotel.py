from tkinter import *
from PIL import Image, ImageTk  # Ensure you have pillow installed: pip install pillow
from customer import Cust_win

class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        #========= first image =========

        img1 = Image.open(r"D:\python practice project\hotel images\hotel1.png")
        img1 = img1.resize((1600, 150), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1600, height=150)

        #=========== logo ==========

        img2=Image.open(r"D:\python practice project\hotel images\logohotel.png")
        img2=img2.resize((230,120), Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lablimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lablimg.place(x=0,y=0,height=120,width=170)

        #============= title =============

        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM", font=("times new roman",40,"bold"), bg="black" , fg="gold", bd=4,relief=RIDGE)
        lbl_title.place(x=-130,y=146,width=1700,height=50)

        #============= frame =============

        main_frame=Frame(self.root,bg="brown",bd=0,relief=RIDGE)
        main_frame.place(x=0,y=194,height=620,width=1550)

        #============== menu ============

        lbl_menu=Label(main_frame,text="MENU" , font=("times new roman ", 16,"bold"),bg="black" ,fg="gold" ,bd=4, relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=250,height=40)

        #============ button frame ========

        btn_frame = Frame(main_frame, bd=1, relief=RIDGE)
        btn_frame.place(x=0, y=39, width=241, height=183)

        cust_btn = Button(btn_frame, text="COSTOMER",command=self.cust_details, width=33, font=("times new roman", 10, "bold"), bg="black", fg="gold", bd=6, cursor="hand2")
        cust_btn.grid(row=0, column=0, padx=0, pady=1)  # Ensure padx is set to 0


        room_btn=Button(btn_frame,text="ROOM",width=33,font=("times new roman",10,"bold"),bg="black",fg="gold",bd=6,cursor="hand2")
        room_btn.grid(row=1,column=0,padx=0,pady=1)

        details_btn=Button(btn_frame,text="DETAILS",width=33,font=("times new roman",10,"bold"),bg="black",fg="gold",bd=6,cursor="hand2")
        details_btn.grid(row=2,column=0,padx=0,pady=1)

        report_btn=Button(btn_frame,text="REPORT",width=33,font=("times new roman",10,"bold"),bg="black",fg="gold",bd=6,cursor="hand2")
        report_btn.grid(row=3,column=0,padx=0,pady=1)

        logout_btn=Button(btn_frame,text="LOG OUT",width=33,font=("times new roman",10,"bold"),bg="black",fg="gold",bd=6,cursor="hand2")
        logout_btn.grid(row=4,column=0,padx=0,pady=1)

        #==================Image=========================

        img3 = Image.open(r"D:\python practice project\hotel images\slide3.jpg")
        img3=img3.resize((1295,700),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        labling1=Label(main_frame,image=self.photoimg3,bd=1,relief=RIDGE)
        labling1.place(x=240,y=0,width=1295,height=700)


        #=============== down side image ============

        img4=Image.open(r"D:\python practice project\hotel images\myh.jpg")
        img4=img4.resize((240,215),Image.LANCZOS)
        self.photoimag4=ImageTk.PhotoImage(img4)

        labling1=Label(main_frame,image=self.photoimag4,bd=2,relief=RIDGE)
        labling1.place(x=0,y=220,width=240,height=215)

        img5=Image.open(r"D:\python practice project\hotel images\khana.jpg")
        img5=img5.resize((240,215),Image.LANCZOS)
        self.photoimag5=ImageTk.PhotoImage(img5)

        labling1=Label(main_frame,image=self.photoimag5,bd=2,relief=RIDGE)
        labling1.place(x=0,y=430,width=240,height=215)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_win(self.new_window)

if __name__ == "__main__":
    root = Tk()
    app = HotelManagementSystem(root)
    root.mainloop()
