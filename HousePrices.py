
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import pandas as pd
import datetime as dt
import seaborn as sns
from matplotlib import pyplot as plt

df = pd.read_csv('C:\\Users\\I867150\\Desktop\\HousePrices\\kc_house_data.csv')

df.drop('id', axis=1, inplace=True)
tmp = pd.to_datetime(df['date'])
date_ord = []
for date in tmp:
    date_ord.append(dt.datetime.toordinal(date))
df.insert(1,'date_ord',date_ord)
df.drop('date',axis=1, inplace =True)
df.drop('lat', axis = 1, inplace = True)
df.drop('long', axis = 1, inplace = True)

reg_model = smf.ols('price~bedrooms+bathrooms+sqft_living+sqft_lot+C(waterfront)+C(view)+C(grade)+yr_built+C(zipcode)', data=df).fit()


#sns.residplot(reg_model.resid.index.values, reg_model.resid, lowess=True, color="g")
#plt.show()

print(reg_model.summary())