from tkinter import *
from tkinter import messagebox
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("FILE BASED RECORD SYSTEM")
        self.root.geometry("1560x800+0+0")
        bg_color="#074463"

        F1=Frame(self.root,bd=10,relief=SUNKEN, bg=bg_color)
        F1.place(x=530,y=200,height=350)

        self.username=StringVar()
        self.password=StringVar()


        title=Label(F1,text="LOGIN SYSTEM",bg=bg_color,fg="white",font=("times new roman",30,"bold")).grid(row=0,columnspan=2,pady=20)


        lblusername=Label(F1,text="Username",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=1,column=0,pady=10,padx=10)


        txtusername=Entry(F1,bd=7,relief=SUNKEN,textvariable=self.username,width=25,font="arial 15 bold").grid(row=1,column=1,padx=10,pady=10)


        lblpass=Label(F1,text="Password",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=2,column=0,pady=10,padx=10)


        txtpass=Entry(F1,bd=7,relief=SUNKEN,show="*",textvariable=self.password,width=25,font="arial 15 bold").grid(row=2,column=1,padx=10,pady=10)


        btnlog=Button(F1,text="Login",font="arial 15 bold",bd=7,width=8,command=self.logfun).place(x=10,y=250)
        btnreset=Button(F1,text="Reset",font="arial 15 bold",bd=7,width=8,command=self.reset).place(x=155,y=250)
        btnexit=Button(F1,text="Exit",font="arial 15 bold",bd=7,width=8,command=self.exit_fun).place(x=300,y=250)

    def logfun(self):
        if self.username.get()=="Neeraja Rajan" and self.password.get()=="123456":
            self.root.destroy()
            import software
            software.File_App()
        else:
            messagebox.showerror("Error","Invalid Username or Password")
            
    def reset(self):
        self.username.set("")
        self.password.set("")

    def exit_fun(self):
        option=messagebox.askyesno("Exit","Do you really want to exit?")
        if option>0:
            self.root.destroy()
        else:
            return
root=Tk()
ob=Login(root)
root.mainloop()

