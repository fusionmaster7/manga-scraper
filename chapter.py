import requests
from bs4 import BeautifulSoup
import json


class Chapter():
    def __init__(self, chapter_number, link):
        self.chapter_number = chapter_number
        self.link = link
        self.image_links = []

    def gen_images(self):
        page = requests.get(self.link)
        chapter_soup = BeautifulSoup(page.content, 'html.parser')
        page_section = chapter_soup.find('div', class_='vung-doc')
        pages = page_section.find_all('img')
        for page in pages:
            self.image_links.append(page['src'])

    def create_json(self):
        my_json = json.dumps(self.__dict__)
        print(my_json)
