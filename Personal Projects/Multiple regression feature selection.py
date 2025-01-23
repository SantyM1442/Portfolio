import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
sns.set()

from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import f_regression
data=pd.read_csv('C:\\Users\\santi\\Documents\\Python_Projects\\Training\\1.02.+Multiple+linear+regression.csv')

x=data[['SAT','Rand 1,2,3']] #dependent variables
y=data['GPA'] #independent variables
reg=LinearRegression()
reg.fit(x,y) #generate model
adj_r_squared=1-(1-reg.score(x,y))*((x.shape[0]-1)/(x.shape[0]-x.shape[1]-1)) #calculate adj r2
f_regression(x,y)
p_values=f_regression(x,y)[1]
print('P-Values:',p_values.round(3))
print('R-squared:',reg.score(x,y)) #R-Squared
print('Coefficients:',reg.coef_) #Coefficients = b1
print('Intercept:',reg.intercept_) #intercepts = b0
print('Adjusted R-squared:',adj_r_squared) #Adjusted R-Squared

