from tkinter import *
from tkinter import ttk,messagebox
import time
import os
class File_App:
    def __init__(self):
        self.root=Tk()
        self.root.title("FILE BASED RECORD SYSTEM")
        self.root.geometry("1560x850+0+0")
        bg_color="#074463"


        title=Label(self.root,text="FILE BASED RECORD SYSTEM" ,bd=10,fg="white",relief=SUNKEN,bg=bg_color,pady=10,font=("times new roman",35,"bold")).pack(fill=X)
        Student_Frame=Frame(self.root,bd=10,relief=SUNKEN,bg=bg_color)
        Student_Frame.place(x=20,y=100,width=1600,height=530)

        stitle=Label(Student_Frame,text="STUDENT DETAILS",bg=bg_color,fg="white",font=("times new roman",27,"bold")).grid(row=0,columnspan=5,pady=20)

        #====All Variables===============

        self.s_id=StringVar()
        self.name=StringVar()
        self.course=StringVar()
        self.address=StringVar()
        self.city=StringVar()
        self.contact=StringVar()
        self.date=StringVar()
        self.degree=StringVar()
        self.proof=StringVar()
        self.payment=StringVar()


        lblsid=Label(Student_Frame,text="Student ID",bg=bg_color,fg="white",font=("times new roman",25,"bold")).grid(row=2,column=1,pady=10,padx=20,sticky="w")
        txtsid=Entry(Student_Frame,bd=7,relief=SUNKEN,textvariable=self.s_id,width=25,font="arial 15 bold").grid(row=2,column=2,padx=10,pady=10)


        lblname=Label(Student_Frame,text="Name",bg=bg_color,fg="white",font=("times new roman",25,"bold")).grid(row=3,column=1,pady=10,padx=20,sticky="w")
        txtname=Entry(Student_Frame,bd=7,relief=SUNKEN,textvariable=self.name,width=25,font="arial 15 bold").grid(row=3,column=2,padx=10,pady=10)

        lblcontact=Label(Student_Frame,text="Contact No.",bg=bg_color,fg="white",font=("times new roman",25,"bold")).grid(row=2,column=3,pady=10,padx=20,sticky="w")
        txtcontact=Entry(Student_Frame,bd=7,relief=SUNKEN,textvariable=self.contact,width=25,font="arial 15 bold").grid(row=2,column=4,padx=10,pady=10)


        lblname=Label(Student_Frame,text="Name",bg=bg_color,fg="white",font=("times new roman",25,"bold")).grid(row=3,column=1,pady=10,padx=20,sticky="w")
        txtname=Entry(Student_Frame,bd=7,relief=SUNKEN,textvariable=self.name,width=25,font="arial 15 bold").grid(row=3,column=2,padx=10,pady=10)

        
        lbldate=Label(Student_Frame,text="Date(dd/mm/yyyy)",bg=bg_color,fg="white",font=("times new roman",25,"bold")).grid(row=3,column=3,pady=10,padx=20,sticky="w")
        txtdate=Entry(Student_Frame,bd=7,relief=SUNKEN,textvariable=self.date,width=25,font="arial 15 bold").grid(row=3,column=4,padx=10,pady=10)


        lblcourse=Label(Student_Frame,text="Course",bg=bg_color,fg="white",font=("times new roman",25,"bold")).grid(row=4,column=1,pady=10,padx=20,sticky="w")
        txtcourse=Entry(Student_Frame,bd=7,relief=SUNKEN,textvariable=self.course,width=25,font="arial 15 bold").grid(row=4,column=2,padx=10,pady=10)


        lbladdress=Label(Student_Frame,text="Address",bg=bg_color,fg="white",font=("times new roman",25,"bold")).grid(row=5,column=1,pady=10,padx=20,sticky="w")
        txtaddress=Entry(Student_Frame,bd=7,relief=SUNKEN,textvariable=self.address,width=25,font="arial 15 bold").grid(row=5,column=2,padx=10,pady=10)


        lblcity=Label(Student_Frame,text="City",bg=bg_color,fg="white",font=("times new roman",25,"bold")).grid(row=6,column=1,pady=10,padx=20,sticky="w")
        txtcity=Entry(Student_Frame,bd=7,relief=SUNKEN,textvariable=self.city,width=25,font="arial 15 bold").grid(row=6,column=2,padx=10,pady=10)


        lbldegree=Label(Student_Frame,text="Select degree",bg=bg_color,fg="white",font=("times new roman",25,"bold")).grid(row=4,column=3,pady=10,padx=20,sticky="w")
        lblproof=Label(Student_Frame,text="ID Proof",bg=bg_color,fg="white",font=("times new roman",25,"bold")).grid(row=5,column=3,pady=10,padx=20,sticky="w")
        lbldegree=Label(Student_Frame,text="Payment Mode",bg=bg_color,fg="white",font=("times new roman",25,"bold")).grid(row=6,column=3,pady=10,padx=20,sticky="w")
        

        degreecombo=ttk.Combobox(Student_Frame,width=20,textvariable=self.degree,state="readonly",font="arial 15 bold")
        degreecombo['values']=("BCA","MCA","Btech","MBA","Mtech")
        degreecombo.grid(row=4,column=4,padx=10,pady=10)

        idcombo=ttk.Combobox(Student_Frame,width=20,textvariable=self.proof,state="readonly",font="arial 15 bold")
        idcombo['values']=("PAN Card","Driving Licence","Student ID Card")
        idcombo.grid(row=5,column=4,padx=10,pady=10)


        paymentcombo=ttk.Combobox(Student_Frame,width=20,textvariable=self.payment,state="readonly",font="arial 15 bold")
        paymentcombo['values']=("Cash","NEFT","Internet Banking","Credit Card")
        paymentcombo.grid(row=6,column=4,padx=10,pady=10)


        btnFrame=Frame(self.root,bd=10,relief=SUNKEN,bg=bg_color)
        btnFrame.place(x=20,y=650,width=1500)


        btnsave=Button(btnFrame,text="Save",font="arial 15 bold",bd=20,width=18,command=self.save_data).grid(row=0,column=2,padx=18,pady=16)
        btndelete=Button(btnFrame,text="Delete",font="arial 15 bold",bd=20,width=18,command=self.delete).grid(row=0,column=3,padx=18,pady=16)
        btnclear=Button(btnFrame,text="Clear",command=self.clear,font="arial 15 bold",bd=20,width=18).grid(row=0,column=4,padx=18,pady=16)
        btnlog=Button(btnFrame,text="Logout",font="arial 15 bold",bd=20,width=18,command=self.logout).grid(row=0,column=5,padx=18,pady=16)
        btnexit=Button(btnFrame,text="Exit",font="arial 15 bold",bd=20,width=18,command=self.exit_fun).grid(row=0,column=6,padx=18,pady=16)


        File_Frame=Frame(self.root,bd=10,relief=SUNKEN)
        File_Frame.place(x=1200,y=100,width=315,height=530)

        ftitle=Label(File_Frame,text="All Files",bg=bg_color,fg="white",font="arial 20 bold",bd=5,relief=SUNKEN).pack(side=TOP,fill=X)

        scroll_y=Scrollbar(File_Frame,orient=VERTICAL)
        self.file_list=Listbox(File_Frame,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.file_list.yview)
        self.file_list.pack(fill=BOTH,expand=1)
        self.file_list.bind("<ButtonRelease-1>",self.get_data)
        self.show_files()
        self.root.mainloop()

    def save_data(self):
        present="no"
        if self.s_id.get()=="":
            messagebox.showerror("Error","Student ID must be required!!")
        else:
            f=os.listdir("files/")
            if len(f)>0:
                for i in f:
                    if i.split(".")[0] == self.s_id.get():
                        present="Yes"
                if present=="Yes":
                    ask=messagebox.askyesno("Update","File already present \nDo you want to update it?")
                    if ask>0:
                        self.save_file()
                        messagebox.showinfo("Update","Record has updated successfully")
                        self.show_files()

                else:
                    self.save_file()
                    messagebox.showinfo("Saved","Record has saved successfully")
                    self.show_files()
                        
            else:
                self.save_file()
                messagebox.showinfo("Saved","Record has saved successfully")
                self.show_files()
            
    def save_file(self):
        f=open("files/"+str(self.s_id.get())+".txt","w")
        f.write(
                str(self.s_id.get())+","+
                str(self.name.get())+","+
                str(self.course.get())+","+
                str(self.address.get())+","+
                str(self.city.get())+","+
                str(self.contact.get())+","+
                str(self.date.get())+","+
                str(self.degree.get())+","+
                str(self.proof.get())+","+
                str(self.payment.get())
                )
        f.close()


    def show_files(self):
        files=os.listdir("files/")
        self.file_list.delete(0,END)
        if len(files)>0:
            for i in files:
                self.file_list.insert(END,i)
                
        
    def get_data(self,ev):
        get_cursor=self.file_list.curselection()
        # print(self.file_list.get(get_cursor))
        f1=open("files/"+self.file_list.get(get_cursor))
        value=[]
        for f in f1:
            value=f.split(",")
        self.s_id.set(value[0])
        self.name.set(value[1])
        self.course.set(value[2])
        self.address.set(value[3])
        self.city.set(value[4])
        self.contact.set(value[5])
        self.date.set(value[6])
        self.degree.set(value[7])
        self.proof.set(value[8])
        self.payment.set(value[9])
    def clear(self):
        self.s_id.set("")
        self.name.set("")
        self.course.set("")
        self.address.set("")
        self.city.set("")
        self.contact.set("")
        self.date.set("")
        self.degree.set("")
        self.proof.set("")
        self.payment.set("")
    def delete(self):
        present="no"
        if self.s_id.get()=="":
            messagebox.showerror("Error","Student ID must be required!!")
        else:
            f=os.listdir("files/")
            if len(f)>0:
                for i in f:
                    if i.split(".")[0]==self.s_id.get():
                        present="Yes"
                if present=="Yes":
                    ask=messagebox.askyesno("Delete","Do you really want to delete?")
                    if ask>0:
                        os.remove("files/"+self.s_id.get()+".txt")
                        messagebox.showinfo("Success","Deleted Successfully")
                        self.show_files()
                else:
                    messagebox.showerror("Error","File not found")

    def exit_fun(self):
        ask=messagebox.askyesno("Exit","Do you really want to Exit?")
        if ask>0:
            self.root.destroy()
    
    def logout(self):
        self.root.destroy()
        import login

    


        

            

                
    


   


        



        

    