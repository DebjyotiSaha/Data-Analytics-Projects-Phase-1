#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


# In[2]:


files=[file for file in os.listdir('D:\Project\Sales Data Analysis')]
for file in files:
    print(file)


# In[3]:


path='D:\Project\Sales Data Analysis'
all_data=pd.DataFrame()

for file in files:
    current_df=pd.read_csv(path+"/"+file)
    all_data=pd.concat([all_data, current_df])

all_data.shape


# In[4]:


all_data=pd.read_csv('D:\Project\Sales Data Analysis/all_data.csv')
all_data.head()


# In[5]:


all_data.isnull().sum()


# In[6]:


all_data=all_data.dropna(how='all')
all_data.shape


# In[7]:


'04/19/19 08:46'.split('/')[0]


# In[8]:


def month(x):
    return x.split('/')[0]


# In[9]:


all_data['month']=all_data['Order Date'].apply(month)


# In[10]:


all_data.head()


# In[11]:


all_data.dtypes


# In[12]:


all_data['month']=all_data['month'].astype(int)


# In[13]:


all_data['month'].unique()


# In[14]:


filter=all_data['month']=='Order Date'
all_data=all_data[-filter]
all_data.head()


# In[15]:


all_data['month']=all_data['month'].astype(int)


# In[16]:


all_data['Quantity Ordered']=all_data['Quantity Ordered'].astype(int)
all_data['Price Each']=all_data['Price Each'].astype(float)


# In[17]:


all_data.dtypes


# In[18]:


all_data['Sales']=all_data['Price Each']*all_data['Quantity Ordered']


# In[19]:


all_data.head()


# In[20]:


all_data.groupby('month')['Sales'].sum()


# In[21]:


month=range(1,13)
plt.bar(month, all_data.groupby('month')['Sales'].sum())
plt.xticks(month)


# In[22]:


all_data.head()


# In[23]:


'917 1st St, Dallas, TX 75001'.split(',')[1]


# In[24]:


def city(x):
    return x.split(',')[1]


# In[25]:


all_data['city']=all_data['Purchase Address'].apply(city)


# In[26]:


all_data.head()


# In[27]:


all_data.groupby('city')['city'].count().plot.bar()


# In[28]:


all_data['Order Date'].dtype


# In[29]:


all_data['Hour']=pd.to_datetime(all_data['Order Date']).dt.hour


# In[30]:


all_data.head()


# In[31]:


keys=[]
hour=[]
for key, hour_df in all_data.groupby('Hour'):
    keys.append(key)
    hour.append(len(hour_df))


# In[32]:


keys


# In[33]:


hour


# In[34]:


plt.grid()
plt.plot(keys, hour)


# In[36]:


all_data.groupby('Product')['Quantity Ordered'].sum()


# In[37]:


all_data.groupby('Product')['Quantity Ordered'].sum().plot(kind='bar')


# In[38]:


all_data.groupby('Product')['Price Each'].mean()


# In[39]:


products=all_data.groupby('Product')['Quantity Ordered'].sum().index
quantity=all_data.groupby('Product')['Quantity Ordered'].sum()
prices=all_data.groupby('Product')['Price Each'].sum()


# In[41]:


fig, ax1=plt.subplots()
ax2=ax1.twinx()
ax1.bar(products, quantity, color='g')
ax2.plot(products, prices)
ax1.set_xticklabels(products, rotation='vertical', size=8)


# In[42]:


all_data.head()


# In[44]:


df=all_data['Order ID'].duplicated(keep=False)
df2=all_data[df]
df2.head()


# In[47]:


df2['Grouped']=df2.groupby('Order ID')['Product'].transform(lambda x:','.join(x))


# In[48]:


df2.head()


# In[49]:


df2=df2.drop_duplicates(subset=['Order ID'])
df2.head()


# In[50]:


df2['Grouped'].value_counts()[0:5].plot.pie()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




