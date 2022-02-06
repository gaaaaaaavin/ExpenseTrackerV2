import os
from tkinter import ttk,messagebox
from tkinter import *
import pathlib
import webbrowser
import pandas as pd
import time
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

def folder_exists(folder_name):
    return pathlib.Path(folder_name).is_dir()
def create_folder(folder):
    try:
        if not folder_exists(folder):
            pathlib.Path(folder).mkdir(parents=True,exist_ok=True)
    except OSError as e:
        pass
def delete_folder(folder):
    try:
        if folder_exists(folder):
            pathlib.Path(folder).rmdir()
    except OSError as e:
        pass
def sync_folder(folder):
    delete_folder(folder)
    create_folder(folder)
def zipFolder():
    return None

def replace_line(fileName,lineNum,idd):
    rlines=open(fileName,"r").readlines()
    rlines[lineNum]="".join(idd+"\t0\t0-0000\tdeleted\t0\tdeleted\n")
    out=open(fileName,"w")
    print(type(rlines))
    out.writelines(rlines)
    out.close()

def alldata():
    vdf=pd.read_csv("logs\exp_log.txt",sep="\t",index_col="index")
    catSum=[] #sum each category
    for x in cat:
        y=vdf.loc[vdf["category"]==x]
        catSum.append(y["amount"].sum())
    allData = Toplevel()
    allData.title("All Data")
    allData.geometry("515x345")
    allData.iconbitmap=(icon)
    lab1=Label(allData,text="Scroll UP or DOWN:").place(x=90,y=135)
    text=Text(allData,width=90,height=20)
    text.insert(INSERT,vdf)
    text.place(x=10,y=10)

def errorCheck(): # checks if inputs are filled and is error free
    x=True
    if x==True:
        try:
            d=dd.get()
            m=mm.get()
            y=yyyy.get()
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
            i=itemName.get()[0]
            x=True
        except:
            messagebox.showerror("ERROR","Enter name for item.")
            x=False
    if x==True:
        try:
            amt=float(itemAmt.get())
            x=True
        except:
            messagebox.showerror("ERROR","Please enter an appropriate amount.")
            x=False
    return x

def save():
    global cat
    x=errorCheck()
    dom=str(dd.get())                                   # day of month
    date=str(mm.get())+"-"+str(yyyy.get())                # date
    itemname=itemName.get()                        # item name
#    currencySym=currencyE.get()                    # price currency
    itemamt=str(itemAmt.get())                      # item amount

    cate=catE.get()                              # item category
    expFile=pathlib.Path("logs\exp_log.txt")
    if x==True:
        with open("logs\exp_log.txt","r") as file:
            for x in file:
                lastIndex=x.split("\t")[0]
        if lastIndex=="index":
            lastIndex=0
        else:
            pass
        indexId=int(lastIndex)+1
        expFile=open("logs\exp_log.txt","a")
        log=[str(indexId),"\t",dom,"\t",date,"\t",itemname,"\t",itemamt,"\t",cate,"\n"]
        expFile.writelines(log)
        expFile.close()
        saveIndex=StringVar()
       
        saveIndex.set(indexId)
        savemsg="*saved\nIndex: "+saveIndex.get()
        label=Message(root,text=savemsg,fg="red")
        label.after("10000",label.destroy)
        label.place(x=5,y=195)
        #messagebox.showinfo("Expense Tracker","File Saved.")
        clearSave()
    else:
        pass

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
    global byMMmonth
    global byYYmonth
    byMMmonth=StringVar()
    byMMmonth.set(time.strftime("%m"))
    byYYmonth=StringVar()
    byYYmonth.set(time.strftime("%Y"))
    byMonth=Toplevel()
    byMonth.geometry("150x100")
    byMonth.iconbitmap(icon)
    byMonth.title("View data by month")
    selYearL=Label(byMonth,text="Year:").place(x=10,y=10)
    selYear=Spinbox(byMonth,width=5,from_=1000,to=9999,textvariable=byYYmonth).place(x=80,y=10)
    selMonL=Label(byMonth,text="Month:").place(x=10,y=35)
    selMon=Spinbox(byMonth,width=5,from_=1,to=12,textvariable=byMMmonth).place(x=80,y=35)
    byMonthBut=Button(byMonth,text="View Data",command=dataViewerbyMonth).place(x=40,y=65)
