import requests
from bs4 import BeautifulSoup

URL = 'https://mangakakalot.com/manga/hw922220'
manga_page = requests.get(URL)

soup = BeautifulSoup(manga_page.content, 'html.parser')
chapter_results = soup.find('div', class_='chapter-list')

chapter_url = chapter_results.a['href']
chapter = requests.get(chapter_url)
chapter_page = BeautifulSoup(chapter.content, 'html.parser')

image_results = chapter_page.find('div', class_='vung-doc')
image_links = image_results.find_all('img')
images = []
for image in image_links:
    images.append(image['src'])
print(images)
