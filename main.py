import requests

url = requests.get('https://ru.wikipedia.org/wiki/ArXiv.org')


def save_page(page):
    """
    сохранение html страницы
    :param page: содержимое страницы
    :return:
    """

    try:
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(page)
    except Exception as e:
        print(e)


save_page(url.text)
