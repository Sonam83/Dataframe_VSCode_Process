# Step 1: Initially, in command prompt : pip install pandas
#Step 2 : Below Code logic



import pandas as pd 

# ------------------ Way 1 : Direct Creation -------------------------------------

data={"Name":["Sonam","Innomatics","Roshni","Shubham","Siddharth"],
"Age":[22,45,78,54,21],
"Gender":["Female","Male","Female","Male","Female"],
"Salary":[80000,56000,34000,45397,57218]}

df=pd.DataFrame(data)
#print(df) ------------------ Step 3 : In terminal, run as python dataframe_1.py


# --------------------- way 2 : with one columns(list) -------------------------------------
data2=pd.DataFrame(["Hyderabad","Pune","Mumbai","Chicago","St.Louis"],columns=["City"])
#print(data2)

# ---------------------- way 3 : with >1 column(list of lists) -----------------------------------------
data3=pd.DataFrame([["India",22,453.98],["China",23,876.90],["Switzerland",67,786.9],["Denmark",56,908],["Australia",68,8786]],
columns=[["Country",'Value',"Number"]]) 
#print(data3)

# ------------------------ way 4 : list of lists directly -------------------------------
d=[["India",22,453.98],["China",23,876.90],["Switzerland",67,786.9],["Denmark",56,908],["Australia",68,8786]]
data4=pd.DataFrame(d)
print(data4)

# using columns
data5=pd.DataFrame(d,columns=["val1","val2","val3"])
print(data5)

# ------------------------ way 5 : read operation -----------------------------------
#data6=pd.read_csv(r'path')
#data7=pd.read_excel(r'path')

