from time import process_time

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
sns.set()

from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import f_regression
data=pd.read_csv('C:\\Users\\santi\\Documents\\Python_Projects\\Training\\real_estate_price_size_year.csv')

x=data[['size','year']] #dependent variables
y=data['price'] #independent variables
reg=LinearRegression()
reg.fit(x,y) #generate model
adj_r_squared=1-(1-reg.score(x,y))*((x.shape[0]-1)/(x.shape[0]-x.shape[1]-1)) #calculate adj r2
f_regression(x,y)
p_values=f_regression(x,y)[1]

reg_summary=pd.DataFrame(data=x.columns.values, columns=['Features'])
reg_summary['Coefficients']=reg.coef_
reg_summary['P-Values']=p_values.round(3)
print(reg.predict([[750,2009]]))
print('Intercept:',reg.intercept_)
print('R-Squared:',reg.score(x,y))
print('Adjusted R-Squared:',adj_r_squared)
print(reg_summary)

