import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
sns.set()
raw_data=pd.read_csv('C:\\Users\\santi\\Documents\\Python_Projects\\Training\\1.03.+Dummies.csv')
data=raw_data.copy()
data['Attendance']=data['Attendance'].map({'Yes':1,'No':0})
y=data['GPA']
x1=data[["SAT",'Attendance']]
x=sm.add_constant(x1)
results=sm.OLS(y,x).fit()
plt.scatter(data['SAT'],y)
yhat_no=0.6439+0.0014*data['SAT']
yhat_yes=0.8665+0.0014*data['SAT']
fig=plt.plot(data['SAT'],yhat_no,lw=2,c='#006837')
fig=plt.plot(data['SAT'],yhat_yes,lw=2,c='#a50026')
plt.xlabel('SAT',fontsize=20)
plt.ylabel('GPA',fontsize=20)
plt.show()