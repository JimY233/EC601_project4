import pytest
import tweepy
from search import search
from TwitterAPI import twitter_search, twitter_timeline

def test_num1(): #test num of search
    #consumer_key = os.getenv('CONSUMER_KEY')
    #consumer_secret = os.getenv('CONSUMER_SECRET')
    #access_key = os.getenv('ACCESS_KEY')
    #access_secret = os.getenv('ACCESS_SECRET')
    keyword = 'COVID-19'
    num = 5
    res = search(keyword,num)
    assert len(res) == 5
    
def test_num2(): #test num of search using different keyword and different num
    keyword = 'realDonaldTrump'
    num = 100
    res = search(keyword,num)
    assert len(res) == 100
  
def test_num3(): #test num of timeline
    userid = 'LeoDiCaprio'
    num = 10
    res = twitter_timeline(userid,num)
    assert len(res) == 10 
    
def test_timeline():
    userid = 'LeoDiCaprio'
    num = 10
    res = twitter_timeline(userid,num)
    assert type(res[0]) is tweepy.models.Status

def test_type():
    keyword = 'COVID-19'
    num = 1
    res = twitter_search(keyword,num)
    assert type(res) is str
        
if __name__ == '__main__':
    pytest.main()

