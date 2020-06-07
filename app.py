from manga import Manga
from chapter import Chapter


url = 'https://mangakakalot.com/manga/fc922780'
my_manga = Manga('The Story of a Waitress and Her Customer', url=url)

my_manga.gen_list()
my_manga.chapters[3].print_pages()
