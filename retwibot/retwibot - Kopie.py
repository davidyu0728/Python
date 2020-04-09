import tweepy
auth = tweepy.OAuthHandler("*********************", "*********************")
auth.set_access_token("*********************", "*********************")
api = tweepy.API(auth)
public_tweets = api.user_timeline("_takigawamiu")
for tweet in public_tweets:
    print(tweet.text)