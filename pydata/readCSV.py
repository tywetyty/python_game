#enconding=utf-8
from pandas import DataFrame,Series
import pandas as pd
import numpy as np
names=['a','b','c','massage']
df =pd.read_csv('unit.csv',names=names,index_col='massage')
print df
df.to_csv('out1.csv')