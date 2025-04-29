#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import os 
df = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/drinks.csv')
df


# In[7]:


df.country.str.contains('India', na=False).sum() # count the number of movies that contain 'Star Wars' in their title


# In[9]:


df.groupby('continent').country.apply(lambda x: x.str.contains('India', na=False).sum())


# In[ ]:




