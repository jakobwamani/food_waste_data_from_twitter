import tweepy
from credentials import *
import csv #Import csv
auth = tweepy.auth.OAuthHandler(api_key,api_secret_key)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# Open/create a file to append data to
csvFile = open('devices.csv', 'a')

#Use csv writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search_tweets,
                           q = "food waste -filter:retweets", 
                           lang = "en").items(3000):

    # Write a row to the CSV file. I use encode UTF-8
    # csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),tweet.user.location])
    csvWriter.writerow([tweet.created_at,tweet.source])
    # print tweet.created_at, tweet.text

csvFile.close()