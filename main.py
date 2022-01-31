from tkinter import ttk,messagebox
from tkinter import *
import pathlib
import webbrowser
import pandas as pd
import time
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', None)


def alldata():
    global vdf
    catSum=[] #sum each category
    #cat=str(cat)
    #for x in range(len(cat)):
    #    cat[x]=cat[x].lower()
    for x in cat:
        y=vdf.loc[df["category"]==x]
        catSum.append(y["amount"].sum())
    allData = Toplevel()
    allData.title("All Data")
    allData.geometry("800x800")
    lab1=Label(allData,text="Scroll UP or DOWN:").place(x=185,y=135)
 #   but1=Button(allData,text="View Pie Chart",command=pie).place(x=350,y=125)
    text=Text(allData,width=90,height=10)
    text.insert(INSERT,vdf)
    text.place(x=10,y=160)
    msg1="\n".join(cat)
    catsum=catSum
    for x in range(len(catsum)):
        catsum[x]=str(catsum[x])
    msg2="\n".join(catsum)
    lab2=Label(allData,text=msg1,justify=LEFT).place(x=10,y=10)
    lab3=Label(allData,text=msg2,justify=RIGHT).place(x=100,y=10)



def errorCheck(): # checks if inputs are filled and is error free
    x=True
    if x==True:
        try:
            d=int(day.get())
            m=int(month.get())
            y=int(year.get())
            x=True
            if d<=31 and m<=12 and y>=1000 and y<=9999:
                x=True
            else:
                messagebox.showerror("ERROR","Please enter an appropriate date.")
                x=False                
        except:
            messagebox.showerror("ERROR","Please enter an appropriate date.")
            x=False
    if x==True:
        try:
            i=itemNameE.get()[0]
            x=True
        except:
            messagebox.showerror("ERROR","Enter name for item.")
            x=False
    if x==True:
        try:
            amt=float(itemAmountE.get())
            x=True
        except:
            messagebox.showerror("ERROR","Please enter an appropriate amount.")
            x=False
    return x

def save():
    global cat
    x=errorCheck()
    dom=day.get()                                   # day of month
    date=month.get()+"-"+year.get()                 # date
    itemName=itemNameE.get()                        # item name
#    currencySym=currencyE.get()                    # price currency
    itemAmt=itemAmountE.get()                       # item amount
    cate=catE.get()                              # item category
    expFile=pathlib.Path("logs\exp_log.txt")
    if x==True:
        if expFile.exists():
            pass
        else:
            expFile=open("logs\exp_log.txt","a")
            expFile.write("day\tmonth-year\titemname\tamount\tcategory\n")
            expFile.close()
        expFile=open("logs\exp_log.txt","a")
        log=[dom,"\t",date,"\t",itemName,"\t",itemAmt,"\t",cate,"\n"]
        expFile.writelines(log)
        expFile.close()
        label = Message( root, text = "*file saved",fg="red")
        label.after("3000",label.destroy)
        label.place(x=5,y=195)
        #messagebox.showinfo("Expense Tracker","File Saved.")
        #clearSave()
    else:
        pass
    df=pd.read_csv("logs\exp_log.txt",sep="\t")    #converts .txt to .xlsx
    df.to_excel("logs\exp_log.xlsx","sheet1")

def clear():
    day.delete(0,END)
    month.delete(0,END)
    itemNameE.delete(0,END)
    itemAmountE.delete(0,END)

def clearSave():
    itemNameE.delete(0,END)
    itemAmountE.delete(0,END)

def contact():
    info="message me on:\nhttps://github.com/gaaaaaaavin"
    messagebox.showinfo("Contact",info)

def credit():
    webbrowser.open_new_tab("https://github.com/gaaaaaaavin")

def tutorial():
    pass

def byMonth():
    byMonth=Toplevel()
    byMonth.geometry("150x100")
    byMonth.iconbitmap(icon)
    byMonth.title("View data by month")
    selYearL=Label(byMonth,text="Year:").place(x=10,y=10)
    selYear=Spinbox(byMonth,width=5,from_=1000,to=9999,textvariable=yyyy).place(x=80,y=10)
    selMonL=Label(byMonth,text="Month:").place(x=10,y=35)
    selMon=Spinbox(byMonth,width=5,from_=1,to=12,textvariable=mm).place(x=80,y=35)
    byMonthBut=Button(byMonth,text="View Data",command=dataViewerbyMonth).place(x=40,y=65)
