from TwitterAPI import twitter_search
from NLPAPI import NLP_analyze

def analysis(keyword = 'COVID-19',num = 10):
    #input module
    #keyword = input("Please enter the keyword:\n")
    #num = int(input("Please enter how many tweets you want to analyze:\n"))

    #Twitter_API module
    text = twitter_search(keyword,num)

    #NLPAPI module
    sentiment = NLP_analyze(text)

    #output module
    print('Sentiment analysis:keyword:{}, score:{}, magnitude:{}'.format(keyword,sentiment.score, sentiment.magnitude))

    with open('sentiment.txt','a') as output:
        output.write('keyword:{}, score:{}, magnitude:{}\n'.format(keyword,sentiment.score, sentiment.magnitude))

    with open('tweets.txt','w',encoding='utf-8') as tweets:
        tweets.write(text)  #record analyzed text

if __name__ == '__main__':
    analysis()
