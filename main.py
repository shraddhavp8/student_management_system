from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox,filedialog
import pymysql
import pandas
#functionality Part

def iexit():
    result=messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        root1.destroy()
    else:
        pass

def export_data():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=studentTable.get_children()
    newlist=[]
    for index in indexing:
        content=studentTable.item(index)
        datalist=content['values']
        newlist.append(datalist)


    table=pandas.DataFrame(newlist,columns=['Id','Name','Mobile','Email','Address','Gender','DOB','Added Date','Added Time'])
    table.to_csv(url,index=False)
    messagebox.showinfo('Success','Data is saved succesfully')

def update_student() :
    def update_data():
        query='update student set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
        mycursor.execute(query,(nameentry.get(),mobileentry.get(),emailentry.get(),adressentry.get(),
                                genderentry.get(),dobentry.get(),currentdate,currenttime,identry.get()))
        con.commit()
        messagebox.showinfo('Success',f'ID {identry.get()} is modified successfully',parent=updatewindow)
        updatewindow.destroy()
        show_student()
    updatewindow=Toplevel()
    updatewindow.title("Update Student")
    updatewindow.grab_set()
    updatewindow.resizable(False,False)
    idlabel=Label(updatewindow,text="ID",font=("times new roman",28,"bold"),fg="red2")
    idlabel.grid(row=0,column=0,padx=30,pady=20,sticky=W)
    identry=Entry(updatewindow,width=24,font=("times new roman",15,"bold"))
    identry.grid(row=0,column=1,padx=30,pady=20)

    namelabel=Label(updatewindow,text="Name",font=("times new roman",28,"bold"),fg="red2")
    namelabel.grid(row=1,column=0,padx=30,pady=20,sticky=W)
    nameentry=Entry(updatewindow,width=24,font=("times new roman",15,"bold"))
    nameentry.grid(row=1,column=1,padx=30,pady=20)
    
    mobilelabel=Label(updatewindow,text="Mobile",font=("times new roman",28,"bold"),fg="red2")
    mobilelabel.grid(row=2,column=0,padx=30,pady=20,sticky=W)
    mobileentry=Entry(updatewindow,width=24,font=("times new roman",15,"bold"))
    mobileentry.grid(row=2,column=1,padx=30,pady=20)
    
    adresslabel=Label(updatewindow,text="Address",font=("times new roman",28,"bold"),fg="red2")
    adresslabel.grid(row=3,column=0,padx=30,pady=20,sticky=W)
    adressentry=Entry(updatewindow,width=24,font=("times new roman",15,"bold"))
    adressentry.grid(row=3,column=1,padx=30,pady=20)

    emaillabel=Label(updatewindow,text="Email",font=("times new roman",28,"bold"),fg="red2")
    emaillabel.grid(row=4,column=0,padx=30,pady=20,sticky=W)
    emailentry=Entry(updatewindow,width=24,font=("times new roman",15,"bold"))
    emailentry.grid(row=4,column=1,padx=30,pady=20)

    genderlabel=Label(updatewindow,text="Gender",font=("times new roman",28,"bold"),fg="red2")
    genderlabel.grid(row=5,column=0,padx=30,pady=20,sticky=W)
    genderentry=Entry(updatewindow,width=24,font=("times new roman",15,"bold"))
    genderentry.grid(row=5,column=1,padx=30,pady=20)

    doblabel=Label(updatewindow,text="DOB",font=("times new roman",28,"bold"),fg="red2")
    doblabel.grid(row=6,column=0,padx=30,pady=20,sticky=W)
    dobentry=Entry(updatewindow,width=24,font=("times new roman",15,"bold"))
    dobentry.grid(row=6,column=1,padx=30,pady=20)

    updatestudentB=ttk.Button(updatewindow,text="Update",command=update_data)
    updatestudentB.grid(row=7,columnspan=2,pady=15)
    
    indexing = studentTable.focus()
    content = studentTable.item(indexing)
    listdata = content['values']
    identry.insert(0, listdata[0])
    nameentry.insert(0, listdata[1])
    mobileentry.insert(0, listdata[2])
    emailentry.insert(0, listdata[3])
    adressentry.insert(0, listdata[4])
    genderentry.insert(0, listdata[5])
    dobentry.insert(0, listdata[6])
    
def show_student():
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('', END, values=data)

def delete_student():
    indexing=studentTable.focus()
    print(indexing)
    content=studentTable.item(indexing)
    content_id=content['values'][0]
    query='delete from student where id=%s'
    mycursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo('Deleted',f'Id {content_id} is deleted succesfully')
    query='select * from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)

