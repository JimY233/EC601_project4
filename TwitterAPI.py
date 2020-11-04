import tweepy
import sys
import os

def twitter_search(keyword,num):
    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

    #Twitter API credentials
    consumer_key = os.getenv('CONSUMER_KEY')
    consumer_secret = os.getenv('CONSUMER_SECRET')
    access_key = os.getenv('ACCESS_KEY')
    access_secret = os.getenv('ACCESS_SECRET')
     
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)

    api = tweepy.API(auth)

    text = ""

    for tweet in tweepy.Cursor(api.search,q=keyword).items(num):
        text += tweet.text.translate(non_bmp_map)

    #print(text)
    return text


def twitter_timeline(userid,num):
    consumer_key = os.getenv('CONSUMER_KEY')
    consumer_secret = os.getenv('CONSUMER_SECRET')
    access_key = os.getenv('ACCESS_KEY')
    access_secret = os.getenv('ACCESS_SECRET')
     
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)

    api = tweepy.API(auth)
     
    timeline = api.user_timeline(id=userid,count=num)
    return timeline

if __name__ == '__main__':
    keyword = input("Please enter the keyword:\n")
    userid = input("Please enter the userid:\n")
    num = int(input("Please enter how many tweets you want to analyze:\n"))

    twitter_search(keyword,num)
    twitter_timeline(userid,num)
    
