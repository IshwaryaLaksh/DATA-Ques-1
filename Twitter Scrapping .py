#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip3 install snscrape')


# In[9]:



import snscrape.modules.twitter as sntwitter
import pandas as pd

# Creating list to append tweet data to
tweets_list2 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('RONALDO since:2022-11-01 until:2023-01-24').get_items()):
    if i>50:
        break
    tweets_list2.append([tweet.date, tweet.id, tweet.content, tweet.user.username, tweet.url])
    
# Creating a dataframe from the tweets list above
tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime', 'Tweet Id', 'Text', 'Username', 'URL'])
tweets_df2


# In[ ]:




