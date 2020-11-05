import os
#os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key/google_nlp_key.json"

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


def NLP_analyze(text):
    
    # Instantiates a client
    client = language.LanguageServiceClient()

    # The text to analyze
    #with open('Tweets.txt', 'r') as review_file:
    #    text = review_file.read()

    #text = u'Hello, world!'
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment

    #print('Text: {}'.format(text))
    #print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))

    return sentiment
