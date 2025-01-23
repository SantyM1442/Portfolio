from time import process_time

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
sns.set()

from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import f_regression
from sklearn.preprocessing import StandardScaler
data=pd.read_csv('C:\\Users\\santi\\Documents\\Python_Projects\\Training\\1.02.+Multiple+linear+regression.csv')

x=data[['SAT','Rand 1,2,3']] #dependent variables
y=data['GPA'] #independent variables
scaler=StandardScaler()
scaler.fit(x)
x_scaled=scaler.transform(x)

reg=LinearRegression()
reg.fit(x_scaled,y) #generate model
adj_r_squared=1-(1-reg.score(x,y))*((x.shape[0]-1)/(x.shape[0]-x.shape[1]-1)) #calculate adj r2
new_data=pd.DataFrame(data=[[1700,2],[1800,1]],columns=['SAT','Rand 1,2,3'])
new_data_scaled=scaler.transform(new_data)
reg_summary=pd.DataFrame([['Bias'],['SAT'],['Rand 1,2,3']], columns=['Features'])
reg_summary['Weights']=reg.intercept_,reg.coef_[0],reg.coef_[1]
print(reg.predict(new_data_scaled))
print('R-Squared:',reg.score(x,y))
print('Adjusted R-Squared:',adj_r_squared)
print(reg_summary)

