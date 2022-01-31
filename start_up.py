from tkinter import  messagebox,ttk
from tkinter import *
import pathlib
import os

#cat=[,,"","","","","",""]
def set_up_page():                              # Start page
    
    def confirmCate():                          # Confirms categories
        confirm=messagebox.askyesno("Categories","Continue with selected titles?")
        if confirm==True:
            catList=[]
            catList.append(cat0.get().lower())
            catList.append(cat1.get().lower())
            catList.append(cat2.get().lower())
            catList.append(cat3.get().lower())
            catList.append(cat4.get().lower())
            catList.append(cat5.get().lower())
            catList.append(cat6.get().lower())
            catList.append(cat7.get().lower())
            cat=",".join(catList)
            expFile=open("logs\cat.txt","a")
            expFile.write(cat)
            expFile.close()
            startpg.destroy()
            mainpg()
        elif confirm==False:
            print("no")
        else:
            print("confirmCate func error")
        
    
    
    
    startpg=Tk()
    startpg.geometry("400x400")
    
    cat0=StringVar()
    cat0.set("Clothing")
    cat1=StringVar()
    cat1.set("Entertainment")
    cat2=StringVar()
    cat2.set("Food")
    cat3=StringVar()
    cat3.set("Grooming")
    cat4=StringVar()
    cat4.set("Transportation")
    cat5=StringVar()
    cat5.set("Utilities")
    cat6=StringVar()
    cat6.set("Work")
    cat7=StringVar()
    cat7.set("Other")

    
    
    lab1=Label(startpg,text="Before we start tracking, we've got to set a few things up").place(x=10,y=10)
    lab2=Label(startpg,text="Please type in Category titles or leave it with the default titles").place(x=10,y=30)
    catE0=Entry(startpg,width=15,textvariable=cat0).place(x=40,y=85)
    catE1=Entry(startpg,width=15,textvariable=cat1).place(x=40,y=110)
    catE2=Entry(startpg,width=15,textvariable=cat2).place(x=40,y=135)
    catE3=Entry(startpg,width=15,textvariable=cat3).place(x=40,y=160)
    catE4=Entry(startpg,width=15,textvariable=cat4).place(x=160,y=85)
    catE5=Entry(startpg,width=15,textvariable=cat5).place(x=160,y=110)
    catE6=Entry(startpg,width=15,textvariable=cat6).place(x=160,y=135)
    catE7=Entry(startpg,width=15,textvariable=cat7).place(x=160,y=160)
    confirmBut=Button(startpg,width=10,text="Confirm",command=confirmCate).place(x=60,y=200)
    exitBut=Button(startpg,width=10,text="Exit",command=startpg.destroy).place(x=170,y=200)




    
    startpg.mainloop()



def mainpg():                                   # Launches main.py (main application)
    import main


catFile=pathlib.Path("logs\cat.txt")
if catFile.exists():
    mainpg()
else:
    set_up_page()
    
    
