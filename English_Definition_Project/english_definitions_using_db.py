from difflib import get_close_matches
import mysql.connector
import json

db_conf = json.load(open("./configuration/db.conf"))

con = mysql.connector.connect(
user=db_conf['user'],
password=db_conf['password'],
host=db_conf['host'],
database=db_conf['database']
)
cursor = con.cursor()

def get_all_words():
    cursor.execute("SELECT word FROM definitions")
    all_words = [item[0] for item in cursor.fetchall()]
    return all_words

def get_definitions(word):
    sql_query = "SELECT word_definitions FROM definitions WHERE word = %s"
    cursor.execute(sql_query, (word,))
    results = [item[0] for item in cursor.fetchall()]
    if len(results) == 0:
        return False
    else:
        return results
def get_similar_word(word):
    all_words = get_all_words()
    similar_words = get_close_matches(word,all_words)
    if len(similar_words) > 0:
        return similar_words[0]
    else:
        return False

def word_definition(word):
    if not get_definitions(word):
        similar_word = get_similar_word(word)
        if not similar_word:
            return "Word does not exist"
        else:
            yn = input(f"Did you mean {similar_word}? if yes write Y if no write N.\n")
            if yn.lower() == "y":
                return "\n".join(get_definitions(similar_word))
            elif yn.lower() == "n":
                return "Word does not exist"
            else:
                return "we didn't understand your answer"
    else:
        return "\n".join(get_definitions(word))
while True:
    user_input = input("Please Enter a word: ")
    if user_input == "\\end":
        break
    else:
        print("########################\n" + word_definition(user_input))