def searchstudent() :
    def search_data():
        query='select * from student where id=%s or name=%s or email=%s or mobile=%s or address=%s or gender=%s or dob=%s'
        mycursor.execute(query,(identry.get(),nameentry.get(),mobileentry.get(),adressentry.get(),emailentry.get(),genderentry.get(),dobentry.get()))
        studentTable.delete(*studentTable.get_children())
        fetched_data=mycursor.fetchall()
        for data in fetched_data:
            studentTable.insert('',END,values=data)
    searchwindow=Toplevel()
    searchwindow.title("Search Student")
    searchwindow.grab_set()
    searchwindow.resizable(False,False)
    idlabel=Label(searchwindow,text="ID",font=("times new roman",28,"bold"),fg="red2")
    idlabel.grid(row=0,column=0,padx=30,pady=20,sticky=W)
    identry=Entry(searchwindow,width=24,font=("times new roman",15,"bold"))
    identry.grid(row=0,column=1,padx=30,pady=20)

    namelabel=Label(searchwindow,text="Name",font=("times new roman",28,"bold"),fg="red2")
    namelabel.grid(row=1,column=0,padx=30,pady=20,sticky=W)
    nameentry=Entry(searchwindow,width=24,font=("times new roman",15,"bold"))
    nameentry.grid(row=1,column=1,padx=30,pady=20)
    
    mobilelabel=Label(searchwindow,text="Mobile",font=("times new roman",28,"bold"),fg="red2")
    mobilelabel.grid(row=2,column=0,padx=30,pady=20,sticky=W)
    mobileentry=Entry(searchwindow,width=24,font=("times new roman",15,"bold"))
    mobileentry.grid(row=2,column=1,padx=30,pady=20)
    
    adresslabel=Label(searchwindow,text="Address",font=("times new roman",28,"bold"),fg="red2")
    adresslabel.grid(row=3,column=0,padx=30,pady=20,sticky=W)
    adressentry=Entry(searchwindow,width=24,font=("times new roman",15,"bold"))
    adressentry.grid(row=3,column=1,padx=30,pady=20)

    emaillabel=Label(searchwindow,text="Email",font=("times new roman",28,"bold"),fg="red2")
    emaillabel.grid(row=4,column=0,padx=30,pady=20,sticky=W)
    emailentry=Entry(searchwindow,width=24,font=("times new roman",15,"bold"))
    emailentry.grid(row=4,column=1,padx=30,pady=20)

    genderlabel=Label(searchwindow,text="Gender",font=("times new roman",28,"bold"),fg="red2")
    genderlabel.grid(row=5,column=0,padx=30,pady=20,sticky=W)
    genderentry=Entry(searchwindow,width=24,font=("times new roman",15,"bold"))
    genderentry.grid(row=5,column=1,padx=30,pady=20)

    doblabel=Label(searchwindow,text="DOB",font=("times new roman",28,"bold"),fg="red2")
    doblabel.grid(row=6,column=0,padx=30,pady=20,sticky=W)
    dobentry=Entry(searchwindow,width=24,font=("times new roman",15,"bold"))
    dobentry.grid(row=6,column=1,padx=30,pady=20)

    searchstudentB=ttk.Button(searchwindow,text="Search",command=search_data)
    searchstudentB.grid(row=7,columnspan=2,pady=15)

