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

