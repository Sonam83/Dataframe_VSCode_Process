import pandas as pd 
from sklearn.preprocessing import LabelEncoder, StandardScaler 
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report 

data={'Age': [25, 30, 28, 35, 24, 40, 27, 32],
    'MonthlyIncome': [30000, 50000, 45000, 70000, 28000, 90000, 42000, 60000],
    'YearsAtCompany': [1, 5, 3, 7, 1, 10, 2, 6],
    'JobRole': ['Developer', 'Tester', 'HR', 'Manager',
                'Support', 'Manager', 'Developer', 'Tester'],
    'Attrition': ['Yes', 'No', 'No', 'No',
                  'Yes', 'No', 'Yes', 'No']}

df=pd.DataFrame(data)
print("Original Dataset : ")
print(df)

jle=LabelEncoder() # Labelencoder one col at a time, ohe or ordinal encoding can perform multiple columns at a time
df["JobRole"]=jle.fit_transform(df["JobRole"])

print(jle.classes_)
print("\n Encoded dataframe is : ")
print(df)

ale=LabelEncoder()
df["Attrition"]=ale.fit_transform(df["Attrition"]) #fit learns mapping the data, transform converts the data on learnt mapping
print(df)

X=df.drop('Attrition',axis=1)
y=df['Attrition']

print("Features are : ")
print(X)

print("Target is : ")
print(y)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
print("Train Data")
print(X_train)
print(y_train)

print("Test Data")
print(X_test)
print(y_test)

model=RandomForestClassifier(n_estimators=100,random_state=42) # estimators = 100
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
print("New prediction is ")
print(y_pred)

acc=accuracy_score(y_test,y_pred) 
print(acc)

cr=classification_report(y_test,y_pred)
print(cr)


feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': model.feature_importances_
})

print(feature_importance)

new_employee = pd.DataFrame({
    'Age': [29],
    'MonthlyIncome': [55000],
    'YearsAtCompany': [4],
    'JobRole': [jle.transform(['Developer'])[0]] # transform expects list/array, returns list/array
})

prediction = model.predict(new_employee)
print("Prediction is : ")
print(prediction)

