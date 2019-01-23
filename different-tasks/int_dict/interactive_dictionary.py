#!/usr/bin/env python3
# Enter word, check result.
import json
from difflib import get_close_matches

data = json.load(open("dictionary.json"))

def retrive_definition(word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        action = input("Did you mean %s instead? [y or n]: " %
                       get_close_matches(word, data.keys())[0])
        if action == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif action == "n":
            return ["The word doesn't exist, lol."]
        else:
            return ["We don't understand your entry. Sorry."]


while True:
    for item in retrive_definition(input("Enter a word: ").lower()):
        print("-", item)
