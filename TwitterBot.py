import os, random, tweepy, datetime, time
from random_words import RandomWords
from PyDictionary import PyDictionary
import renameGifs


consumer_key = "nDZ9rWxijlxGoYIly1ZA0heT0"
consumer_secret_key = "Yv7OjoX20T2Fi5N6xbffZcK7U9IoB18kqphTWFUACfufJXgiUX"

access_token = "1292602359076605953-viJYPtgMqiH4Lqv8H8i8LgM7lN1pVM"
access_token_secret = "PCaE2bmD41NyOkScxBdFZggznR05iOwuUnFr08uGBA5UR"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

def loadRandomWord():
    dictionary = PyDictionary() # declaring dictionary variable  and initialising PyDictionary
    rw = RandomWords() # delcaring rw variable and initialising RandomWords

    word = rw.random_word() #adeclaring a new variable and assigning it to equal a random word from the RandomWords library
    definitions = dictionary.meaning(word) #declaring a new value, and assigning it a meaning from the PyDictionarylibrary

    try: #Try catch to prevent a null definition
        part_of_speech = random.choice(list(definitions.keys()))  #randomly choosing a part of speech
        definition = random.choice(definitions[part_of_speech]) #randomly choosing a definition associated with part of speech generated above
    except:
        return "NULL_DEFINITION" #returns an exception if no definition available for generated part of speech

    return{ #returns a word using the "word" key in the dictionary, a definition using "dictionary" key, and a part of speech using "part_of_speech" key from PyDictionary
    "word":word,
    "definition":definition,
    "part_of_speech":part_of_speech
    }

def GrabRandomGif(): #Grabs a random .gif file from img/ folder
    Gif_Choice = random.choice(os.listdir("Gifs/")) #Grabs a random file name from img/ folder, assigns filename as a string
    print (Gif_Choice)
    return Gif_Choice

def SendTweet(): #Tries to send the tweet containing the wotd and gif

    print("\nSend Tweet Reached") #Duckytest
    try:
        print("\nTrying to tweet")
        api.update_with_media(f'Gifs/{Gif_Choice}', wotd_tweet) #Sends tweet with gif attachment, filename generated by GrabRandomGif()

        Time_Sent = str(datetime.datetime.now()) #Gets current time
        print(f'--------------------\nTweet sent successfully at {Time_Sent} about {word_of_the_day["word"]}\n------------------')
         #Prints to console when a tweet is successfully made, with it's time and what word was tweeted
        Sleep() #Calls sleep function

    except:
        print("Error Code: GIF_EXCEED")
        return "GIF_EXCEED" #If gif file cannot be posted (Gifs limited to 3mb upload on twitter) will return exception


def Sleep():
    print("\nNow sleeping for 59 minutes")
    time.sleep(3540)

while(True): #always true
    if (datetime.datetime.now().minute == 00): #Waits until beginning of the hour
        word_of_the_day = loadRandomWord() #initialises loadRandomWord() and assigns its return value to word_of_the_day
        #print("\nRandom Word Loaded") #Duckytest
        Gif_Choice = GrabRandomGif() #initialises GrabRandomGif() and assigns its return value to Gif_Choice
        #print("\nRandom Gif Grabbed") #Duckytest

        while(word_of_the_day == "NULL_DEFINITION"): # while wotd try/catch produces an error exception, re-tries the method
            word_of_the_day = loadRandomWord()

        while(SendTweet == "GIF_EXCEED"): # while tweet can't send - picks a new gif
            GrabRandomGif()

        wotd_tweet = (f'{word_of_the_day["word"]} ({word_of_the_day["part_of_speech"]}): {word_of_the_day["definition"]} \n #WordOfTheDay ') #collates the 3 strings into one, to be sent as a single string to SendTweet()
        #print("\nwotd assigned")
        SendTweet() #calls SendTweet() methood
