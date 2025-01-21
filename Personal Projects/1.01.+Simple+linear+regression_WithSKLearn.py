import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
sns.set()

from sklearn.linear_model import LinearRegression
data=pd.read_csv('C:\\Users\\santi\\Documents\\Python_Projects\\Training\\1.01.+Simple+linear+regression.csv')
x=data['SAT']
y=data['GPA']
x_matrix=x.values.reshape(-1,1) #make a matrix so SKlearn works properly
reg=LinearRegression()
reg.fit(x_matrix,y)
num=pd.DataFrame(data=[int(input('What SAT score do you have?')),int(input('What SAT score do you have?'))],columns=['SAT']) #Ask user to imput SAT score to predict GPA score later
print(num.head())
print('R-squared:',reg.score(x_matrix,y)) #R-Squared
print('Coefficients:',reg.coef_) #Coefficients = b1
print('Intercept:',reg.intercept_) #intercepts = b0
print('Your predicted GPA score is:',str(reg.predict(num)))
num['Predicted_GPA']=reg.predict(num)
print(num.head())
