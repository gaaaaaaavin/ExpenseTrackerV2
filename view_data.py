import pandas as pd
df=pd.read_csv("logs\exp_log.txt",sep="\t")    #converts .txt to .xlsx
df.to_excel("logs\exp_log.xlsx","sheet1")