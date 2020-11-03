from TwitterAPI import twitter_search
from NLPAPI import NLP_analyze

def compare():
    #input module
    print("Compare the sentiment related keyword1 and keyword2 in twitter")
    keyword1 = input("Please enter the keyword1:\n")
    keyword2 = input("Please enter the keyword2:\n")
    num = int(input("Please enter how many tweets you want to analyze:\n"))

    #Twitter_API module
    text1 = twitter_search(keyword1,num)
    text2 = twitter_search(keyword2,num)

    #NLPAPI module
    sentiment1 = NLP_analyze(text1)
    sentiment2 = NLP_analyze(text2)

    #output module
    print('Sentiment analysis:keyword:{}, score:{}, magnitude:{}'.format(keyword1,sentiment1.score, sentiment1.magnitude))
    print('Sentiment analysis:keyword:{}, score:{}, magnitude:{}'.format(keyword2,sentiment2.score, sentiment2.magnitude))
    if sentiment1.score < sentiment2.score:
        print("Sentiment to {} is more negative than sentiment to {} in Twitter".format(keyword1,keyword2))
    elif sentiment1.score == sentiment2.score:
        print("Sentiment to {} and sentiment to {} are similiar in Twitter".format(keyword1,keyword2))
    else:
        print("Sentiment to {} is more positive than sentiment to {} in Twitter".format(keyword1,keyword2))

if __name__ == '__main__':
    compare()
