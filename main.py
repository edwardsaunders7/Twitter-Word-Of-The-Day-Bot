from PyDictionary import PyDictionary
import random
from RandomWords import RandomWords

dictionary = PyDictionary()


word = "run"
definitions = dictionary.meaning(word)

part_of_speech = random.choice(list(definitions.keys()))
definition = random.choice(definitions[part_of_speech])

print(f'{word}: {definition} ({part_of_speech})')
