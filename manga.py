import requests
from bs4 import BeautifulSoup


class Manga ():
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def gen_list(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
        chapters = soup.find_all('div', class_='row')
        chapters.pop(0)
        for chapter in chapters:
            anchor = chapter.find('a')
            print('The Title is ' + anchor.string)
            print('The Link is ' + anchor['href'])
