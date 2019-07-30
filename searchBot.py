import tweepy
import time

consumer_key=''
consumer_secret= ''
key= ''
secret= ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

#Indicate the hashtag the bot should search for and how many retweets should it perfom

hashtag = '100daysofcode'
tweetNumber = 10

tweets = tweepy.Cursor(api.search,hashtag).items(tweetNumber)

#create a function to confirm retweet status,time interval between retweets and error info
 
def searchbot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweet Done!")
            time.sleep(60)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(60)

searchbot()
