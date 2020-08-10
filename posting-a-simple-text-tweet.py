import tweepy

consumer_key = "nDZ9rWxijlxGoYIly1ZA0heT0"
consumer_secret_key = "Yv7OjoX20T2Fi5N6xbffZcK7U9IoB18kqphTWFUACfufJXgiUX"

access_token = "1292602359076605953-viJYPtgMqiH4Lqv8H8i8LgM7lN1pVM"
access_token_secret = "PCaE2bmD41NyOkScxBdFZggznR05iOwuUnFr08uGBA5UR"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

api.update_with_media("img/celebration.gif", "Testing a gif post with Tweepy API")
