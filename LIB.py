from tkinter import*
from tkinter import messagebox
from datetime import datetime
import mysql.connector

#window
windows=Tk()
windows.title("lib management")
windows.geometry('1000x700')
windows.configure(bg='bisque1')
windows.maxsize(1000,700)

#date_time
now=datetime.now()
dt_string=now.strftime("%d/%m/%y %H:%M:%S")
datetime_lbl=Label(windows,text=dt_string)
datetime_lbl.place(x=850,y=20)

#slq
mydb=mysql.connector.connect(
    host="localhost",
    user="himanshu",
    passwd="12345",
    database="LIBRARY"
    )

mycursor = mydb.cursor()


    
#load_photos
bk_pht=PhotoImage(file=r'D:\\lib_man\\icon-books.png')


lbl_img=Label(image=bk_pht)
lbl_img.place(x=10,y=10)
lbl_txt=Label(text="LIBRARY",font=("BOLD",80),fg="blue")
lbl_txt.place(x=400,y=70)

#admin_login
def login():
    login_win=Tk()
    login_win.title("ENTER PASSWORD")
    login_win.geometry('300x100')

    
    lbl_userid=Label(login_win,text='USER ID',font=("",10))
    lbl_userid.place(x=0,y=0)
    lbl_password=Label(login_win,text='PASSWORD',font=("",10))
    lbl_password.place(x=0,y=30)

    userid=Entry(login_win,font=("",10))
    userid.place(x=100,y=0)
    password=Entry(login_win,font=("",10))
    password.place(x=100,y=30)

    def etr():
        uid=userid.get()
        pas=password.get()
        if uid=="himanshu"and pas=="chaudhary":
            messagebox.showinfo("STATUS","LOGGED IN")
            login_win.destroy()
            loggedin()
        else:
            messagebox.showinfo("STATUS","INCORRECT PASSWORD")

    submit=Button(login_win,text="LOGIN",command=etr)
    submit.place(x=200,y=60)

    
login=Button(windows,text="ADMIN_LOGIN",command=login)
login.place(x=825,y=200)

#admin_commands
def add_book():
    addbook_win=Tk()
    addbook_win.title("ADDBOOK")
    addbook_win.geometry('400x400')

    lbl_sino=Label(addbook_win,text="SI.NO.",font=("",10))
    lbl_sino.place(x=0,y=0)
    lbl_class=Label(addbook_win,text="CLASS",font=("",10))
    lbl_class.place(x=0,y=30)
    lbl_subject=Label(addbook_win,text="SUBJECT",font=("",10))
    lbl_subject.place(x=0,y=60)
    lbl_author=Label(addbook_win,text="AUTHOR",font=("",10))
    lbl_author.place(x=0,y=90)


    sino=Entry(addbook_win,font=("",10))
    sino.place(x=100,y=0)
    clas=Entry(addbook_win,font=("",10))
    clas.place(x=100,y=30)
    subject=Entry(addbook_win,font=("",10))
    subject.place(x=100,y=60)
    author=Entry(addbook_win,font=("",10))
    author.place(x=100,y=90)
    
    def addbook():
        sn=sino.get()
        cs=clas.get()
        sub=subject.get()
        aut=author.get()
        val=[]
        val.append(sn)
        val.append(cs)
        val.append(sub)
        val.append(aut)
        val.append("N")
        val.append(0)
        print(type(sn))
        print(val)
        sql = "INSERT INTO books (sino, class, subject, author,status,issuedto ) VALUES (%s,%s,%s,%s,%s,%s)"
        mycursor.execute(sql,val)
        mydb.commit()
        mycursor.close()
        mydb.close()
        messagebox.showinfo("ADD BOOK","new book succesfully added")
        addbook_win.destroy()
        
    ADD=Button(addbook_win,text="ADD",command=addbook)
    ADD.place(x=200,y=120)

def show_books():
    showbook_win=Tk()
    showbook_win.title("SHOW BOOKS")
    showbook_win.geometry('500x500')
    
    with open(r'D:\\lib_man\\BOOK.txt')as file:
        data=file.read()
    showbook_lbl=Label(showbook_win,text=data,font=("",10))
    showbook_lbl.place(x=0,y=20)

