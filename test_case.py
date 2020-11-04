import pytest
from search import search
from TwitterAPI import twitter_search

def test_num1():
    #consumer_key = os.getenv('CONSUMER_KEY')
    #consumer_secret = os.getenv('CONSUMER_SECRET')
    #access_key = os.getenv('ACCESS_KEY')
    #access_secret = os.getenv('ACCESS_SECRET')
    keyword = 'COVID-19'
    num = 5
    res = search(keyword,num)
    assert len(res) == 5
    
def test_num2():
    keyword = 'COVID-19'
    num = 5
    res = twitter_search(keyword,num)
    assert len(res) == 1

def test_type_successful():
        keyword = 'COVID-19'
        num = 1
        res = twitter_search(keyword,num)
        assert type(res) is str
        
if __name__ == '__main__':
    pytest.main()

