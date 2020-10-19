from tkinter import*
import tkinter.messagebox
from PIL import Image,ImageTk
import sqlite3

window=Tk()
window.title("REGISTRATION FORM")
window.geometry('500x800')
img=Image.open("C:/Users/hp/PycharmProjects/guitutorials/downloadfinal.png")
photo=ImageTk.PhotoImage(img)
lab=Label(image=photo)
lab.pack()



fn=StringVar()
ln=StringVar()
DOB=StringVar()
var=StringVar()
radio_var=StringVar()



def database():
        name1 = fn.get()
        name2 = ln.get()
        date = DOB.get()
        country = var.get()
        gender = radio_var.get()
        conn = sqlite3.connect("Form.db")
        with  conn:
            cursor = conn.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS Student(Name TEXT,Last TEXT,DOB TEXT,Country TEXT,Gender TEXT)')
            cursor.execute('INSERT INTO Student(Name,Last,DOB,Country,Gender) VALUES(?,?,?,?,?)', (name1, name2,date,country,gender))
            conn.commit()
            tkinter.messagebox.showinfo("Welcome","User is successfully signed up!!")


def exit1():
    print("Thanks")
    exit()


def abt():
    tkinter.messagebox.showinfo("Hey User","This is Signup Page")


menu=Menu(window)  #passing variable menu
window.config(menu=menu)

subm1=Menu(menu)
menu.add_cascade(label="File",menu=subm1)
subm1.add_command(label="Exit",command=exit1)

subm2=Menu(menu)
menu.add_cascade(label="Options",menu=subm2)
subm2.add_command(label="About",command=abt)






#def printt():
 #   print("Hello",fn.get(),"Your information is given below:")
  #  print("Your Full Name is:",fn.get(),ln.get())
   # print("Your DOB is:",DOB.get())
    #print("Your Country is:",var.get())
    #print("Your Gender is:",radio_var.get())

def secondwin():
    win=Tk()
    win.title("Welcome to login window")
    win.geometry('200x200')



label0=Label(window,text="Registration Form",relief="solid",font=('bold',16))
label0.pack()

label1=Label(window,text="First Name :",font=('arial',16))
label1.place(x=10,y=300)
entry1=Entry(window,textvar=fn)
entry1.place(x=200,y=305)


label2=Label(window,text="Last Name :",font=('arial',16))
label2.place(x=10,y=350)
entry2=Entry(window,textvar=ln)
entry2.place(x=200,y=350)

label3=Label(window,text="DOB :",font=('arial',16))
label3.place(x=10,y=400)
entry3=Entry(window,textvar=DOB)
entry3.place(x=200,y=400)


label4=Label(window,text="Country :",font=('arial',16))
label4.place(x=10,y=450)
list1=['Nepal','India','Canada']
droplist=OptionMenu(window,var,*list1)
var.set("Select Country")
droplist.place(x=200,y=450)

label5=Label(window,text="Gender :",font=('arial',16))
label5.place(x=10,y=500)
r2=Radiobutton(window,text="Female",variable=radio_var,value="Female")
r2.place(x=260,y=505)
r1=Radiobutton(window,text="Male",variable=radio_var,value="Male")
r1.place(x=200,y=505)


b1= Button(window,text="Signup",width=12,bg="brown",fg="white",command=database)
b1.place(x=150,y=600)


b2= Button(window,text="Quit",width=12,bg="brown",fg="white",command=exit1)
b2.place(x=250,y=600)

b3=Button(window,text="Login",width=12,bg="brown",fg="white",command=secondwin)
b3.place(x=200,y=650)

window.mainloop()