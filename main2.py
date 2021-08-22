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
                my_answer = f"<b>{article['name']}</b>\n" \
                            f"<i>{article['date']}</i>\n\n" \
                            f"{article['anotation']}\n" \
                            f"<a href='{article['url']}'>inline URL</a>"
                send_result = rq.post(
                    URL + '/sendPhoto',
                    params={
                        'chat_id': user_id,
                        'photo': article['img'],
                        'caption': my_answer,
                        'parse_mode': 'HTML'
                    }
                )
        time.sleep(3600) #repeat every hour


if __name__ == '__main__':
    send_new_articles()
