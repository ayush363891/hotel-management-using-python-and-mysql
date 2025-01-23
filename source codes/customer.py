from tkinter import*
from tkinter.ttk import Combobox
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox


class Cust_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital management system")
        self.root.geometry("1295x575+241+226")

        #============= veriables ===============
        self.var_ref=StringVar()
        x = random.randint(1000, 9999)
        self.var_ref.set(x)

        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality = StringVar()
        self.var_address = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number=StringVar()



        #============= title ===========

        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=0,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1290,height=50)

        #============= Logo =============

        img1=Image.open(r"D:\python practice project\hotel images\logohotel.png")
        img1=img1.resize((100,50),Image.Resampling.LANCZOS)
        self.PhotoImage=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.PhotoImage,bd=0,relief=RIDGE)
        lblimg.place(x=0,y=0,width=100,height=50)

        #============= LabelFrame ==========

        lblframeleft=LabelFrame(self.root, text="Customer Details",font=("times new roman",12,"bold"),bd=3,relief=RIDGE)
        lblframeleft.place(x=5,y=50,width=400,height=500)

        #============ Labels and entries =============
        #costomer ref
        lbl_cust_ref=Label(lblframeleft,text="Customer Ref",font=("arial",10,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
        entry_ref=ttk.Entry(lblframeleft,width=30,textvariable=self.var_ref,font=("arial",10,"bold"),state="readonly")
        entry_ref.grid(row=0,column=1)

        #costomer name

        lbl_cust_name=Label(lblframeleft,text="Customer Name:",font=("arial",10,"bold"),padx=2,pady=6)
        lbl_cust_name.grid(row=1,column=0,sticky=W)
        entry_cust_name=ttk.Entry(lblframeleft,width=30,textvariable=self.var_cust_name,font=("arial",10,"bold"))
        entry_cust_name.grid(row=1,column=1)

        #mother name

        lbl_mother_name=Label(lblframeleft,text="Mother Name:",font=("arial",10,"bold"),padx=2,pady=6)
        lbl_mother_name.grid(row=2,column=0,sticky=W)
        entry_mother_name=ttk.Entry(lblframeleft,width=30,textvariable=self.var_mother,font=("arial",10,"bold"))
        entry_mother_name.grid(row=2,column=1)

        # gender

        lbl_gender=Label(lblframeleft,text="Gender:",font=("arial",10,"bold"),padx=2,pady=6)
        lbl_gender.grid(row=3,column=0,sticky=W)
        combo_gender=ttk.Combobox(lblframeleft,textvariable=self.var_gender,font=("arial",10,"bold",),width=28,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)



        # post code

        lbl_post_code=Label(lblframeleft,text="Post Code:",font=("arial",10,"bold"),padx=2,pady=6)
        lbl_post_code.grid(row=4,column=0,sticky=W)
        entry_post_code=ttk.Entry(lblframeleft,width=30,textvariable=self.var_post,font=("arial",10,"bold"))
        entry_post_code.grid(row=4,column=1)

        # Mobile

        lbl_mobile=Label(lblframeleft,text="Mobile:",font=("arial",10,"bold"),padx=2,pady=6)
        lbl_mobile.grid(row=5,column=0,sticky=W)
        entry_mobile = ttk.Entry(lblframeleft, width=30,textvariable=self.var_mobile, font=("arial", 10, "bold"))
        entry_mobile.grid(row=5, column=1)

        # Email

        lbl_email = Label(lblframeleft, text="Email:", font=("arial", 10, "bold"), padx=2, pady=6)
        lbl_email.grid(row=6, column=0, sticky=W)
        entry_email = ttk.Entry(lblframeleft, width=30, textvariable=self.var_email,font=("arial", 10, "bold"))
        entry_email.grid(row=6, column=1)

        # Nationality

        lbl_nationality = Label(lblframeleft, text="Nationality:", font=("arial", 10, "bold"), padx=2, pady=6)
        lbl_nationality.grid(row=7, column=0, sticky=W)
        combo_nationality=ttk.Combobox(lblframeleft,textvariable=self.var_nationality,font=("arial",10,"bold"),width=28,state="readonly")
        combo_nationality["value"]=("Indian","American","British","Russian")
        combo_nationality.current(0)
        combo_nationality.grid(row=7,column=1)


        # Id Proof Type

        lbl_id_proof_type = Label(lblframeleft, text="Id Proof Type:", font=("arial", 10, "bold"), padx=2, pady=6)
        lbl_id_proof_type.grid(row=8, column=0, sticky=W)
        combo_id_proof_type=ttk.Combobox(lblframeleft,textvariable=self.var_id_proof,font=("arial",10,"bold"),width=28,state="readonly")
        combo_id_proof_type["value"]=("Aadhar Card","Pan Card","Driving Licence","Passport")
        combo_id_proof_type.current(0)
        combo_id_proof_type.grid(row=8,column=1)



        # id number

        lbl_id_number = Label(lblframeleft, text="Id Number:", font=("arial", 10, "bold"), padx=2, pady=6)
        lbl_id_number.grid(row=9, column=0, sticky=W)
        entry_id_number = ttk.Entry(lblframeleft, width=30,textvariable=self.var_id_number, font=("arial", 10, "bold"))
        entry_id_number.grid(row=9, column=1)

        # address

        lbl_address = Label(lblframeleft, text="Address:", font=("arial", 10, "bold"), padx=2, pady=6)
        lbl_address.grid(row=10, column=0, sticky=W)
        entry_address = ttk.Entry(lblframeleft, width=30,textvariable=self.var_address ,font=("arial", 10, "bold"))
        entry_address.grid(row=10, column=1)

        #============== Buttons ======================

        btn_frame=Frame(lblframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=390,height=45)

        #Add

        btn_add=Button(btn_frame,text="Add",command=self.add_data,font=("arial",10,"bold"),bg="black",fg="gold",width=11,height=2)
        btn_add.grid(row=0,column=0)

        #update

        btn_update=Button(btn_frame,text="Update",command=self.update,font=("arial",10,"bold"),bg="black",fg="gold",width=11,height=2)
        btn_update=Button(btn_frame,text="Update",command=self.update,font=("arial",10,"bold"),bg="black",fg="gold",width=11,height=2)
        btn_update.grid(row=0,column=1)

        #delete

        btn_delete=Button(btn_frame,text="Delete",command=self.delete,font=("arial",10,"bold"),bg="black",fg="gold",width=11,height=2)
        btn_delete.grid(row=0,column=2)


        #resate

        btn_resat=Button(btn_frame,text="Reset",font=("arial",10,"bold"),bg="black",fg="gold",width=11,height=2)
        btn_resat.grid(row=0,column=3)


        #============= tableFrame ===============

        label_frame=LabelFrame(self.root,text="View details and search system",font=("arial",10,"bold"),relief=RIDGE)
        label_frame.place(x=410,y=50,width=880,height=500)

        # search by label

        search_label=Label(label_frame,text="Search By",font=("arial",10,"bold"),bg="red",fg="yellow")
        search_label.grid(row=0,column=0,sticky=W,padx=2)

        # combo box
        self.search_var=StringVar()
        search_combo=Combobox(label_frame,textvariable=self.search_var,font=("arial",10,"bold"),state="readonly")
        search_combo["value"]=("Mobile","Ref no")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,sticky=W,padx=2)

        #search entry
        self.txt_search=StringVar()
        entry_search=ttk.Entry(label_frame,textvariable=self.txt_search,font=("arial",10,"bold"),width=25)
        entry_search.grid(row=0,column=2,sticky=W,padx=2)


        #search button

        btn_search = Button(label_frame, command=self.search, text="Search", font=("arial", 10, "bold"), bg="black",fg="gold")
        btn_search.grid(row=0,column=3,sticky=W,padx=2)

        #showall button

        btn_showall=Button(label_frame,command=self.fetch_data,text="Search All",font=("arial",10,"bold"),bg="black",fg="gold")
        btn_showall.grid(row=0,column=4,sticky=W,padx=2)


        #=============== Frame =================

        tbl_frame=Frame(label_frame,bd=2,relief=RIDGE)
        tbl_frame.place(x=10,y=50,width=850,height=370)

        scroll_x=ttk.Scrollbar(tbl_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tbl_frame,orient=VERTICAL)

        self.Cust_Details_table = ttk.Treeview(tbl_frame, columns=(
        "ref", "name", "mother", "gender", "postal", "mobile", "email", "nationality", "id proof", "id number", "address"),
                                               xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_table.xview)
        scroll_y.config(command=self.Cust_Details_table.yview)

        self.Cust_Details_table.heading("ref",text="Refer no")
        self.Cust_Details_table.heading("name", text="Name")
        self.Cust_Details_table.heading("mother", text="Mother")
        self.Cust_Details_table.heading("gender", text="Gender")
        self.Cust_Details_table.heading("postal",text="Postal Code")
        self.Cust_Details_table.heading("mobile",text="Mobile")
        self.Cust_Details_table.heading("email", text="Email")
        self.Cust_Details_table.heading("nationality", text="Nationality")
        self.Cust_Details_table.heading("id proof", text="ID Proof")
        self.Cust_Details_table.heading("id number", text="ID Number")
        self.Cust_Details_table.heading("address", text="Address")


        self.Cust_Details_table["show"]="headings"

        self.Cust_Details_table.column("ref", width=100)
        self.Cust_Details_table.column("name", width=100)
        self.Cust_Details_table.column("mother", width=100)
        self.Cust_Details_table.column("gender", width=100)
        self.Cust_Details_table.column("postal", width=100)
        self.Cust_Details_table.column("mobile", width=100)
        self.Cust_Details_table.column("email", width=100)
        self.Cust_Details_table.column("nationality", width=100)
        self.Cust_Details_table.column("id proof", width=100)
        self.Cust_Details_table.column("id number",width=100)
        self.Cust_Details_table.column("address", width=100)


        self.Cust_Details_table.pack(fill=BOTH, expand=1)
        self.Cust_Details_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_cust_name.get()=="":
            messagebox.showerror("Error","Please enter name",parent=self.root)
        elif self.var_mother.get()=="":
            messagebox.showerror("Error", "Please enter mother name",parent=self.root)
        elif self.var_post.get()=="":
            messagebox.showerror("Error", "Please enter post number",parent=self.root)
        elif self.var_mobile.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        elif not self.var_mobile.get().isdigit() or len(self.var_mobile.get())!=10:
            messagebox.showerror("Error","please enter right mobile number ",parent=self.root)
        elif self.var_email.get()=="":
            messagebox.showerror("Error", "Please enter email",parent=self.root)
        elif not self.var_email.get().endswith("@gmail.com"):
            messagebox.showerror("Error", "email must end with @gmail.com",parent=self.root)
        elif self.var_id_number.get()=="":
            messagebox.showerror("Error", "Please enter id number",parent=self.root)
        elif not self.var_id_number.get().isdigit():
            messagebox.showerror("Error", "Please enter right id number",parent=self.root)
        elif self.var_address.get=="":
            messagebox.showerror("Error", "Please enter address",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                self.var_ref.get(),
                                                                                                self.var_cust_name.get(),
                                                                                                self.var_mother.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_post.get(),
                                                                                                self.var_mobile.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_nationality.get(),
                                                                                                self.var_id_proof.get(),
                                                                                                self.var_id_number.get(),
                                                                                                self.var_address.get()
                                                                                                 ) )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"some thing went wrong:{str(es)}",parent=self.root)


    def fetch_data(self):
        try:
            conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from customer")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.Cust_Details_table.delete(*self.Cust_Details_table.get_children())
                for i in rows:
                    self.Cust_Details_table.insert("",END,values=i)

                conn.commit()
            conn.close()
        except Exception as es:
            messagebox.showwarning("warning",f"somthing went wrong:{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.Cust_Details_table.focus()
        contant=self.Cust_Details_table.item(cursor_row)
        row=contant["values"]

        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_mother.set(row[2])
        self.var_gender.set(row[3])
        self.var_post.set(row[4])
        self.var_mobile.set(row[5])
        self.var_email.set(row[6])
        self.var_nationality.set(row[7])
        self.var_id_proof.set(row[8])
        self.var_id_number.set(row[9])
        self.var_address.set(row[10])



    def update(self):
        try:
            conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set name=%s,mother=%s,gender=%s,postcode=%s,mobile=%s,email=%s,nationality=%s,id proof=%s,id number=%s,id number=%s where ref=%s",(

                                                                                                                                                                                                self.var_cust_name.get(),
                                                                                                                                                                                                self.var_mother.get(),
                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                self.var_post.get(),
                                                                                                                                                                                                self.var_mobile.get(),
                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                self.var_nationality.get(),
                                                                                                                                                                                                self.var_id_proof.get(),
                                                                                                                                                                                                self.var_id_number.get(),
                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                self.var_ref.get()
                                                                                                                                                                                                ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("update","Customer details updated successfully",parent=self.root)


        except Exception as es:
            messagebox.showwarning("Warning",f"somthing went wrong {es}",parent=self.root)


    def delete(self):
        delete=messagebox.askyesno("hotel management system","do you want to delete this customer",parent=self.root)
        try:
            if delete>0:
                conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="management")
                my_cursor=conn.cursor()
                query="delete from customer where ref=%s"
                value=(self.var_ref.get(),)
                my_cursor.execute(query,value)

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("success","customer deleted successfully",parent=self.root)

        except Exception as es:
            messagebox.showwarning("warning ",f"something went wrong{es}",parent=self.root)

    def search(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="management")
            my_cursor = conn.cursor()

            column_mapping={
                "Mobile":"mobile",
                "Ref no":"ref"
            }

            column_name = column_mapping.get(self.search_var.get())

           # my_cursor.execute("SELECT * FROM customer WHERE "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
            if column_name:
               query = f"SELECT * FROM customer WHERE `{self.search_var.get()}` LIKE %s"
               value = ("%" + str(self.txt_search.get()) + "%",)

               my_cursor.execute(query, value)
               rows = my_cursor.fetchall()

               if len(rows) != 0:
                  self.Cust_Details_table.delete(*self.Cust_Details_table.get_children())
                  for i in rows:
                      self.Cust_Details_table.insert("", END, values=i)
                  conn.commit()
               else:
                  messagebox.showinfo("No Results", "No data found matching the search criteria.")
            else:
                   messagebox.showwarning("Invalid search", "Please choose a valid search option.")
            conn.close()
        except Exception as es:
            #messagebox.showwarning("warning ",f"something went wrong{es}",parent=self.root)
            print(es)


if __name__=="__main__":
    root=Tk()
    obj=Cust_win(root)
    root.mainloop()