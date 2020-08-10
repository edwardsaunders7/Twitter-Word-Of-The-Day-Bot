import os, random
from random_words import RandomWords
from PyDictionary import PyDictionary
import tweepy
import datetime
import time

consumer_key = "nDZ9rWxijlxGoYIly1ZA0heT0"
consumer_secret_key = "Yv7OjoX20T2Fi5N6xbffZcK7U9IoB18kqphTWFUACfufJXgiUX"

access_token = "1292602359076605953-viJYPtgMqiH4Lqv8H8i8LgM7lN1pVM"
access_token_secret = "PCaE2bmD41NyOkScxBdFZggznR05iOwuUnFr08uGBA5UR"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

def loadRandomWord():

    dictionary = PyDictionary()
    rw = RandomWords()

    word = rw.random_word()
    definitions = dictionary.meaning(word)

    try:
        part_of_speech = random.choice(list(definitions.keys()))
        definition = random.choice(definitions[part_of_speech])
    except:
        return "NULL_DEFINITION"

    return{
    "word":word,
    "definition":definition,
    "part_of_speech":part_of_speech
    }

while(True):
    if (datetime.datetime.now().minute == 00): #Waits until beginning of the hour
        word_of_the_day = loadRandomWord()

        while(word_of_the_day == "NULL_DEFINITION"):
            word_of_the_day = loadRandomWord()

        wotd_tweet = (f'{word_of_the_day["word"]} ({word_of_the_day["part_of_speech"]}): {word_of_the_day["definition"]} \n #WordOfTheDay ')
        number = random.randint(1,14)

        Gif_Choice = random.choice(os.listdir("img/"))


        api.update_with_media(f'img/{Gif_Choice}' ,wotd_tweet)
        Time_Sent = str(datetime.datetime.now())
        print(f'Tweet sent successfully at {Time_Sent} about {word_of_the_day["word"]}')
        time.sleep(3600) # waits 1hr
