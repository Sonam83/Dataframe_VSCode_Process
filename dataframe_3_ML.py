# step 0 : In new terminal - command prompt - install libraries(pip install pandas, pip install scikit-learn)

# step 1 : Import Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# step 2: Creating data manually
data={'Age':[25,30,35,40,28,32,45,50],
      'Salary':[50000,60000,65000,80000,52000,58000,90000,100000],
      'Gender':['Male','Female','Female','Male','Female','Male','Male','Female'],
      'Purchased':[0,1,1,1,0,0,1,1]}

# step 3 : creating dataframe
df=pd.DataFrame(data)
print(df) # in command prompt run : python dataframe_3_ML.py

# step 4 : encode gender column
le=LabelEncoder()
df['Gender']=le.fit_transform(df['Gender'])
print("\n Encoded dataframe : ")
print(df)

# step 5 : split features and target
X=df[['Age','Salary','Gender']]
y=df['Purchased']

# step 6 : Train - test - split
X_train, X_test, y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

# step 7 : feature scaling
scaler=StandardScaler()
X_train[['Age','Salary']]=scaler.fit_transform(X_train[['Age','Salary']]) # on train data to avoid data leakage
X_test[['Age','Salary']]=scaler.transform(X_test[['Age','Salary']]) #on test data

# step 8 : logistic regression model
model=LogisticRegression()
model.fit(X_train,y_train)

y_pred=model.predict(X_test)
print(y_pred)

# new query for prediction
query={'Age':[30],'Salary':[70000],'Gender':['Female']}
new_data=pd.DataFrame(query)
new_data['Gender']=le.transform(new_data['Gender'])
new_data[['Age','Salary']]=scaler.transform(new_data[['Age','Salary']])
prediction=model.predict(new_data)

print("New query prediction")
print(prediction)

# Step 9 : Evluation
acc=accuracy_score(y_test,y_pred)
print(acc)

cm=confusion_matrix(y_test,y_pred)
print(cm)