def dataViewerbyMonth():
    date=month.get()+"-"+year.get() 
    global df
    
    dateDF=df.loc[df["month-year"]==date] # new df from selected cate
    catSum=[] #sum each category
    for x in cat:
        y=dateDF.loc[df["category"]==x]
        catSum.append(y["amount"].sum())
    maxCatSum=max(catSum)
    explode=[]
    for x in catSum:
        y=x/maxCatSum
        explode.append(y)
    explode=tuple(explode)
    #print(catSum)
    #explode=(0,0,0,0,0,0,0,0) # pie that sticks out
    fig1, ax1 = plt.subplots()
    fig1.canvas.set_window_title("View data by month")
    ax1.pie(catSum,explode=explode,labels=cat,autopct='%1.1f%%',startangle=90)
    ax1.axis('equal')
    ax1.legend()
    dataByMonth = Toplevel()
    dataByMonth.title("By Month")
    dataByMonth.geometry("800x400")
    dataByMonth.iconbitmap(icon)
    def pie():    
        plt.show()
    lab1=Label(dataByMonth,text="Scroll UP or DOWN:").place(x=185,y=135)
    but1=Button(dataByMonth,text="View Pie Chart",command=pie).place(x=350,y=125)
    text=Text(dataByMonth,width=90,height=10)
    text.insert(INSERT,dateDF)
    text.place(x=10,y=160)
    catsum=catSum
    for x in range(len(catsum)):
        catsum[x]=str(catsum[x])
    msg1="\n".join(cat)
    msg2="\n".join(catsum)
    lab2=Label(dataByMonth,text=msg1,justify=LEFT).place(x=10,y=10)
    lab3=Label(dataByMonth,text=msg2,justify=RIGHT).place(x=100,y=10)

    


def byYear():                       #add button for graph view
    byYear=Toplevel()
    byYear.geometry("150x100")
    byYear.iconbitmap(icon)
    byYear.title("View data by year")
    selYearL=Label(byYear,text="Year:").place(x=10,y=10)
    selYear=Spinbox(byYear,width=5,from_=1000,to=9999,textvariable=yyyy).place(x=80,y=10)
    byMonthBut=Button(byYear,text="View Data",command=dataViewerbyYear).place(x=40,y=65)
def dataViewerbyYear():
    date=year.get() 
    global df
    cat=["Clothing","Entertainment","Food","Grooming","Transportation","Utilities","Work","Other"]
    bool_series = df["month-year"].str.endswith(date, na = False) # new df from selected cate
    dateDF=df[bool_series]
    catSum=[] #sum each category
    for x in range(len(cat)):
        cat[x]=cat[x].lower()
    for x in cat:
        y=dateDF.loc[df["category"]==x]
        catSum.append(y["amount"].sum())
    allData = Toplevel()
    allData.title("All Data")
    allData.geometry("800x800")
    lab1=Label(allData,text="Scroll UP or DOWN:").place(x=185,y=135)
 #   but1=Button(allData,text="View Pie Chart",command=pie).place(x=350,y=125)
    text=Text(allData,width=90,height=10)
    text.insert(INSERT,dateDF)
    text.place(x=10,y=160)
    msg1="\n".join(cat)
    catsum=catSum
    for x in range(len(catsum)):
        catsum[x]=str(catsum[x])
    msg2="\n".join(catsum)
    lab2=Label(allData,text=msg1,justify=LEFT).place(x=10,y=10)
    lab3=Label(allData,text=msg2,justify=RIGHT).place(x=100,y=10)

icon="icon.ico"
root=Tk()
root.title("Expense Tracker")
root.iconbitmap(icon)
root.geometry("320x250")



# Variables:
####

catFileDF=pd.read_csv("logs\cat.txt")

cat=[]                      # categories

for x in catFileDF:
    cat.append(x)
ci0=cat[0]
ci1=cat[1]
ci2=cat[2]
ci3=cat[3]
ci4=cat[4]
ci5=cat[5]
ci6=cat[6]
ci7=cat[7]
####