def addstudent() :
    def adddata() :
        if identry.get()=="" or nameentry.get()=="" or mobileentry.get()=="" or genderentry.get()=="" or adressentry.get()=="" or emailentry.get()=="" or dobentry.get()=="" :
            messagebox.showerror("Error","All fields are required",parent=addwindow)
        else :
            query="insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            mycursor.execute(query,(identry.get(),nameentry.get(),mobileentry.get(),adressentry.get(),emailentry.get(),genderentry.get(),dobentry.get(),currentdate,currenttime))
            con.commit()
            result=messagebox.askyesno("Confirm","Data added sucessfully. Do you want to clean the form?",parent=addwindow)
            if result :
                identry.delete(0,END)
                nameentry.delete(0,END)
                mobileentry.delete(0,END)
                adressentry.delete(0,END)
                emailentry.delete(0,END)
                genderentry.delete(0,END)
                dobentry.delete(0,END)
            else :
                pass
    
            query="select *from student"    
            mycursor.execute(query)
            fetchdata=mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for data in fetchdata :
                studentTable.insert("",END,values=data)

    addwindow=Toplevel()
    addwindow.title("Add Student")
    addwindow.grab_set()
    addwindow.resizable(False,False)
    idlabel=Label(addwindow,text="ID",font=("times new roman",28,"bold"),fg="red2")
    idlabel.grid(row=0,column=0,padx=30,pady=20,sticky=W)
    identry=Entry(addwindow,width=24,font=("times new roman",15,"bold"))
    identry.grid(row=0,column=1,padx=30,pady=20)

    namelabel=Label(addwindow,text="Name",font=("times new roman",28,"bold"),fg="red2")
    namelabel.grid(row=1,column=0,padx=30,pady=20,sticky=W)
    nameentry=Entry(addwindow,width=24,font=("times new roman",15,"bold"))
    nameentry.grid(row=1,column=1,padx=30,pady=20)
    
    mobilelabel=Label(addwindow,text="Mobile",font=("times new roman",28,"bold"),fg="red2")
    mobilelabel.grid(row=2,column=0,padx=30,pady=20,sticky=W)
    mobileentry=Entry(addwindow,width=24,font=("times new roman",15,"bold"))
    mobileentry.grid(row=2,column=1,padx=30,pady=20)
    
    adresslabel=Label(addwindow,text="Address",font=("times new roman",28,"bold"),fg="red2")
    adresslabel.grid(row=3,column=0,padx=30,pady=20,sticky=W)
    adressentry=Entry(addwindow,width=24,font=("times new roman",15,"bold"))
    adressentry.grid(row=3,column=1,padx=30,pady=20)

    emaillabel=Label(addwindow,text="Email",font=("times new roman",28,"bold"),fg="red2")
    emaillabel.grid(row=4,column=0,padx=30,pady=20,sticky=W)
    emailentry=Entry(addwindow,width=24,font=("times new roman",15,"bold"))
    emailentry.grid(row=4,column=1,padx=30,pady=20)

    genderlabel=Label(addwindow,text="Gender",font=("times new roman",28,"bold"),fg="red2")
    genderlabel.grid(row=5,column=0,padx=30,pady=20,sticky=W)
    genderentry=Entry(addwindow,width=24,font=("times new roman",15,"bold"))
    genderentry.grid(row=5,column=1,padx=30,pady=20)

    doblabel=Label(addwindow,text="DOB",font=("times new roman",28,"bold"),fg="red2")
    doblabel.grid(row=6,column=0,padx=30,pady=20,sticky=W)
    dobentry=Entry(addwindow,width=24,font=("times new roman",15,"bold"))
    dobentry.grid(row=6,column=1,padx=30,pady=20)

    addstudentB=ttk.Button(addwindow,text="Submit",command=adddata)
    addstudentB.grid(row=7,columnspan=2,pady=15)

def clock() :
    global currentdate,currenttime
    currentdate=time.strftime("%d/%m/%Y")
    currenttime=time.strftime("%H:%M")
    dateTimeLabel.config(text=f'        Date:{currentdate}\nTime:{currenttime}')
    dateTimeLabel.after(6000,clock)

count=0
text1=" "
def slider() :
    global count,text1
    if count==len(s) :
        count=0
        text1=" "
    text1=text1+s[count]
    sliderLabel.config(text=text1)
    count+=1
    sliderLabel.after(300,slider)   
    
def connectDatabase() :
    def connect() :
        global mycursor,con
        try:
            con=pymysql.connect(host=hostEntry.get(),user=userEntry.get(),password=passwordEntry.get())
            mycursor=con.cursor()
           
        except :
            messagebox.showerror("Error","Invalid details",parent=connectWindow)
            return         
        try :
            query="create database studentmanagementsystem"
            mycursor.execute(query)
            query="use studentmanagementsystem"
            mycursor.execute(query)
            query="create table student(id int not null primary key, name varchar(30), mobile varchar(10), email varchar(30), address varchar(100), gender varchar(20), dob varchar(20), date varchar(50), time varchar(50))"
            mycursor.execute(query)
        except :
            query="use studentmanagementsystem"
            mycursor.execute(query)
        messagebox.showinfo("Success", "Database connection is successful",parent=connectWindow)    
        connectWindow.destroy()
        addStudent.config(state=NORMAL)
        searchStudent.config(state=NORMAL)
        updateStudent.config(state=NORMAL)
        showStudent.config(state=NORMAL)
        deleteStudent.config(state=NORMAL)
        exportStudent.config(state=NORMAL)

    connectWindow=Toplevel()
    connectWindow.geometry("470x265+730+230") 
    connectWindow.title("Database Connection")
    connectWindow.grab_set()
    connectWindow.resizable(0,0)
    
    hostName=Label(connectWindow,text="Host name",font=("times new roman ",18,"bold"),fg="red2")
    hostName.grid(row=0,column=0,padx=20,pady=20)
    hostEntry=Entry(connectWindow,font=("times new roman",18,"bold"),bd=2)
    hostEntry.grid(row=0,column=1,padx=20,pady=10)

    userName=Label(connectWindow,text="User name",font=("times new roman ",18,"bold"),fg="red2")
    userName.grid(row=1,column=0,padx=20,pady=20)
    userEntry=Entry(connectWindow,font=("times new roman",18,"bold"),bd=2)
    userEntry.grid(row=1,column=1,padx=20,pady=10)
    
    password=Label(connectWindow,text="Password",font=("times new roman ",18,"bold"),fg="red2")
    password.grid(row=2,column=0,padx=20,pady=20)
    passwordEntry=Entry(connectWindow,font=("times new roman",18,"bold"),bd=2)
    passwordEntry.grid(row=2,column=1,padx=20,pady=10)
    
    connectButton=ttk.Button(connectWindow,text="CONNECT",command=connect)
    connectButton.grid(row=3,columnspan=2)


