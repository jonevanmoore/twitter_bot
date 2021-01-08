import tweepy
from time import sleep
from random import choice

#create a list of tweets you want to execute

tweet_list = ["tweet1", "tweet2", "tweet3", "etc."]


#Twitter information to access your profile

consumer_key = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
consumer_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
access_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
access_token_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


#Executing Tweets

for tl in tweet_list:
    tweet = api.update_status(choice(tweet_list))
    print(tweet)
    #Tweet every 2 hours
    sleep(7200)
