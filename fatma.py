#!/usr/bin/env python
# coding: utf-8

# # Task 2

# In[1]:


import pandas as pd

import numpy as np


# In[2]:


ar = np.arange(100).reshape((10,10))

df = pd.DataFrame(ar,columns=['F','A','T','M','A','A','L','Z','H','A'])
df.index = ['A', 'L', 'Y', 'S','a', 'L', 'E', 'M','A', 'L']
df


# In[3]:


df.to_csv('x.csv')
df1 = pd.read_csv('x.csv', index_col=0)
df1


# In[4]:


print("df size :",df.size)
print('df shape :',df.shape)
print('df index :',df.index)
print('df columns :',df.columns)


# In[5]:


df[['A']]


# In[6]:


df['Z'] = (df['F']+20)/30.5
df


# In[7]:


df.iloc[0 , 1] = np.nan
df.iloc[1 , 2] = np.nan
df.iloc[2 , 3] = np.nan
df.iloc[3 , 4] = np.nan
df.iloc[4 , 5] = np.nan
df.iloc[5 , 6] = np.nan
df.iloc[6 , 1] = np.nan
df.iloc[5 , 2] = np.nan
df.iloc[7 , 3] = np.nan
df.iloc[4 , 4] = np.nan
df.iloc[0 , 5] = np.nan
df.iloc[0 , 6] = np.nan
df.iloc[9 , 7] = np.nan
df.iloc[8 , 8] = np.nan
df.iloc[0 , 9] = np.nan
df.iloc[0 , 0] = np.nan
df.iloc[9 ,0 ] = np.nan
df


# In[8]:


df = df.drop(['H'], axis=1)


# In[9]:


df


# In[10]:


df=df.drop(['A'] )
df


# In[11]:


df = df /55
df


# In[12]:


booldf = df> 0.08
booldf


# In[13]:


df.loc["L"]


# In[14]:


df.iloc[7] 


# In[15]:


df[1:]


# In[16]:


df.iloc[2:4]


# In[17]:


df.mean()


# In[18]:


df[df > df.mean()]


# In[19]:


df.median()


# In[20]:


df2 = 1 - df % 2
df2


# In[21]:


df2=df2<0
df2


# In[22]:


df.mean(axis=0)


# In[23]:


df.mean(axis=1)


# In[24]:


df.describe()


# In[25]:


df.describe().T


# In[26]:


df


# In[27]:


df.head(4)


# In[28]:


df.tail()


# In[29]:


df.sample()


# In[30]:


df.head(6).style.background_gradient(cmap='Reds')


# In[31]:


df.shape


# In[32]:


df.columns


# In[33]:


df.info()


# In[34]:


df.isnull()


# In[35]:


df.isnull().sum()


# In[36]:


df.isna()


# In[37]:


df.isna().sum()


# In[38]:


df.nunique().sum()


# In[39]:


df.nunique()


# In[40]:


len(df['Z'].unique())


# In[41]:


df.fillna(df.mean(), inplace=True)


# In[42]:


df


# In[43]:


df.isnull().sum()


# In[44]:


df.tail().style.background_gradient(cmap='Reds')


# In[45]:


x = np.random.rand(60)
y = np.random.rand(60)

df = pd.DataFrame(np.array([x, y]).T, columns=['a', 'b'])
df.plot.hist()


# In[46]:


x = np.random.rand(10)
y = np.random.rand(10)

df = pd.DataFrame(np.array([x, y]).T, columns=['a', 'b'])
df.plot.bar()


# In[47]:


x = np.random.rand(40)
y = np.random.rand(40)

df = pd.DataFrame(np.array([x, y]).T, columns=['a', 'b'])
df.plot()


# In[48]:


ar = np.arange(100).reshape((10,10))

df = pd.DataFrame(ar,columns=['F','A','T','M','A','A','L','Z','H','A'])
df.index = ['A', 'L', 'Y', 'S','a', 'L', 'E', 'M','A', 'L']
df.head(10).style.background_gradient(cmap='Reds')


# In[ ]:





# In[ ]:




