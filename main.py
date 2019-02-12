from tkinter import *
import time
import sqlite3
import tkinter.messagebox as tmsg

db = sqlite3.connect("Books.db")
db.execute("CREATE TABLE IF NOT EXISTS DONATED(NAME CHAR[20], PHONE INT, ROLL_NO INT, BOOK CHAR[50])")
db.execute("CREATE TABLE IF NOT EXISTS BORROWED(NAME CHAR[20], PHONE INT, BOOK CHAR[50])")
db.commit()


def search():
    found = 0
    crsr = db.execute("SELECT * FROM DONATED")
    for row in crsr:
        if(row[3] == bsearch1.get()):
            tmsg.showinfo("Found", "Book Found!!")
            found = 1
            ans = tmsg.askyesno("Select Yes or No", "Do you want to borrow it?")
            if(ans == 1):
                tmsg.showinfo("Success", f"{bsearch1.get()} is Yours!")
                db.execute("INSERT INTO BORROWED(NAME, PHONE, BOOK) VALUES(?,?,?)",(bname1.get(), bphone1.get(), bsearch1.get()))
                db.commit()
            else:
                tmsg.showinfo("Done", "No Problem, Thanks & visit again")

            break
    if(found==0):
        tmsg.showerror("Not Found", "Book Not Found!")



def create():
    global bname1,bphone1, bsearch1

    bname1 = StringVar()
    bphone1 = IntVar()
    bsearch1 = StringVar()

    Label(root, text="Borrow a Book!", font="tahoma 15 bold", pady=15).grid(row=11, column=1)
    Label(root, text="Name: ", font="tahoma 10 bold", pady=10).grid(row =12,column=0)
    Label(root, text="Phone: ", font="tahoma 10 bold", pady=10).grid(row=13, column=0)
    Label(root, text="Search Book: ", font="tahoma 10 bold", pady=10).grid(row=14, column=0)

    bname = Entry(root, textvariable=bname1, width=50).grid(row=12, column=1)
    bphone = Entry(root, textvariable=bphone1, width=50).grid(row=13, column=1)
    bsearch = Entry(root, textvariable=bsearch1, width=50).grid(row=14, column=1)
    b1= Button(root, text="Search", font="tahoma 10 bold",command = search).grid(row=16, column=1)


def donate():
    db.execute("INSERT INTO DONATED(NAME, PHONE, ROLL_NO, BOOK) VALUES(?,?,?,?)",(name1.get(), phone1.get(),rollno1.get(), yourbook1.get()))
    db.commit()
    tmsg.showinfo("Success", "Donated Successfully!")
    db.close()

root = Tk()

root.geometry("445x820")

root.wm_iconbitmap("db.ico")


root.title("Student Database 2019")

cgc = PhotoImage(file = "cgc.png")
Label(root, image = cgc, padx = 10).grid(row = 0, column = 1, sticky = E)
Label(root, text = "CGC Book Service", font = "tahoma 15 bold", pady = 15).grid(row = 1, column = 1)
Label(root, text = "Name: ", font="tahoma 10 bold", pady = 10).grid(row = 2, column=0,sticky = W)
Label(root, text = "Phone: ", font = "tahoma 10 bold",  pady = 10).grid(row=3,column = 0,sticky = W)
Label(root,text = "Book Name: ", font = "tahoma 10 bold",  pady = 10).grid(row =4, column = 0,sticky = W)
Label(root,text = "Rollno: ", font = "tahoma 10 bold",  pady = 10).grid(row =5, column = 0,sticky = W)


global name1,phone1,rollno1,yourbook1

name1= StringVar()
phone1 = IntVar()
yourbook1 = StringVar()
rollno1 = IntVar()

name = Entry(root, textvariable = name1, width = 50).grid(row = 2,column = 1)
phone = Entry(root, textvariable = phone1, width = 50).grid(row = 3,column = 1)
yourbook = Entry(root, textvariable = yourbook1, width = 50).grid(row = 4,column = 1)
rollno = Entry(root, textvariable = rollno1, width =50).grid(row =5,column =1)


b = Button(root,text = "Donate your book", font = "tahoma 10 bold", command = donate).grid(row = 6, column = 1)

c=Button(root, text = "Borrow a book", command = create,font = "tahoma 10 bold").grid(row = 8,column=1)

# statusvar = StringVar()
# statusvar.set("Ready")
# sbar = Label(root, textvariable = statusvar, relief = SUNKEN)
# sbar.grid()

root.mainloop()