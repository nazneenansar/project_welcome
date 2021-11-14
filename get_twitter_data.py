from config import *
import tweepy
import datetime
import csv


auth = tweepy.OAuthHandler("key", "secret")
auth.set_access_token("key", "secret")
api = tweepy.API(auth, wait_on_rate_limit=True)
today = datetime.date.today()
yesterday= today - datetime.timedelta(days=30)
print("tweet list")
tweets_list = tweepy.Cursor(api.search_tweets, q="girlsintech", lang="en", since=yesterday, tweet_mode='extended').items()
output = []
csv_file = open("csv_filetechwomen.csv", "w")
writer = csv.writer(csv_file)

for tweet in tweets_list:
     if tweet.user.verified:
        continue
    text1 = tweet.full_text
    id1 = tweet.id
    if tweet.retweet_count < 5:
        continue
    if len(text1) > 2 and text1[:2] == "RT":
        continue

    print(text1)
    line = {'text': text1}
    output.append(line)
    writer.writerow([text1, id1])

import pandas as pd
df = pd.DataFrame(output)
df.to_csv('output.csv')
print("done!")
