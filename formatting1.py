# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 00:13:09 2017

@author: divyam
"""

import json
import time
import pandas as pd
tweets_filename = 'fetched_tweets.json'
tweets_file = open(tweets_filename, "r")
tweets_data=[]
df=pd.DataFrame();
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)    
df['created_at'] = list(map(lambda tweet: time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y')), tweets_data))
df['user'] = list(map(lambda tweet: tweet['user']['screen_name'], tweets_data))
print (df)
df.to_csv('fetched_df.csv')

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   