from pars import get_last_articles
import requests as rq
import time

API_TOKEN = ''
user_id = 1455367819

URL = 'https://api.telegram.org/bot' + API_TOKEN


def send_new_articles():
    while True:
        last = get_last_articles()
        if last:
            for article in last.values():
                my_answer = f"{article['name']}\n{article['date']}\n{article['anotation']}\n{article['url']}"
                send_result = rq.get(
                    URL + 'sendPhoto',
                    params={
                        'chat_id': user_id,
                        'photo': article['img'],
                        'caption': my_answer
                    }
                )
        time.sleep(3600) #repeat every hour


if __name__ == '__main__':
    send_new_articles()
