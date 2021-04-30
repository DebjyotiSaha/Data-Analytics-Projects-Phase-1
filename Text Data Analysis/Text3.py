#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[ ]:


#perform sentiment analysis, positive and negative comments


# In[2]:


comments= pd.read_csv("D:/Project/Youtube Analysis/GBcomments.csv", error_bad_lines=False)
print(comments)
print(comments.head())


# In[3]:


from textblob import TextBlob
T=TextBlob("Its more accurate to call it the M+ (1000) be..").sentiment.polarity
print(T)
null_values=comments.isna().sum()
print(null_values)
drop=comments.dropna(inplace=True)
print(drop)


# In[4]:


polarity=[]
for i in comments["comment_text"]:
    polarity.append(TextBlob(i).sentiment.polarity)


# In[6]:


comments["polarity"]=polarity


# In[7]:


comments.head(20)


# In[7]:


comments_positive=comments[comments["polarity"]==1]


# In[8]:


comments_positive.shape


# In[9]:


comments_positive.head()


# In[10]:


from wordcloud import WordCloud, STOPWORDS


# In[11]:


stopwords=set(STOPWORDS)


# In[16]:


total_comments=' '.join(comments_positive["comment_text"])


# In[17]:


wordcloud=WordCloud(width=1000, height=500, stopwords=stopwords).generate(total_comments)


# In[18]:


plt.figure(figsize=(15,15))
plt.imshow(wordcloud)
plt.axis("off")


# In[23]:


comments_negative=comments[comments["polarity"]==-1]


# In[24]:


total_comments=' '.join(comments_negative['comment_text'])


# In[25]:


wordcloud=WordCloud(width=1000, height=500, stopwords=stopwords).generate(total_comments)


# In[26]:


plt.figure(figsize=(15,5))
plt.imshow(wordcloud)
plt.axis('off')


# In[ ]:


#Trending tags in youtube


# In[28]:


videos=pd.read_csv("D:\Project\Youtube Analysis/USvideos.csv", error_bad_lines=False)


# In[29]:


videos.head()


# In[32]:


tags_complete=' '.join(videos['tags'])


# In[33]:


tags_complete


# In[34]:


import re


# In[36]:


tags=re.sub('[^a-zA-Z]',' ', tags_complete)


# In[37]:


tags


# In[38]:


tags=re.sub(' +',' ', tags)


# In[39]:


wordcloud=WordCloud(width=1000, height=500, stopwords=set(STOPWORDS)).generate(tags)


# In[41]:


plt.figure(figsize=(15,5))
plt.imshow(wordcloud)
plt.axis('off')


# In[ ]:


#likes and dislikes in youtube


# In[42]:


sns.regplot(data=videos, x='views', y='likes')
plt.title('Regression plot for views and likes')


# In[43]:


sns.regplot(data=videos, x='views', y='dislikes')
plt.title('Regression plot for views and dislikes')


# In[ ]:


#How they are co-related?


# In[44]:


df_corr=videos[['views', 'likes', 'dislikes']]


# In[45]:


df_corr.corr()


# In[46]:


sns.heatmap(df_corr.corr(), annot=True)

