# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 10:29:10 2018

@author: Jahanzaib Malik
"""

import numpy as np
import pandas as pd

#Reading File
data = pd.read_csv('DOS2012.csv')
data = np.array(data)

#Identifying row and columns
rows = len(data)
columns = len(data[0])
old_rows = rows
x=0

#Removing NaN and Infinity
for r in range(0,rows):
    for c in range(0,columns):
        if(data[r][c]=='NaN'):
            data = np.delete(data,(r),axis=0)
            x=x+1
            print('{0}. Eliminated: [{1},{2}]'.format(x,r, c))
    
        elif(data[r][c]=="Infinity"):
            data = np.delete(data,(r),axis=0)
            x=x+1
            print('{0}. Eliminated: [{1},{2}]'.format(x,r, c))
        elif(data[r][c]=="infinity"):
            data = np.delete(data,(r),axis=0)
            x=x+1
            print('{0}. Eliminated: [{1},{2}]'.format(x,r, c))

            
#Analyzing old and new records (How Much Emliminated Records)
print(old_rows)
new_rows = len(data)
print(new_rows)
print('Total Records Eliminated:{0} '.format(old_rows-new_rows))            



#Saving Filtred File
data = pd.DataFrame(data)
data.to_csv('DOS2012.csv', index=False)  

          
            