def dataViewerbyMonth():
    date=byMMmonth.get()+"-"+byYYmonth.get() 
    df=pd.read_csv("logs\exp_log.txt",sep="\t",index_col="index")
    
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
    plt.close('all')
    fig1,ax1=plt.subplots()
    fig1.canvas.set_window_title(date)
    ax1.pie(catSum,explode=explode,labels=cat,autopct='%1.1f%%',startangle=90)
    ax1.axis("equal")
    ax1.legend()
    dataByMonth = Toplevel()
    dataByMonth.title(date)
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
    month_sum=0
    for x in catSum:
        month_sum=float(x)+month_sum
    labSumMsg=StringVar()
    labSumMsg.set("total: "+str(month_sum))
    lab2=Label(dataByMonth,text=msg1,justify=LEFT).place(x=10,y=10)
    lab3=Label(dataByMonth,text=msg2,justify=RIGHT).place(x=100,y=10)
    labSum=Label(dataByMonth,text=labSumMsg.get()).place(x=300,y=10)

def byYear():
    df=pd.read_csv("logs\exp_log.txt",sep="\t",index_col="index")
    with open("logs\exp_log.txt","r") as file:
        for x in file:
            lastIndex=x.split("\t")[0]
    if lastIndex=="index":
        lastIndex=0
    else:
        pass
    lastIndex=int(lastIndex)
    rangeOfEntries=list(range(0,lastIndex))
    monthSets=[]
    for x in rangeOfEntries:
        y=df["month-year"].values[x]
        monthSets.append(y)
    monthSets=list(dict.fromkeys(monthSets)) # each month with year (no dupes)
    try:
        monthSets.remove("0-0000")
    except:
        pass
    yearSets=list(dict.fromkeys([int(x[-4:]) for x in monthSets]))# each year (no dupes)

    
    
    byYear=Toplevel()
    byYear.geometry("145x235")
    byYear.iconbitmap(icon)
    byYear.title("View data by year")
    selYearL=Label(byYear,text="Year:").place(x=10,y=10)



    
    def viewYears():
        global selectedYears
        
        selectedYears=[] # years selected in previous menue
        select=[]
        for x in yearLB.curselection():
            select.append(x)
        for x in select:
            selectedYears.append(yearDict[x])
        yearGraph={}
        for x in selectedYears:
            yearDF=df[df["month-year"].str.endswith(str(x), na = False)]
            monthSum=[]
            for month in range(1,13):
                month=str(month)+"-"
                monthDF=yearDF[df["month-year"].str.startswith(month, na = False)]
                y=monthDF["amount"].sum()
                monthSum.append(y)
            yearGraph[x]=monthSum
        if yearGraph=={}:
            pass
        else:
            byYear.geometry("700x235")
        plt.close('all')
        fig,ax=plt.subplots()
        fig.canvas.set_window_title("Data by years")
        for x in yearGraph:
            ax.plot(months,yearGraph[x],label=x)
            ax.legend()
        ax.plot(kind='area', stacked=False)
        
        yearlySum=yearGraph
        for years in yearlySum:
            yearTotal=sum(yearlySum[years])
            yearlySum[years]=yearTotal #sum per year
        text=Text(byYear,width=65,height=10)
        for x in yearlySum:
            yd=pd.read_csv("logs\exp_log.txt",sep="\t",index_col="index")
            dateDF=yd[yd["month-year"].str.endswith(str(x), na = False)]# new df from selected cate
            dateDF=dateDF.loc[:, dateDF.columns !="Unnamed: 0"]
            text.insert(INSERT,dateDF)
        text.place(x=150,y=45)
        yearSum=Tk()
        yrlen=len(selectedYears)
        tempgeo="200x"+str(40*yrlen-10)
        yearSum.geometry(tempgeo)
        yearSum.title("Yearly Sum:")
        yearSum.iconbitmap(icon)
        year_sum=str(sum(list(yearlySum.get(x) for x in yearlySum)))
        
        ytt=StringVar()
        ytt.set(year_sum)
        yearSumtext=Text(yearSum,width=15,height=yrlen+2)
        yearSumtext.insert(INSERT,"sum  : "+ytt.get()+"\n")
        yearSumtext.insert(INSERT,"YEAR : TOTAL"+"\n")
        
        for x in yearlySum:
            z=StringVar()
            z.set(str(x))
            a=StringVar()
            a.set(str(yearlySum[x]))
            y=z.get()+" : "+a.get()+"\n"
            yearSumtext.insert(INSERT,y)
        yearSumtext.place(x=0,y=0)
        yearSum.mainloop()
    

    yearDict={} #letterbox years
    for x in range(len(yearSets)):
        yearDict[x]=yearSets[x]
    yearLB=Listbox(byYear,selectmode=MULTIPLE,height=10)
    for x in range(len(yearSets)):
        yearLB.insert(x,yearSets[x])
    yearLB.place(x=10,y=45)
    byYearBut=Button(byYear,text="View/Update Data",command=viewYears).place(x=10,y=10)
    scrollInfo=Label(byYear,text="*scroll to view more").place(x=10,y=215)

    def graph():
        plt.show()
    lab1=Label(byYear,text="Scroll UP or DOWN:").place(x=185,y=215)
    but1=Button(byYear,text="View Graph",command=graph).place(x=150,y=10)


