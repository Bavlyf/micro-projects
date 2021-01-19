import json
from difflib import get_close_matches

data = json.load(open("./dataset/data.json"))

def word_definition(word,english_dict):
    if word.title() in english_dict:
        return "\n".join(english_dict[word.title()])
    elif word.lower() in english_dict:
        return "\n".join(english_dict[word.lower()])
    elif word.upper() in english_dict:
        return "\n".join(english_dict[word.upper()])
    similar_words = get_close_matches(word.lower(),english_dict)
    if len(similar_words) > 0:
        yn = input(f"Did you mean {similar_words[0]}? if yes write Y if no write N.\n")
        if yn.lower() == "y":
            return "\n".join(english_dict[similar_words[0]])
        elif yn.lower() == "n":
            return "Word does not exist"
        else:
            return "we didn't understand your answer"
    else:
        return "Word does not exist"

while True:
    user_input = input("Please Enter a word: ")
    if user_input == "\\end":
        break
    else:
        print(word_definition(user_input,data))