expFile=pathlib.Path("logs\exp_log.xlsx")
if expFile.exists():
    pass
else:
    expFile=open("logs\exp_log.txt","a")
    expFile.write("day\tmonth-year\titemname\tamount\tcategory\n")
    expFile.close()
df=pd.read_csv("logs\exp_log.txt",sep="\t")    #converts .txt to .xlsx
df.to_excel("logs\exp_log.xlsx","sheet1")
df=pd.read_excel("logs\exp_log.xlsx","sheet1")
vdf=pd.read_excel("logs\exp_log.xlsx","sheet1",index_col=[0])
catE=StringVar() 
dd=IntVar()
dd.set(time.strftime("%d"))
mm=IntVar()
mm.set(time.strftime("%m"))
yyyy=IntVar()
yyyy.set(time.strftime("%Y"))
itemName=StringVar()
currencySym=StringVar()
itemAmt=IntVar()

# Menu
expMenu=Menu(root)
root.config(menu=expMenu)
file_menu=Menu(expMenu)         # File menu
expMenu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="Save",command=save)
file_menu.add_command(label="Clear",command=clear)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)
data_menu=Menu(expMenu)         # ViewData menu
expMenu.add_cascade(label="View Data",menu=data_menu)
data_menu.add_command(label="By Month",command=byMonth)#month
data_menu.add_command(label="By Year",command=byYear)#year
data_menu.add_command(label="By Category",command=contact)#category
data_menu.add_separator()
data_menu.add_command(label="All",command=alldata)#all
help_menu=Menu(expMenu)         # Help menu
expMenu.add_cascade(label="Help",menu=help_menu)
help_menu.add_command(label="Getting started",command=tutorial)#add tutorial
help_menu.add_command(label="Report bugs",command=contact)
help_menu.add_separator()
help_menu.add_command(label="Credits",command=credit)

# Dates
enterDate=Label(root,text="Date: ")
day=Spinbox(root,width=3,from_=1,to=31,textvariable=dd)
month=Spinbox(root,width=3,from_=1,to=12,textvariable=mm)
year=Spinbox(root,width=5,from_=1,to=9999,textvariable=yyyy)
dateFormat=Label(root,text="* dd mm yy")

enterDate.place(x=10,y=10)
day.place(x=80,y=10)
month.place(x=120,y=10)
year.place(x=160,y=10)
dateFormat.place(x=210,y=10)

# Expense Name
itemNameL=Label(root,text="Item name: ")
itemNameE=Entry(root,width=30,textvariable=itemName)

itemNameL.place(x=10,y=35)
itemNameE.place(x=80,y=35)

# Amount
itemAmountL=Label(root,text="Amount: ")
currencyE=Entry(root,width=3,textvariable=currencySym) # change from Entry to Radio button
itemAmountE=Entry(root,width=20,textvariable=itemAmt)

itemAmountL.place(x=10,y=60)
itemAmountE.place(x=80,y=60)
#currencyE.place(x=210,y=60)

# Category
CategoryL=Label(root,text="Category: ").place(x=10,y=85)
c1=ttk.Radiobutton(root,text=ci0,variable=catE,value=ci0).place(x=80,y=85)
c2=ttk.Radiobutton(root,text=ci1,variable=catE,value=ci1).place(x=80,y=110)
c3=ttk.Radiobutton(root,text=ci2,variable=catE,value=ci2).place(x=80,y=135)
c4=ttk.Radiobutton(root,text=ci3,variable=catE,value=ci3).place(x=80,y=160)
c5=ttk.Radiobutton(root,text=ci4,variable=catE,value=ci4).place(x=200,y=85)
c6=ttk.Radiobutton(root,text=ci5,variable=catE,value=ci5).place(x=200,y=110)
c7=ttk.Radiobutton(root,text=ci6,variable=catE,value=ci6).place(x=200,y=135)
c8=ttk.Radiobutton(root,text=ci7,variable=catE,value=ci7).place(x=200,y=160)



# Save / Clear

saveInput=Button(root,text="Save",width=10,command=save)
clearInput=Button(root,text="Clear",width=10,command=clear)

saveInput.place(x=70,y=195)
clearInput.place(x=180,y=195)

root.mainloop()