def totalCategoryYear():
    df=pd.read_csv("logs\exp_log.txt",sep="\t",index_col="index")
    with open("logs\exp_log.txt","r") as file:
        for x in file:
            lastIndex=x.split("\t")[0]
    if lastIndex=="index":
        lastIndex=0
    else:
        pass
    lastIndex=int(lastIndex)
    rangeOfEntries=list(range(0,lastIndex))
    monthSets=[]
    for x in rangeOfEntries:
        y=df["month-year"].values[x]
        monthSets.append(y)
    monthSets=list(dict.fromkeys(monthSets)) # each month with year (no dupes)
    try:
        monthSets.remove("0-0000")
    except:
        pass
    yearSets=list(dict.fromkeys([int(x[-4:]) for x in monthSets]))# each year (no dupes)

    
    
    cateByYr=Toplevel()
    cateByYr.geometry("145x235")
    cateByYr.iconbitmap(icon)
    cateByYr.title("View data by year")
    selYearL=Label(cateByYr,text="Year:").place(x=10,y=10)



    
    def viewCateYears():
        global selectedCateYears
        
        selectedCateYears=[] # years selected in previous menue eg. [2020,2022]
        select=[]                       #index of slected years eg. [0,2]
        for x in yearLB.curselection():
            select.append(x)
        for x in select:
            selectedCateYears.append(yearDict[x])
        yearCateGraph={}
        df=pd.read_csv("logs\exp_log.txt",sep="\t",index_col="index")
        for year in selectedCateYears:
            yearDF=df[df["month-year"].str.endswith(str(year),na=False)] # looks through main df for years selected
            catSum=[] # sum of each category                             # and assigns it to yearDF
            for category in cat:
                y=yearDF.loc[df["category"]==category]                   # looks through each year selected and assigns
                catSum.append(y["amount"].sum())                         # the sum of each cat to a list called catSum
            maxCatSum=max(catSum)
            yearCateGraph[year]=catSum
        if yearCateGraph=={}:
            pass
        else:
            cateByYr.geometry("700x235")
        plt.close('all')
        fig,ax=plt.subplots()
        fig.canvas.set_window_title("Data by years")
        for x in yearCateGraph:                                          ### change to pie
            ax.plot(cat,yearCateGraph[x],label=x)
            ax.legend()
        ax.set_xticklabels(labels=cat,rotation=90)
        yearlySum=yearCateGraph.copy()
        for years in yearlySum:
            yearTotal=sum(yearlySum[years])
            yearlySum[years]=yearTotal #sum per year
        text=Text(cateByYr,width=65,height=10)
        for x in yearlySum:
            yd=pd.read_csv("logs\exp_log.txt",sep="\t",index_col="index")
            dateDF=yd[yd["month-year"].str.endswith(str(x), na = False)]# new df from selected cate
            dateDF=dateDF.loc[:, dateDF.columns !="Unnamed: 0"]
            text.insert(INSERT,dateDF)
        text.place(x=150,y=45)
        
        yearSum=Tk()
        catlen=len(cat)
        tempgeo="200x"+str(40*catlen-10)
        yearSum.geometry(tempgeo)
        yearSum.title("Yearly Category Sum:")
        yearSum.iconbitmap(icon)
        
        cateGraph={}
        for x in range(len(cat)):
            catname=cat[x]
            tempcattotal=0
            for y in yearCateGraph.values():
                
                tempcattotal+=y[x]
                
                cateGraph[catname]=tempcattotal # categories and total by selected years
        cate_sum=str(sum(list(cateGraph.get(x) for x in cateGraph)))
        
        yctt=StringVar()
        yctt.set(cate_sum)

        yearSumtext=Text(yearSum,width=30,height=catlen+2)
        yearSumtext.insert(INSERT,"sum      : "+yctt.get()+"\n")
        yearSumtext.insert(INSERT,"CATEGORY : TOTAL"+"\n")
        for x in cateGraph:
            z=StringVar()
            z.set(str(x))
            a=StringVar()
            a.set(str(cateGraph[x]))
            y=z.get()+" : "+a.get()+"\n"
            yearSumtext.insert(INSERT,y)
        yearSumtext.place(x=0,y=0)
        yearSum.mainloop()
    

    yearDict={} #letterbox years
    for x in range(len(yearSets)):
        yearDict[x]=yearSets[x]
    yearLB=Listbox(cateByYr,selectmode=MULTIPLE,height=10)
    for x in range(len(yearSets)):
        yearLB.insert(x,yearSets[x])
    yearLB.place(x=10,y=45)
    byYearBut=Button(cateByYr,text="View/Update Data",command=viewCateYears).place(x=10,y=10)
    scrollInfo=Label(cateByYr,text="*scroll to view more").place(x=10,y=215)

    def graph():
        plt.show()
    lab1=Label(cateByYr,text="Scroll UP or DOWN:").place(x=185,y=215)
    but1=Button(cateByYr,text="View Graph",command=graph).place(x=150,y=10)

