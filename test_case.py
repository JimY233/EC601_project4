import pytest
import unittest
from TwitterAPI import twitter_search

class MyTestCase(unittest.TestCase):
    def test_num_successful(self):

        #consumer_key = os.getenv('CONSUMER_KEY')
        #consumer_secret = os.getenv('CONSUMER_SECRET')
        #access_key = os.getenv('ACCESS_KEY')
        #access_secret = os.getenv('ACCESS_SECRET')

        keyword = 'COVID-19'
        num = 1

        #res = twitter_search(keyword,num,consumer_key,consumer_secret,access_key,acess_secret):
        res = twitter_search(keyword,num)
                             
        txt = []
        for tweet in res:
            txt.append(tweet.text)
        print(txt)


        self.assertEqual(1, len(txt))


if __name__ == '__main__':
    unittest.main()
