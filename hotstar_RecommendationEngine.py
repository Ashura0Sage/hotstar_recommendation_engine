#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os


# In[2]:


os.getcwd()


# In[3]:


os.chdir('C:/Users/anike/Downloads/hack_datasets/Datasets/Problem 4')


# In[22]:


import pandas as pd
import time
import numpy as np


# In[57]:


start = time.time()
df = pd.read_json('train_data.json',orient = 'index')
end = time.time()
print(end - start)
#df = df.T


# In[58]:


df.head()


# In[63]:


df.to_pickle('dummy.pkl')
df = df.iloc[:500]

df['index'] = df.index


# In[65]:


df['user'] = df['index'].str.replace('train-',' ')


# In[66]:


df = df.drop('index',1)


# In[67]:


df.head()


# In[68]:


df.shape


# In[69]:


df.reset_index(level=0,inplace = True)


# In[70]:


df.head()


# In[71]:


df = df.drop('index',1)


# In[72]:


df.head()


# In[73]:


df.shape


# In[74]:


user1_cities = df['cities'][1]
user2_cities = df['cities'][2]
# user1_cities = user1_cities.split(',')
# user2_cities = user2_cities.split(',')


# In[75]:


user1_cities


# In[89]:


for x in user1_cities.split(','):
    print(x) 


# In[90]:


cities = df['cities'].values.tolist()


# In[91]:


user1_city = cities[0].split(',')


# In[97]:


user1_city


# In[88]:





# In[ ]:




