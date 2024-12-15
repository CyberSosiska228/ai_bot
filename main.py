import telebot
import psycopg2
import json
import ai_req


settings  = {}
with open("settings.json") as f:
    settings = json.load(f)

'''
pg_connection = psycopg2.connect(database=settings["postgres_settings"]["database"],
                                 host=settings["postgres_settings"]["host"],
                                 user=settings["postgres_settings"]["user"],
                                 password=settings["postgres_settings"]["password"],
                                 port=settings["postgres_settings"]["port"])
print(pg_connection)
'''

bot = telebot.TeleBot(settings["token"])


def mes_handle(message):
    send_req = {
            "url" : "http://localhost:11434/api/generate",
            "headers" : {"Content-Type" : "applicatioin/json"},
            "json" : {
                "model": "llama3.2:3b",
                "prompt": message.text
            }
    }
    response = ai_req.ans_quest(send_req)
    bot.send_message(message.from_user.id, response)

@bot.message_handler(content_types=['text'])
def get_text_message(message):
    mes_handle(message)


while True:
    bot.polling(none_stop=True, interval=0)
