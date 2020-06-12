# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 14:36:00 2017

@author: divyam
"""



#Variables that contains the user credentials to access Twitter API 
from twitter import OAuth ,Twitter
import pandas as pd

#Setting up Twitter API

access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""
oauth = OAuth(access_token, access_token_secret,consumer_key,consumer_secret)



#This is a basic listener that just prints received tweets to stdout.
twitter = Twitter(auth=oauth)

#search = api.GetSearch(term='fakenews', lang='en', result_type='recent', count=100, max_id='')
tweets=twitter.search.tweets(q='fakenews')
with open('fetched_tweets_home.json','a') as tf:
            tf.write(tweets)

