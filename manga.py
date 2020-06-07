import requests
from bs4 import BeautifulSoup

from chapter import Chapter


class Manga ():
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.chapters = []

    def gen_list(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
        manga_chapters = soup.find_all('div', class_='row')
        manga_chapters.pop(0)
        i = 0
        for chapter in manga_chapters:
            anchor = chapter.find('a')
            new_chapter = Chapter(chapter_number=i, link=anchor['href'])
            new_chapter.gen_images()
            self.chapters.append(new_chapter)
            i = i+1
        self.chapters.reverse()