def byIndex():
    df=pd.read_csv("logs\exp_log.txt",sep="\t")
    with open("logs\exp_log.txt","r") as file:
        for x in file:
            lastIndex=x.split("\t")[0]
    
    def byIndexClick():         #button to view entry
        def confirm_delete():   #button to confirm entry delection      
            def del_entry():
                idIndex=str(indexSearch.get())
                indexLs=[]
                indexDict={}
                with open("logs\exp_log.txt","r") as file:                  # gives indexs
                    for x in file:
                        indexLs.append(x.split("\t")[0])
                with open("logs\exp_log.txt", 'r') as file:
                    data = file.readlines()
                for line in range(len(data)):                               # gives lines
                    indexDict[indexLs[line]]=[line]                           # dict{"index":lineNo}
                for tempId in indexDict[idIndex]:
                    str(tempId)
                replace_line("logs\exp_log.txt",tempId,idIndex)
                df=pd.read_csv("logs\exp_log.txt",sep="\t")
                byIndexTk.geometry("583x169")
                label2=Text(byIndexTk,width=70,height=2)
                label2.insert(INSERT,df.loc[df["index"]==indexSearch.get()])
                label2.place(x=10,y=85)

            byIndexTk.geometry("583x231")
            label3=Label(byIndexTk,text="Are you sure you want to delete entry "+str(indexSearch.get()))
            label3.place(x=10,y=165)
            confirmBut=Button(byIndexTk,text="Delete "+str(indexSearch.get()),command=del_entry)
            confirmBut.place(x=10,y=195)
        df=pd.read_csv("logs\exp_log.txt",sep="\t")
        try:
            checker=int(indexSearch.get())*1
            byIndexTk.geometry("583x169")
            
            label2=Text(byIndexTk,width=70,height=2)
            label2.insert(INSERT,df.loc[df["index"]==indexSearch.get()])
            label2.place(x=10,y=85)
            delBut=Button(byIndexTk,text="Delete Entry",command=confirm_delete).place(x=10,y=135)
    
        except:
            messagebox.showerror("ERROR","Enter a number.")
        

        
    indexSearch=IntVar()
    maxIndexAvail=IntVar()
    maxIndexAvail.set(lastIndex)
    
    byIndexTk=Toplevel()
    byIndexTk.geometry("175x70")
    byIndexTk.title("Specific Entry Viewer:")
    byIndexTk.iconbitmap(icon)
    
    label1=Label(byIndexTk,text="Pick an entry from 0 to "+str(maxIndexAvail.get()))
    label1.place(x=10,y=10)
    
    indexInput=Entry(byIndexTk,width=15,textvariable=indexSearch).place(x=10,y=35)
    IndexButton=Button(byIndexTk,width=5,text="Search",command=byIndexClick).place(x=120,y=30)

