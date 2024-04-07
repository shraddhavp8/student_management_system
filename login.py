from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

def login() :
    if userEntry.get() == " " or passEntry.get() == " " :
        messagebox.showerror("Error","Fields cannot be left empty")
    elif userEntry.get()== "Krishna" and passEntry.get()=="1234" :
        messagebox.showinfo("Success","Welcome")
        root.destroy()
        import sms
    else :
        messagebox.showerror("Error","Incorrect Credentials")
        
       
root=Tk()
root.geometry("1288x760+0+0")
root.resizable(False,False)
root.title("Login Page")

bgImage=PhotoImage(file="bg.png")
bgLabel=Label(root,image=bgImage)
bgLabel.place(x=0,y=0)

logoFrame=Frame(root,bg="White")
logoFrame.place(x=400,y=250)
logoImage=PhotoImage(file="logo.png")
logoLabel=Label(logoFrame,image=logoImage,justify='center')
logoLabel.grid(row=0,column=0,columnspan=2,pady=10)

userImage=PhotoImage(file="students-cap.png")
passImage=PhotoImage(file="padlock.png")

userName=Label(logoFrame,image=userImage,text="Username",compound=LEFT,font=('times new roman',20,'bold'),bg="White")
userName.grid(row=1,column=0)
userEntry=Entry(logoFrame,width=20,borderwidth=2,font=('times new roman',20,'bold'))
userEntry.grid(row=1,column=1,pady=10,padx=20)

password=Label(logoFrame,image=passImage,text="Password",compound=LEFT,font=('times new roman',20,'bold'),bg="White")
password.grid(row=2,column=0)
passEntry=Entry(logoFrame,borderwidth=2,font=('times new roman',20,'bold'))
passEntry.grid(row=2,column=1,pady=10,padx=20)

loginButton=Button(logoFrame,text="Login",font=("times new roman",14,"bold"),width=10,cursor="hand2",bg="royalblue",fg="white",command=login)
loginButton.grid(row=3,column=1,pady=10)

root.mainloop()