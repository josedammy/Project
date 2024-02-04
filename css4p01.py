#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 22:44:20 2024

@author: josedam
"""

import pandas as pd
df = pd.read_csv("movie_dataset.csv")
print(df.info())


print(df.columns)

avg_cal = df["Revenue (Millions)"].mean()

avg_cal2 = df["Metascore"].mean()


df["Revenue (Millions)"].fillna(avg_cal, inplace = True)

df["Metascore"].fillna(avg_cal2, inplace = True)
print(df.info())


#df = df[df["Actors"] == "Mark Wahberg"]

#df = df[df['Year']>2007]



#The highest rated movie is obtained by filtering all ratings greater than 8.9

#df = df[df['Rating']>7.9]

#avg_rev = df["Revenue (Millions)"].mean()
#print(avg_rev