# Variables:
icon="icon.ico"
root=Tk()
root.title("Expense Tracker")
root.iconbitmap(icon)
root.geometry("320x250")
catFileDF=pd.read_csv("logs\cat.txt")
cat=[]
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
months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
expFile=pathlib.Path("logs\exp_log.txt")

sync_folder("logs")
if expFile.exists():
    pass
else:
    expFile=open("logs\exp_log.txt","a")
    expFile.write("index\tday\tmonth-year\titemname\tamount\tcategory\n")
    expFile.close()

catE=StringVar()
catE.set(ci7)
dd=IntVar()
dd.set(time.strftime("%d"))
mm=IntVar()
mm.set(time.strftime("%m"))
yyyy=IntVar()
yyyy.set(time.strftime("%Y"))
itemName=StringVar()
currencySym=StringVar()
itemAmt=StringVar()

# Menu
expMenu=Menu(root)
root.config(menu=expMenu)
file_menu=Menu(expMenu)                                             # File menu
expMenu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="Save",command=save)                        # save
file_menu.add_command(label="Clear",command=clearSave)                  # clear
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)                   # exit
data_menu=Menu(expMenu)                                             # ViewData menu
expMenu.add_cascade(label="View Data",menu=data_menu)
data_menu.add_command(label="By Index",command=byIndex)                 # index
data_menu.add_separator()
data_menu.add_command(label="By Month",command=byMonth)                 # month
data_menu.add_command(label="By Year",command=byYear)                   # year
data_menu.add_command(label="By Category",command=totalCategoryYear)    # category
data_menu.add_separator()
data_menu.add_command(label="All",command=alldata)                      # all
data_menu.add_separator()
miss_dm=StringVar()
miss_dm.set("missing data?\n restart")
data_menu.add_command(label=miss_dm.get(),command=root.quit)#all
help_menu=Menu(expMenu)                                             # Help menu
expMenu.add_cascade(label="Help",menu=help_menu)
help_menu.add_command(label="Getting started",command=tutorial)         #add tutorial
help_menu.add_command(label="Report bugs",command=contact)
help_menu.add_separator()
help_menu.add_command(label="Credits",command=credit)

# Dates
enterDate=Label(root,text="Date: ").place(x=10,y=10)
day=Spinbox(root,width=3,from_=1,to=31,textvariable=dd).place(x=80,y=10)
month=Spinbox(root,width=3,from_=1,to=12,textvariable=mm).place(x=120,y=10)
year=Spinbox(root,width=5,from_=1,to=9999,textvariable=yyyy).place(x=160,y=10)
dateFormat=Label(root,text="* dd mm yy").place(x=210,y=10)

# Expense Name
itemNameL=Label(root,text="Item name: ").place(x=10,y=35)
itemNameE=Entry(root,width=30,textvariable=itemName)
itemNameE.place(x=80,y=35)
# Amount
itemAmountL=Label(root,text="Amount: ").place(x=10,y=60)
#currencyE=Entry(root,width=3,textvariable=currencySym).place(x=210,y=60) # change from Entry to Radio button
itemAmountE=Entry(root,width=20,textvariable=itemAmt)
itemAmountE.place(x=80,y=60)

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
saveInput=Button(root,text="Save",width=10,command=save).place(x=70,y=195)
clearInput=Button(root,text="Clear",width=10,command=clearSave).place(x=180,y=195)

root.mainloop()

