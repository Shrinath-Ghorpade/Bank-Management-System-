import tkinter as tk
from tkinter import *
import mysql.connector

con=mysql.connector.connect(host='localhost',user='root',password="S#8378@qlph",database="Bank_database")
cursor=con.cursor()

# cursor.execute("CREATE DATABASE Bank_database")

cursor.execute("""CREATE TABLE Bank_table 
                (NAME TEXT NOT NULL,
                ACCOUNT_NO INT PRIMARY KEY,
               TYPEOF_ACCOUNT TEXT NOT NULL,
               BALANCE INT NOT NULL)""")

root=Tk()
root.geometry("700x500")

def show():

        screen=Toplevel()   

        name=tk.Label(text="Name:")
        name_entry=tk.Entry()

        account=tk.Label(text="Account_no:")
        account_entry=tk.Entry()

        typeofaccount=tk.Label(text="Type_of_account:")
        typeofaccount_entry=tk.Entry()

        Balance=tk.Label(text="Balance:")
        Balance_entry=tk.Entry()

        name.grid(row=0 , column=1)
        name_entry.grid(row=0,column=2)

        account.grid(row=1,column=1)
        account_entry.grid(row=1,column=2)

        typeofaccount.grid(row=2,column=1)
        typeofaccount_entry.grid(row=2,column=2)

        Balance.grid(row=3,column=1)
        Balance_entry.grid(row=3,column=2)
    
        Name=name_entry.get()
        Account_no=account_entry.get()
        Type_of_account=typeofaccount_entry.get()
        Balance=Balance_entry.get()

        data=(Name,Account_no,Type_of_account,Balance)
        sql="insert into Bank_table values(%s,%s,%s,%s)"

        cursor.execute(sql,data)
        con.commit()

def display():

        cursor.execute("select * from Bank_table")
        row=cursor.fetchall()

        for i in row:
                print("Name:",i[0])
                print("Account_no:",i[1])
                print("Typeofaccount:",i[2])
                print("Balance:",i[3])

def deposite():
        Deposite=int(input("Enter your deposite amount:"))
        ac=int(input("Enter your account no:"))

        query="select Balance from Bank_table where Account_no=%s"

        data=(ac,)

        cursor.execute(query,data)

        row=cursor.fetchone()

        total=row[0]+Deposite

        query2="update Bank_table set Balance=%s where Account_no=%s"

        d=(total,ac)

        cursor.execute(query2,d)


insert=tk.Button(text="Insert",command=show)
insert.grid(row=5,column=2)

show=tk.Button(text="show",command=display)
show.grid(row=6,column=3)


deposite=tk.Button(text="Deposite",command=deposite)
deposite.grid(row=7,column=3)

root.mainloop()
