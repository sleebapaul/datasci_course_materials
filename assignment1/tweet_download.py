import tweepy 

# Fill the X's with the credentials obtained by 
# following the above mentioned procedure. 
consumer_key = "sI4ViVkZ8Ocu8c91Wip9MvIrd"
consumer_secret = "HR1KsfYApPk9f9wcCud0FN7y3iYQqxpEhke8eOXUZrVXFBinkU"
access_key = "300140254-azF1tGgrrZJoGIAPsIez1f48IWgDAoQrFkY3KnlM"
access_secret = "qxhDBx5pyWw13UfyrVJfIKLiBprEJvuv7CMraL30IHxh4"

# Function to extract tweets 
def get_tweets(username): 
    # Authorization to consumer key and consumer secret 
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 

    # Access to user's access key and access secret 
    auth.set_access_token(access_key, access_secret) 

    # Calling api 
    api = tweepy.API(auth) 

    # 200 tweets to be extracted 
    number_of_tweets=200
    tweets = api.user_timeline(screen_name=username, count=number_of_tweets) 

    # Empty Array 
    tmp=[] 

    # create array of tweet information: username, 
python tweet_sentiment.py AFINN-111.txt output.txt    # tweet id, date/time, text 
    for tweet in tweets: 
        # Appending tweets to the empty array tmp 
        print(tweet.text.strip()) 

    # Printing the tweets 
    print(tmp) 


# Driver code 
if __name__ == '__main__': 

	# Here goes the twitter handle for the user 
	# whose tweets are to be extracted. 
	get_tweets("omarsar0") 
