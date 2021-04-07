"""
Получить с русской википедии список всех животных (Категория:Животные по алфавиту)
и вывести количество животных на каждую букву алфавита.
Результат должен получиться в следующем виде:
А: 642
Б: 412
В:....
Не забываем установить bs4 командой: pip install beautifulsoup4,
а так же requests командой: pip install requests
"""
from bs4 import BeautifulSoup
import requests


def count_animals():
    """
    Парсим с википедии количество животных на каждую букву алфавита.
    Это займет некоторое время.
    """
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0'}
    url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
    response = requests.get(url, headers=headers)
    flag = True
    d = {x: 0 for x in 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ'}
    # Ключи словаря можно и динамически при парсинге создавать

    while flag:
        soup = BeautifulSoup(response.text, features='html.parser')
        groups = soup.find_all('div', class_='mw-category-group')

        for group in groups:
            letter = group.find('h3').text
            if letter == 'A':  # chr(65)
                flag = False
                break
            d[letter] += len(group.find_all('li'))

        link = soup.find('div', id='mw-pages').find('a',
                                                    text='Следующая страница')
        url = 'https://ru.wikipedia.org/' + link.get('href')
        response = requests.get(url, headers=headers)

    return d


if __name__ == "__main__":
    animals = count_animals()
    for i in animals:
        print(i + ':', animals[i])
