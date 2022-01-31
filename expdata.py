def totalAll(df): # Returns total sum of all categories
    x=df["amount"].sum()
    return x
#print(totalAll(df))

def cat(category): # Returns DataFrame of selected category
    import pandas as pd
    df=pd.read_excel("logs/exp_log.xlsx","sheet1")   
    x=df.loc[df["category"]==category]
    return x
#print(cat("food"))

def totalCat(categoryName): # Returns total sum in selected category
    x=totalAll(cat(categoryName))
    return x
#print(totalCat("food"))


def categoryData():
    import tkinter as tk

    categoryRoot=tk.Tk()
    categoryRoot.geometry("200x200")

    x=tk.StringVar()

    def click():
        b=totalAll(cat(x.get()))
        top=tk.Toplevel()
        top.title(x.get())
        label=tk.Label(top,text=b).pack(pady=30)  

    input=tk.Entry(categoryRoot,textvariable=x).pack(pady=30)
    temp=totalCat(x.get())
    button=tk.Button(categoryRoot,text="enter",command=click).pack(pady=30)

    categoryRoot.mainloop()
categoryData()