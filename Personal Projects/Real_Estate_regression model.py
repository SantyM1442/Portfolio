import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

data=pd.read_csv('C:\\Users\\santi\\Documents\\Python_Projects\\Training\\real_estate_price_size.csv')

y=data['price']
x1=data['size']

plt.scatter(x1,y)
plt.xlabel('size',fontsize=20)
plt.ylabel('price',fontsize=20)
plt.show()
x=sm.add_constant(x1)
results=sm.OLS(y,x).fit()
print(results.summary())
plt.scatter(x1,y)
yhat=223.1787*x1+1.019e+05
fg=plt.plot(x1,yhat,c='orange',label='regression line')
plt.xlabel('size',fontsize=20)
plt.ylabel('price',fontsize=20)
plt.show()