import tweepy
import sys
import os

def twitter_search2(keyword,num):
    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

    #Twitter API credentials
    consumer_key = os.getenv('CONSUMER_KEY')
    consumer_secret = os.getenv('CONSUMER_SECRET')
    access_key = os.getenv('ACCESS_KEY')
    access_secret = os.getenv('ACCESS_SECRET')
     
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)

    api = tweepy.API(auth)

    text = []

    for tweet in tweepy.Cursor(api.search,q=keyword).items(num):
        text.append(tweet.text.translate(non_bmp_map))

    return text

if __name__ == '__main__':
    
    keyword = input("Please enter the keyword:\n")
    num = int(input("Please enter how many tweets you want to analyze:\n"))

    twitter_search(keyword,num)
    
