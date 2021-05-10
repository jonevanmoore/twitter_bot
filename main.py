import tweepy
from time import sleep
from random import choice
from hn_lists_dicts import human_nature_accounts, human_nature_without, human_nature_dict, birthday, psych
from affiliates import affiliate_links
import engaging_accounts

#Get your keys from the Twitter developer site
#https://developer.twitter.com/
consumer_key = 'XXXXX'
consumer_secret = 'XXXXX'
access_token = 'XXXXX'
access_token_secret = 'XXXX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


#Executing Tweets

#This will wish authors happy birthday while tweeting their best quotes
used_bday_quotes = []
def birthday_boy():
    from datetime import date

    date = date.today()
    today = f"{date.month}-{date.day}"

    bday_dates = birthday.items()
    for l in bday_dates:
        if l[1] == today:
            if "@" in l[0]:
                for user in human_nature_accounts:
                    if l[0] in user:
                        birthday_tweet = (user.split(" - ")[0]+f"\n\nHappy Birthday {l[0]}!")
                        if len(birthday_tweet) > 280:
                            pass
                        elif birthday_tweet in used_bday_quotes:
                            pass
                        else:
                            print(api.update_status(birthday_tweet))
                            print(birthday_tweet, "\n\n", len(birthday_tweet), "characters long","\n")
                            #1 hour
                            sleep(3600)
            elif "#" in l[0]:
                for user in human_nature_without:
                    if l[0] in user:
                        birthday_tweet = (user.split(" - ")[0]+f"\n\nHappy Birthday {l[0]}!")
                        if len(birthday_tweet) > 280:
                            pass
                        elif birthday_tweet in used_bday_quotes:
                            pass
                        else:
                            print(api.update_status(birthday_tweet))
                            print(birthday_tweet, "\n\n", len(birthday_tweet), "characters long", "\n")
                            #1 hour
                            sleep(3600)
###########################################
#This tweets quotes from authors who have Twitter accounts
def regular_tweet_accounts():
    tweet = choice(human_nature_accounts)
    try:
        print(api.update_status(tweet))
        print(f"Tweeting: {tweet}\n{len(tweet)} characters long")
    except:
        print(f"Was not able to tweet:\n{tweet}")
        print(f"{len(tweet)} characters long")
#############################################
#Tweets authors who do not have Twitter accounts
def regular_tweet_without():
    tweet = choice(human_nature_without)
    try:
        print(api.update_status(tweet))
        print(f"Tweeting: {tweet}\n{len(tweet)} characters long")
    except:
        print(f"Was not able to tweet:\n{tweet}")
        print(f"{len(tweet)} characters long")
#############################################
#Tweets from authors who have retweeted my account in the past
def accounts_that_engage():
    tweet = choice(engaging_accounts.accounts)
    try:
        print(api.update_status(tweet))
        print(f"Tweeting: {tweet}\n{len(tweet)} characters long")
    except:
        print(f"Was not able to tweet:\n{tweet}")
        print(f"{len(tweet)} characters long")
#############################################
#Tweets quotes from authors with their photos on it
def tweet_with_pic():
    hnd = choice(list(human_nature_dict.keys()))
    try:
        tweet = api.update_with_media(f"pics/{hnd}", human_nature_dict[hnd])
        print(tweet)
        print(f"Tweeting: {human_nature_dict[hnd]}\n{len(human_nature_dict[hnd])} characters long")
    except:
        print(f"Was not able to tweet:\n{human_nature_dict[hnd]}")
        print(f"{len(human_nature_dict[hnd])} characters long")
##############################################
#tweets various psychology terms
def psychology():
    tweet = choice(psych)
    try:
        print(api.update_status(tweet))
        print(f"Tweeting: {tweet}\n{len(tweet)} characters long")
    except:
        print(f"Was not able to tweet:\n{tweet}")
        print(f"{len(tweet)} characters long")
###############################################
#tweets links for people to buy books from these authors
def amazon_links():
    aff_links = choice(list(affiliate_links.keys()))
    tweet = (f"{affiliate_links[aff_links]}\n{aff_links}")
    print(api.update_status(tweet))
    print(f"Tweeted an affiliate link:\n{tweet}")
###############################################
#Decides which function above will get executed
tweets = (human_nature_accounts, human_nature_accounts, human_nature_without, "accounts_that_engage", human_nature_without, human_nature_dict, human_nature_dict, psych, affiliate_links)
while True:
    birthday_boy()
    tweet_list = choice(tweets)
    if tweet_list == human_nature_accounts:
        regular_tweet_accounts()
    elif tweet_list == human_nature_without:
        regular_tweet_without()
    elif tweet_list == "accounts_that_engage":
        accounts_that_engage()
    elif tweet_list == human_nature_dict:
        try:
            tweet_with_pic()
        except:
            choice(regular_tweet_accounts(), regular_tweet_without())
    elif tweet_list == psych:
        psychology()
    elif tweet_list == affiliate_links:
        amazon_links()
    #Tweet every 2 hours
    sleep(7200)
