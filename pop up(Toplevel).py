import pandas as pd
from tkinter import *
from tkinter import ttk
vdf=pd.read_excel("logs\exp_log.xlsx","sheet1",index_col=[0])

def dataDf(df):
    allData = Toplevel()
    allData.title("All Data")
    allData.geometry("800x800")
    cols=list(df.columns)

    tree=ttk.Treeview(allData)
    tree.place(x=10,y=40)
    tree["columns"]=cols
    for i in cols:
        tree.column(i,anchor="w")
        tree.heading(i,text=i,anchor='w')

    for index, row in df.iterrows():
        tree.insert("",0,text=index,values=list(row))

root=Tk()
button=Button(root,text="CLICK ME",command=alldata).pack(pady=10)
root.mainloop()