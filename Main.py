from tkinter import *
from tkinter import ttk
import mysql.connector

con=mysql.connector.connect(host='localhost',user='root',password="root123",database="Bank_database")

cursor=con.cursor()

mainwindow=Tk()
mainwindow.geometry("700x500")


def insert_button():
        
        Name=tname.get()
        Account_no=taccountno.get()
        Type_of_account=ttypeofaccount.get()
        Balance=tbalance.get()

        data=(Name,Account_no,Type_of_account,Balance)
        sql="insert into Bank_table values(%s,%s,%s,%s)"

        cursor.execute(sql,data)
        con.commit()

        

def insert():
    
        global tname
        global taccountno
        global ttypeofaccount
        global tbalance

        tname=StringVar()
        taccountno=IntVar()
        ttypeofaccount=StringVar()
        tbalance=IntVar()

        insert_screen=Toplevel(mainwindow)   
        insert_screen.geometry('500x500')

        name=Label(insert_screen,text="Name:").grid(row=0 , column=1)
        name_entry=Entry(insert_screen,textvariable=tname).grid(row=0,column=2)
        

        account=Label(insert_screen,text="Account_no:").grid(row=1,column=1)
        account_entry=Entry(insert_screen,textvariable=taccountno).grid(row=1,column=2)

        typeofaccount=Label(insert_screen,text="Type_of_account:").grid(row=2,column=1)
        typeofaccount_entry=Entry(insert_screen,textvariable=ttypeofaccount).grid(row=2,column=2)

        Balance=Label(insert_screen,text="Balance:").grid(row=3,column=1)
        Balance_entry=Entry(insert_screen,textvariable=tbalance).grid(row=3,column=2)
        
        Button(insert_screen,text="Insert",command=insert_button,width=20).grid(row=5,column=2,pady=10)


def deposite_button():
        
        ac=tac.get()
        Deposite=tdeposite.get()

        sql="select Balance from Bank_table WHERE Account_no=%s"
        data=(ac,)
        cursor.execute(sql,data)

        row=cursor.fetchone()
    
        total=row[0]+Deposite

        sql2="update Bank_table set Balance=%s where Account_no=%s"
        d=(total,ac)
        cursor.execute(sql2,d)

        con.commit()

def deposite():
        
        global tdeposite
        global tac

        tdeposite=IntVar()
        tac=IntVar()
        deposite_screen=Toplevel(mainwindow)
        deposite_screen.geometry("500x500")

        Label(deposite_screen,text="Enter the deposite amount").grid(row=2,column=2)
        Entry(deposite_screen,textvariable=tdeposite).grid(row=2,column=3)

        Label(deposite_screen,text="Enter accountno").grid(row=3,column=2)
        Entry(deposite_screen,textvariable=tac).grid(row=3,column=3)

        Button(deposite_screen,text="Deposite",width=20,command=deposite_button).grid(row=4,column=3,pady=10)

def withdraw_button():

    Withdraw=twithdraw.get()
    a=ta.get()
    sql="select Balance from Bank_table where Account_no=%s"
    data=(a,)
    cursor.execute(sql,data)

    row=cursor.fetchone()

    total=row[0]-Withdraw

    sql2="update Bank_table set Balance=%s where Account_no=%s"
    d=(total,a)
    cursor.execute(sql2,d)

    con.commit()

def withdraw():
    
        global twithdraw
        global ta

        twithdraw=IntVar()
        ta=IntVar()
        withdraw_screen=Toplevel(mainwindow)
        withdraw_screen.geometry("500x500")

        Label(withdraw_screen,text="Enter the deposite amount").grid(row=2,column=2)
        Entry(withdraw_screen,textvariable=twithdraw).grid(row=2,column=3)

        Label(withdraw_screen,text="Enter accountno").grid(row=3,column=2)
        Entry(withdraw_screen,textvariable=ta).grid(row=3,column=3)

        Button(withdraw_screen,text="Withdraw",width=20,command=withdraw_button).grid(row=4,column=3,pady=10)

def display():
       
    display_screen=Toplevel(mainwindow)
    display_screen.geometry("500x500")
    
   
    a=cursor.execute("select * from Bank_table")
    
    
   
    tree=ttk.Treeview(display_screen)
    tree['show']='headings'

    style=ttk.Style()
    style.configure("tree.heading",
                    background="black")

    tree['columns']=("Name","Account_no","Type_of_account","Balance")

    tree.column("Name",width=100,minwidth=100,anchor=CENTER)
    tree.column("Account_no",width=100,minwidth=100,anchor=CENTER)
    tree.column("Type_of_account",width=100,minwidth=100,anchor=CENTER)
    tree.column("Balance",width=100,minwidth=100,anchor=CENTER)

    tree.heading("Name",text="Name",anchor=CENTER)
    tree.heading("Account_no",text="Account_no",anchor=CENTER)
    tree.heading("Type_of_account",text="Type_of_account",anchor=CENTER)
    tree.heading("Balance",text="Balance",anchor=CENTER)

    
    i=0
    for ro in cursor:
           tree.insert("", i, text=" ",values=(ro[0],ro[1],ro[2],ro[3]))
           i=i+1

    
    tree.pack()
    con.commit()
       

label=Label(mainwindow, text="Sincere Bank",font=("Timesnewroman",20))
label.place(relx = 0.5, rely = 0.1, anchor = CENTER)


Label(mainwindow,text="            *****WELCOME TO SINCERE BANK*****",font=(18)).place(relx=0.22,rely=0.2)


Button(mainwindow,text="CREATE NEW ACCOUNT",width=20,command=insert).place(relx=0.2,rely=0.3)

Button(mainwindow,text="DEPOSITE AMOUNT",width=20,command=deposite).place(relx=0.6,rely=0.3)

Button(mainwindow,text="DIPLAY ALL DETAILS",width=20,command=display).place(relx=0.2,rely=0.4)

Button(mainwindow,text="WITHDRAW AMOUNT",width=20,command=withdraw).place(relx=0.6,rely=0.4)
mainwindow.mainloop()