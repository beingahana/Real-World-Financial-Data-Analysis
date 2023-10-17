# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 20:19:36 2022

@author: Ahana Sarkar
"""

#importing Pandas
import pandas as pd

#Reading the CSV File
dataa = pd.read_csv("D:\\This PC\\Downloads\\Real World Financial Data Analysis\\Ecommerce Purchases.csv")
dataa

dataa.head(10)

dataa.tail(10)

dataa['CC Security Code'].dtype

dataa.isnull().sum()

len(dataa) #for rows

len(dataa.columns)
dataa.shape
dataa.info()

dataa["Purchase Price"].max()

dataa[["Purchase Price","Email"]].min()

dataa["Purchase Price"].mean()

len(dataa[dataa["Language"]=="fr"])

len(dataa[dataa["Job"].str.contains('engineer',case=False)])

dataa[dataa["IP Address"]=="24.140.33.94"]['Email']

len(dataa[(dataa["CC Provider"]=="Mastercard") & (dataa["Purchase Price"]>50)])

dataa[dataa["Credit Card"]==869968197049750]['Email']

len(dataa[dataa['AM or PM']=="AM"])

len(dataa[dataa['AM or PM']=="PM"])

dataa[dataa["CC Exp Date"].apply(lambda x: x[3:]=="20")]['Email'].head()

dataa["Email"].apply(lambda x: x.split('@')[1]).value_counts().head()

dataa[['Company','Purchase Price']].nlargest(5,'Purchase Price').head()

