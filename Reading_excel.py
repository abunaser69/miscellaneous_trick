import pandas as pd
from pandas import ExcelWriter
import pandas as pd
import numpy as np
import chart_studio.plotly as py
import cufflinks as cf
import seaborn as sns
import plotly.express as px
from matplotlib import colors
import matplotlib.pyplot as plt
#from string import count
from string import *
%matplotlib inline

#Setting for plotly
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)
cf.go_offline()

#dataframe display settings
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_rows', None)

import xlrd
xls = xlrd.open_workbook(r'name.xlsx', on_demand=True)
print(xls.sheet_names()) # <- remeber: xlrd sheet_names is a function, not a property

xl = pd.ExcelFile('name.xlsx')
print(xl.sheet_names)

#reading all the sheets as dictionaly
d = {} # your dict.
for sheet in xl.sheet_names:
    d[f'{sheet}']= pd.read_excel(xl, sheet_name=sheet, header=3)
    
col1_col2_drop=d['col1, col2'].drop(labels=range(39, 54), axis=0)

#data shape and type
col1_col2_drop.shape
col1_col2_drop.dtypes
col1_col2_drop.select_dtypes('object').head()
col1_col2_drop.select_dtypes('number').head()

#Printing group by object
for key, item in scotland:
    print("Key is: " + str(key))
    print(str(item), "\n\n")
    
scotland.boxplot(subplots=False, rot=90, fontsize=12)

#groupby object to table
scotland.apply(lambda a: a[:])

#groupby to dataframe 
scot_df = scotland.apply(lambda a: a.drop(['col1 code', 'col1 name'], axis=1)).reset_index(drop=True)

#plotting 
scot_df.plot(kind='line',figsize=(15,10), legend=True, x='Direction', title='Scotland')




