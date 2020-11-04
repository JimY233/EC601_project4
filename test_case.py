import pytest
from search import search
from TwitterAPI import twitter_search

def test_num_successful():

    #consumer_key = os.getenv('CONSUMER_KEY')
    #consumer_secret = os.getenv('CONSUMER_SECRET')
    #access_key = os.getenv('ACCESS_KEY')
    #access_secret = os.getenv('ACCESS_SECRET')

    keyword = 'COVID-19'
    num = 1
    res = search(keyword,num)
    assert len(res) == 1


if __name__ == '__main__':
    pytest.main()