root1=ttkthemes.ThemedTk()
root1.get_themes()
root1.set_theme("radiance")
root1.geometry("1274x780+0+0")
root1.resizable(False,False)
root1.title("Student Management System")


dateTimeLabel=Label(root1,font=("times new roman",18,"bold"),fg="red2")
dateTimeLabel.place(x=5,y=5)
clock()

s="STUDENT MANAGEMENT SYSTEM"
sliderLabel=Label(root1,text=s,font=("times new roman",28,"italic bold"),width=30,fg="red2")
sliderLabel.place(x=300,y=10)
slider()

connectButton=ttk.Button(root1,text="Connect to Database",command=connectDatabase)
connectButton.place(x=1050,y=10)

leftFrame=Frame(root1)
leftFrame.place(x=50,y=80,width=300,height=600)

studentImage=PhotoImage(file="university.png")
studentLabel=Label(leftFrame,image=studentImage,justify="center")
studentLabel.grid(row=0,column=1,pady=10)

addStudent=ttk.Button(leftFrame,text="Add student",width=25,state=DISABLED,command=addstudent)
addStudent.grid(row=1,column=1,pady=20)
searchStudent=ttk.Button(leftFrame,text="Search student",width=25,state=DISABLED,command=searchstudent)
searchStudent.grid(row=2,column=1,pady=20)
updateStudent=ttk.Button(leftFrame,text="Update student",width=25,state=DISABLED,command=update_student)
updateStudent.grid(row=3,column=1,pady=20)
deleteStudent=ttk.Button(leftFrame,text="Delete student",width=25,state=DISABLED,command=delete_student)
deleteStudent.grid(row=4,column=1,pady=20)
showStudent=ttk.Button(leftFrame,text="Show student",width=25,state=DISABLED,command=show_student)
showStudent.grid(row=5,column=1,pady=20)
exportStudent=ttk.Button(leftFrame,text="Export data",width=25,state=DISABLED,command=export_data)
exportStudent.grid(row=6,column=1,pady=20)
exitStudent=ttk.Button(leftFrame,text="Exit",width=25,command=iexit)
exitStudent.grid(row=7,column=1,pady=20)

rightFrame=Frame(root1)
rightFrame.place(x=350,y=90,width=875,height=650)

scrollbarX=Scrollbar(rightFrame,orient=HORIZONTAL)

studentTable=ttk.Treeview(rightFrame,columns=("ID","Name","Mobile Number","Email","Address","Gender",
                                              "D.O.B","Added date","Added time"),xscrollcommand=scrollbarX.set)
studentTable.pack(fill=BOTH,expand=1)

scrollbarX.config(command=studentTable.xview)
scrollbarX.pack(side=BOTTOM,fill=X)

studentTable.heading("ID",text="ID")
studentTable.heading("Name",text="Name")
studentTable.heading("Mobile Number",text="Mobile Number")
studentTable.heading("Email",text="Email")
studentTable.heading("Address",text="Address")
studentTable.heading("Gender",text="Gender")
studentTable.heading("D.O.B",text="D.O.B")
studentTable.heading("Added date",text="Added date")
studentTable.heading("Added time",text="Added time")
studentTable.config(show="headings")

studentTable.column("ID",width=50,anchor=CENTER)
studentTable.column("Name",width=200,anchor=CENTER)
studentTable.column("Mobile Number",width=300,anchor=CENTER)
studentTable.column("Email",width=250,anchor=CENTER)
studentTable.column("Address",width=200,anchor=CENTER)
studentTable.column("Gender",width=200,anchor=CENTER)
studentTable.column("D.O.B",width=200,anchor=CENTER)
studentTable.column("Added date",width=200,anchor=CENTER)
studentTable.column("Added time",width=200,anchor=CENTER)

style=ttk.Style()
style.configure("Treeview",rowheight=40,font=("times new roman",14,"bold"),foreground="red2")
style.configure("Treeview.Heading",font=("times new roman",16,"bold"),foreground="red2")








root1.mainloop()
