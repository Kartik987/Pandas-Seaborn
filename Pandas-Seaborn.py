import numpy as np
import pandas as pd
import seaborn as sns


list = [1,2,3,4,5,6,7,8,9,10]

ser =pd.Series(list)

print(ser)
print(ser[:6])
# Position based accessing
print(ser[1:6])
# index based accessing
print(ser[6])
print(ser.head())
print(ser.head(5))

# Working of iloc and loc in indexing
name = [1,2,3,4,5,6]

data = pd.DataFrame({
						'Country':['IND','AU','USA','CAN'],

	                  	 'Age':[23,27,20,34]

	                   },

	                   index=['Person1','Person2','Person3','Person4'])

print(data.loc[	['Person1','Person4'],['Country']])    

# Here in iloc we have to use integer indexes instead of string or char
print(data.iloc[[0,3],[0]])

