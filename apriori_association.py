# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 13:47:43 2019

@author: hp
"""

#IMPORT THE LIBRARIES
import pandas as pd
import matplotlib.pyplot as plt

#IMPORT THE DATASET
dataset=pd.read_csv('Market_Basket_Optimisation.csv',header=None)
transaction=[]
for i in range(0,7501):
    transaction.append([str(dataset.values[i,j])for j in range(0,20)])
    
#TRAINING DATASET USING APRIORI
from apyori import apriori
rules=apriori(transaction,min_support=0.003,min_confidence=0.2,min_lift=3,min_length=2)

#viewing the result
results=list(rules)
