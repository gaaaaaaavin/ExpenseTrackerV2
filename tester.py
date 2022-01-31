import pandas as pd

catFileDF=pd.read_csv("logs\cat.txt")
#catFileDF=list(catFileDF)
print(catFileDF)
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
print(cat)
