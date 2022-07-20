import requests
import random

url = requests.get('https://ru.wikipedia.org/wiki/ArXiv.org')


def save_page(page):
    """
    сохранение html страницы
    :param page: содержимое страницы
    :return:
    """
    num = random.randint(1, 100)
    try:
        with open(f'index{num}.html', 'w', encoding='utf-8') as f:
            f.write(page)
    except Exception as e:
        print(e)


save_page(url.text)
