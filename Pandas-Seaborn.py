import numpy as np
import pandas as pd
import seaborn as sns


print("Example 1")

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

print("Example 2")

data = pd.DataFrame({
						'Country':['IND','AU','USA','CAN'],

	                  	 'Age':[23,27,20,34]

	                   },

	                   index=['Person1','Person2','Person3','Person4'])

print(data.loc[	['Person1','Person4'],['Country']])    

# Here in iloc we have to use integer indexes instead of string or char
print(data.iloc[[0,3],[0]])

## Boolean queries

print("Example 3")
var1 = pd.Series(['a','b','c','d','e'])
var2 = pd.Series([False,True,True,False,True])

print(var1[var2])

#
print("Example 3.1 querying")

#seaborn comes with a default data of titanic passengers

titanic = sns.load_dataset('titanic')

# print Passesngers with gender male, age<35 and pclass 2
print(titanic[(titanic.sex=='male')&(titanic.age<35)&(titanic.pclass==2)])

# Alignment : Label are important not the order.

a1 = pd.Series([200,300,400,np.nan], index=['a','b','c','d'])
a2= pd.Series([40,150,310,100], index=['a','g','c','d'])

print(a1.add(a2))

print(a1.align(a2))