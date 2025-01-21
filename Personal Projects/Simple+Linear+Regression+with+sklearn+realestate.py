import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
sns.set()

from sklearn.linear_model import LinearRegression
data=pd.read_csv('C:\\Users\\santi\\Documents\\Python_Projects\\Training\\real_estate_price_size.csv')
x=data['size']
y=data['price']
x_matrix=x.values.reshape(-1,1) #make a matrix so SKlearn works properly
reg=LinearRegression()
reg.fit(x_matrix,y)
predict=pd.DataFrame(data=[750],columns=['size']) #Ask user to input SAT score to predict GPA score later
print(data.head())
print(predict.head())
print('R-squared:',reg.score(x_matrix,y)) #R-Squared
print('Coefficients:',reg.coef_) #Coefficients = b1
print('Intercept:',reg.intercept_) #intercepts = b0
print('Your predicted GPA score is:',str(reg.predict(predict)))
plt.scatter(x,y)
yhat=223.1787*x+1.019e+05
fg=plt.plot(x,yhat,c='orange',label='regression line')
plt.xlabel('size',fontsize=20)
plt.ylabel('price',fontsize=20)
plt.show()
