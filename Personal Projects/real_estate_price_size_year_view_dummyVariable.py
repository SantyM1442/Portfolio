import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
sns.set()
raw_data=pd.read_csv('C:\\Users\\santi\\Documents\\Python_Projects\\Training\\real_estate_price_size_year_view.csv')
data=raw_data.copy()
data['view']=data['view'].map({'Sea view':1,'No sea view':0})
y=data['price']
x1=data[["size",'year','view']]
x=sm.add_constant(x1)
results=sm.OLS(y,x).fit()
print(results.summary())
