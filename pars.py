import requests
from bs4 import BeautifulSoup as bs
import json

URL_TEMPLATE = "https://losst.ru/"
r = requests.get(URL_TEMPLATE)
soup = bs(r.text, "html.parser")



def get_last_articles():

    with open('articles_json.json', 'r') as file:
        articles_data = json.loads(file.read())

    articles_list = [name for name in soup.find_all('article', class_='latestPost')]

    last_articles = {}

    for article in articles_list:

        article_name = article.find('h2', class_='post-title').a['title']
        article_author = article.find('span', class_='theauthor').span.a.text
        article_date = article.find('span', class_='thetime updated').span.text
        article_img = article.find('div', class_='post-img').a.img['src']
        article_anotation = article.find('div', class_='post-excerpt').text[29:]
        article_url = article.find('div', class_='readMore').a['href']
        article_slug = article_url[17:]

        if article_slug not in articles_data:
            last_articles.update(
                {article_slug: {
                        'name': article_name,
                        'author': article_author,
                        'date': article_date,
                        'img': article_img,
                        'anotation': article_anotation,
                        'url': article_url
                        }
                    }
                )
        else:
            break

    articles_data.update(last_articles)
    with open('articles_json.json', 'w') as file:
        json.dump(articles_data, file, indent=4, ensure_ascii=False)

    return last_articles
