import tweepy
import time

consumer_key= ''
consumer_secret= ''
key= ''
secret= ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

#create file to store tweet id that has already been tweeted/liked/commented to prevent repetition

FILE_NAME = 'last_seen.txt'

#iterate over the last tweet id to exclude it ensure the bot doesn't repeat itself

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

 #store the last tweet id used to a file 

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

#create a function that searches for mentions/tags then automatically comments,likes and retweets the tweet and stores it's id to the file_name

def reply():
    tweets= api.mentions_timeline(read_last_seen(FILE_NAME),tweet_mode = 'extended')
    for tweet in reversed(tweets):
        if '#randomtweet' in tweet.full_text.lower():
            print("Replied  To ID - " + str(tweet.id))
            api.update_status("@" + tweet.user.screen_name  + ' Good Luck For #100DaysOfCode!', tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen(FILE_NAME, tweet.id)

while True:
    reply()
    time.sleep(15)
