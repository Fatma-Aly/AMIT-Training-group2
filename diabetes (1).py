#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import libraries 
import numpy as np
import pandas as pd #to read csv file 
import matplotlib.pyplot as plt
import seaborn as sns


# In[23]:


#load csv file (diabetes.csv)
df = pd.read_csv('diabetes.csv')


# In[3]:


#showing frist 5 rows of dataframe
df.head()


# In[4]:


#coulmns names 
df.columns


# In[5]:


#get data types for each coulmn and number of Non-Null Count
df.info()


# In[6]:


#sum of null values in each coulmn of dataframe
df.isnull().sum()


# In[7]:


#mean,3Quartears of each coulmns
df.describe ()


# In[8]:


df


# In[9]:


df.groupby('Outcome').mean()


# In[10]:


df.groupby('Outcome').median()


# In[76]:


df['Pregnancies'].value_counts() 


# In[12]:


#number of uniqye values in Pregnancies coulmn
df['Pregnancies'].nunique()


# In[29]:


x=[]
for i in range(len(df["Outcome"])):
    if df["Outcome"][i]==1:
        x.append('Diabetic')
    if  df["Outcome"][i]==0:
        x.append('Non Diabetic')




# In[20]:


plt.bar(df["Outcome"] ,df["Pregnancies"])
plt.xticks(df["Outcome"] ,x )
plt.xlabel('Outcome')
plt.ylabel('Pregnancies')
plt.title('Pregnancies vs Outcome')
plt.xticks(df["Outcome"])
plt.show()


# In[30]:


df


# In[51]:


width=0.3
plt.bar(df["Outcome"],df["Glucose"], width , color='r', label='Glucose')
plt.bar(df["Outcome"]+ width,df["Insulin"], width, color='g', label='Insulin')
plt.bar(df["Outcome"]+ 2*width,df["BloodPressure"], width, color='b', label='BloodPressure')
plt.xticks(df["Outcome"]+width,x)
plt.legend()
plt.show()


# In[53]:


sns.displot(df['Age'], color='b',height=5,aspect=1.2 )
plt.show()


# In[54]:


sns.displot(df['Age'], color='b',kde =True,height=5,aspect=1.2)
plt.show()


# In[63]:


sns.displot(df['Pregnancies'],kde = False, color='b',height=8,aspect=0.6)
plt.show()


# In[66]:


sns.displot(df['BMI'],kde = False, color='c',height=8,aspect=0.6)
plt.show()


# In[70]:


sns.displot(df.BloodPressure, color='r',kde =True,height=10,aspect=1.5)


# In[105]:


plt.figure(figsize=(12,6))
sns.heatmap(df.corr(), cmap="Blues",annot=True);


# In[106]:


df['Outcome'].value_counts()
plt.figure(figsize=(7,7))

plt.pie(df['Outcome'].value_counts(),labels=['Non-diabetic','Diabetic'],radius=1,
        autopct='%1.1f%%',explode = [0,0.1],labeldistance=1.15,startangle = 90)

plt.legend(title = 'Outcome:',loc='upper right', bbox_to_anchor=(1.6,1))
plt.show()


# In[98]:


df2['BMI'].value_counts()


# In[99]:


df2['BMI'].mean()


# In[96]:


df2['Pregnancies'].value_counts()
 


# In[14]:


df.hist(figsize=(20, 20) ,bins = 45, color='g' ,alpha = 1)
plt.show()


# In[110]:


df


# In[112]:


#outliers 
sns.set(style="whitegrid")
df.boxplot(figsize=(15,6))
plt.show()


# In[ ]:




