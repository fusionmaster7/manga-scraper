import requests
import pprint

URL = 'https://manganelo.com/manga/read_one_piece_manga_online_free4'
page = requests.get(URL)

print(page.content)
