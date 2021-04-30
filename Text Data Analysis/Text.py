import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

comments= pd.read_csv("D:/Project/Youtube Analysis/GBcomments.csv", error_bad_lines=False)
print(comments)
print(comments.head())

from textblob import TextBlob
T=TextBlob("Its more accurate to call it the M+ (1000) be..").sentiment.polarity
print(T)
null_values=comments.isna().sum()
print(null_values)
drop=comments.dropna(inplace=True)
print(drop)

polarity=[]
for i in comments["comment_text"]:
    polarity.append(TextBlob(i).sentiment.polarity)
