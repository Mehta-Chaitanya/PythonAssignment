# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 12:36:54 2021

@author: Khushi
"""
import pandas as pd
for i,chunk in enumerate(pd.read_csv('G:\PS\Sales.csv', chunksize=5000)):
    chunk.to_csv('G:\PS\chunk{}.csv'.format(i), index=False)