def add_student():
    addstudent_win=Tk()
    addstudent_win.title("ADD STUDENT")
    addstudent_win.geometry('500x500')

    lbl_rollno=Label(addstudent_win,text="lib. ROLL.NO.",font=("",10))
    lbl_rollno.place(x=0,y=0)
    lbl_class=Label(addstudent_win,text="CLASS",font=("",10))
    lbl_class.place(x=0,y=60)
    lbl_name=Label(addstudent_win,text="NAME",font=("",10))
    lbl_name.place(x=0,y=30)

    rollno=Entry(addstudent_win,font=("",10))
    rollno.place(x=100,y=0)
    clas=Entry(addstudent_win,font=("",10))
    clas.place(x=100,y=60)
    name=Entry(addstudent_win,font=("",10))
    name.place(x=100,y=30)
    
    def addstudent():
        rno=rollno.get()
        cls=clas.get()
        nm=name.get()
        val=[]
        val.append(rno)
        val.append(cls)
        val.append(nm)
        
        sql = "INSERT INTO students (lib_rollno, class, name) VALUES (%s,%s,%s)"
        mycursor.execute(sql,val)
        mydb.commit()
        mycursor.close()
        mydb.close()
                                                                                                                    
        messagebox.showinfo("ADD STUDENT","new student "+nm+" succesfully added")                                           
        addstudent_win.destroy()
    
    ADD=Button(addstudent_win,text="ADD",command=addstudent)
    ADD.place(x=200,y=90)
    
def show_students():
    showstudents_win=Tk()
    showstudents_win.title("SHOW STUDENTS")
    showstudents_win.geometry('500x500')
    
    mycursor.execute("SELECT * FROM students")
    mydata=mycursor.fetchall()
    
    showbook_lbl=Label(showstudents_win,text=mydata,font=("",10))
    showbook_lbl.place(x=0,y=20)

def issue():
    lblissue=Label(windows,text="ISSUE BOOK",font=("",20))
    lblissue.place(x=120,y=300)
    stud_lbl=Label(windows,text="STUDENT ROLLNO.",font=("",10))
    stud_lbl.place(x=50,y=375)
    bksino_lbl=Label(windows,text="BOOK SINO.",font=("",10))
    bksino_lbl.place(x=50,y=400)
    studno=Entry(windows,font=("",10))
    studno.place(x=200,y=375)
    bookno=Entry(windows,font=("",10))
    bookno.place(x=200,y=400)

    def issuee():
        bk=bookno.get()
        std=studno.get()
        val=["I",bk]
        sql = "UPDATE books SET status = %s WHERE sino = %s"
        
        mycursor.execute(sql, val)

        val=[std,bk]
        sql = "UPDATE books SET issuedto = %s WHERE sino = %s"
        
        mycursor.execute(sql, val)
        
        mydb.commit()

        messagebox.showinfo("BOOK ISSUED","BOOK NO."+bk+" issued to student no."+std)
        
        
    issue=Button(windows,text="ISSUE",font=("",10),command=issuee)
    issue.place(x=200,y=430)


def retrieve():
    lblretrieve=Label(windows,text="RETRIEVE BOOK",font=("",20))
    lblretrieve.place(x=500,y=300)
    rstud_lbl=Label(windows,text="STUDENT ROLLNO.",font=("",10))
    rstud_lbl.place(x=430,y=375)
    rbksino_lbl=Label(windows,text="BOOK SINO.",font=("",10))
    rbksino_lbl.place(x=430,y=400)
    rstudname=Entry(windows,font=("",10))
    rstudname.place(x=580,y=375)
    rbookno=Entry(windows,font=("",10))
    rbookno.place(x=580,y=400)

    def retrievee():
        bk=rbookno.get()
        std=rstudname.get()
        val=["N",bk]
        sql = "UPDATE books SET status = %s WHERE sino = %s"
        
        mycursor.execute(sql, val)

        val=[0,bk]
        sql = "UPDATE books SET issuedto = %s WHERE sino = %s"
        
        mycursor.execute(sql, val)

               
        mydb.commit()
        





    retrieve=Button(windows,text="RETRIEVE",font=("",10),command=retrievee)
    retrieve.place(x=580,y=430)


    
   
     
    

def loggedin():

    issue()
    
    retrieve()

    
    AB=Button(windows,text="    ADD BOOK   ",fg="blue",font=("",15),command=add_book)
    AB.place(x=525,y=600)

    #SB=Button(windows,text="   SHOW BOOKS  ",fg="blue",font=("",15),command=show_books)
    #SB.place(x=700,y=600)

    AS=Button(windows,text="  ADD STUDENT  ",fg="blue",font=("",15),command=add_student)
    AS.place(x=100,y=600)

    #SS=Button(windows,text="SHOW STUDENTS",fg="blue",font=("",15),command=show_students)
    #SS.place(x=300,y=600)

    


    



        


windows.mainloop()
