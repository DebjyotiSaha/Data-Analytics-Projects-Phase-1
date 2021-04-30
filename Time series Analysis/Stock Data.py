#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


path='D:\Project\Time series Analysis\individual_stocks_5yr-20210209T115530Z-001\individual_stocks_5yr'
company_list=['AAPL_data.csv', 'GOOG_data.csv', 'MSFT_data.csv', 'AMZN_data.csv']
all_data=pd.DataFrame()
for file in company_list:
    current_df=pd.read_csv(path+'/'+file)
    all_data=pd.concat([all_data, current_df])
all_data.shape


# In[3]:


all_data.head()


# In[4]:


tech_list=all_data['Name'].unique()


# In[5]:


all_data.dtypes


# In[6]:


all_data['date']=pd.to_datetime(all_data['date'])


# In[7]:


all_data.dtypes


# In[8]:


plt.figure(figsize=(20,12))
for i, company in enumerate(tech_list,1):
    plt.subplot(2,2,i)
    df=all_data[all_data['Name']==company]
    plt.plot(df['date'], df['close'])
    plt.xticks(rotation='vertical')
    plt.title(company)
    plt.show()


# In[9]:


import plotly.express as px


# In[10]:


for comapny in tech_list:
    df=all_data[all_data['Name']==comapny]
    fig=px.line(df, x='date', y='volume', title=company)
    fig.show()


# In[11]:


df=pd.read_csv("D:\Project\Time series Analysis\individual_stocks_5yr-20210209T115530Z-001\individual_stocks_5yr/AAPL_data.csv")


# In[12]:


df.head()


# In[13]:


df['Daily_Price_change']=df['close']-df['open']


# In[14]:


df.head()


# In[15]:


df['1day % return']=((df['close']-df['open'])/df['close'])*100


# In[16]:


df.head()


# In[17]:


fig=px.line(df, x='date', y='1day % return', title=company)
fig.show()


# In[18]:


df2=df.copy()


# In[19]:


df2.dtypes


# In[20]:


df2['date']=pd.to_datetime(df2['date'])


# In[21]:


df2.set_index('date', inplace=True)


# In[22]:


df2.head()


# In[23]:


df2['2013-02-08':'2013-02-14']


# In[25]:


df2['close'].resample('M').mean().plot()


# In[27]:


df2['close'].resample('Y').mean().plot(kind='bar')


# In[28]:


aapl=pd.read_csv('D:\Project\Time series Analysis\individual_stocks_5yr-20210209T115530Z-001\individual_stocks_5yr/AAPL_data.csv')
aapl.head()


# In[30]:


amzn=pd.read_csv('D:\Project\Time series Analysis\individual_stocks_5yr-20210209T115530Z-001\individual_stocks_5yr/AMZN_data.csv')
amzn.head()                


# In[31]:


msft=pd.read_csv('D:\Project\Time series Analysis\individual_stocks_5yr-20210209T115530Z-001\individual_stocks_5yr/MSFT_data.csv')
msft.head()


# In[32]:


goog=pd.read_csv('D:\Project\Time series Analysis\individual_stocks_5yr-20210209T115530Z-001\individual_stocks_5yr/GOOG_data.csv')
goog.head()


# In[33]:


close=pd.DataFrame()


# In[34]:


close['aapl']=aapl['close']
close['goog']=goog['close']
close['amzn']=amzn['close']
close['msft']=msft['close']


# In[35]:


close.head()


# In[37]:


import seaborn as sns


# In[38]:


sns.pairplot(data=close)


# In[40]:


sns.heatmap(close.corr(), annot=True)


# In[ ]:


#Daily return of my stock


# In[41]:


aapl.head()


# In[42]:


data=pd.DataFrame()


# In[44]:


data['aapl_change']=((aapl['close']-aapl['open'])/aapl['close'])*100
data['goog_change']=((goog['close']-goog['open'])/goog['close'])*100
data['amzn_change']=((amzn['close']-amzn['open'])/amzn['close'])*100
data['msft_change']=((msft['close']-msft['open'])/msft['close'])*100


# In[45]:


data.head()


# In[46]:


sns.pairplot(data=data)


# In[48]:


sns.heatmap(data.corr(), annot=True)


# In[49]:


sns.distplot(data['aapl_change'])


# In[50]:


data['aapl_change'].std()
#68%


# In[51]:


data['aapl_change'].std()*2
#95%


# In[52]:


data['aapl_change'].std()*3
#99%


# In[53]:


data['aapl_change'].quantile(0.1)


# In[54]:


data.describe().T


# In[ ]:




