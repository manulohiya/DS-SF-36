# This is a simple twitter sentiment analysis based on keyword search

import tweepy
from textblob import TextBlob


consumer_key = 'blIEzxbMsjbiRBVNsHZnHLrHS'
consumer_secret = 'MWTTJ855qsM23qX6O1In3wTRH2PJ7EHaEG6HUfeskAFzbKJZzS'

access_token = 	'1010066696-zHPbnHrUti3THtEPl3HXRUN4eAuGUyjvnhLjsWg'
access_token_secret = 'VPB99S6rb6TesCwhMODwUnEBd4sh9kVUIU3j9hy1eatnn'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Change query here 
query = 'Trump'

max_results = 100
public_tweets = api.search(q=query,count=max_results)
polarity = 0
subjectivity = 0

for tweet in public_tweets:
	analysis = TextBlob(tweet.text)
	# print the really negative ones
	if analysis.sentiment.polarity < -0.5:
		print tweet.text
		print analysis.sentiment
	# print the really positive ones
	if analysis.sentiment.polarity > 0.5:
		print tweet.text
		print analysis.sentiment
	polarity = polarity + analysis.sentiment.polarity
	
print "total polarity", polarity
