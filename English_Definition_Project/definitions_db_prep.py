import json
import mysql.connector

data = json.load(open("./dataset/data.json"))

db_conf = json.load(open("./configuration/db.conf"))

con = mysql.connector.connect(
user=db_conf['user'],
password=db_conf['password'],
host=db_conf['host'],
database=db_conf['database']
)
cursor = con.cursor()
for word in data:
    # if one word has multiple definitions loop on the definitions.
    if len(data[word]) > 1:
        for expression in data[word]:
            sql_query = "INSERT into definitions (word,word_definitions) VALUES(%s,%s)"
            query = cursor.execute(sql_query, (word,expression))
            con.commit()
            print(cursor.rowcount, "record inserted.")
    else:
        sql_query = "INSERT into definitions (word,word_definitions) VALUES(%s,%s)"
        query = cursor.execute(sql_query, (word,data[word][0]))
        con.commit()
        print(cursor.rowcount, "record inserted.")
