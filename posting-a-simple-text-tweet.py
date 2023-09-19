import tweepy

consumer_key = ""
consumer_secret_key = ""

access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

api.update_with_media("img/celebration.gif", "Testing a gif post with Tweepy API")
