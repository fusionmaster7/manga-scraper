import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flask import jsonify

from manga import Manga
from chapter import Chapter

cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred)

db = firestore.client()


def get_manga(manga_name):
    doc_ref = db.collection(u'manga').document(manga_name)
    doc = doc_ref.get()
    if(doc.exists):
        manga_url = doc.to_dict()['url']
        my_manga = Manga(name=manga_name, url=manga_url)
        my_manga.gen_list()
        chapter_list = []
        for chapter in my_manga.chapters:
            chapter_list.append(chapter.link)
        res = {"name": my_manga.name, "url": my_manga.url, "links": chapter_list}
        return jsonify(res)
    else:
        res = {"okay": False, "message": "Manga Not Found"}
        return jsonify(res)


def get_chapter(manga_name, chapter_number):
    doc_ref = db.collection(u'manga').document(manga_name)
    doc = doc_ref.get()
    if(doc.exists):
        manga_url = doc.to_dict()['url']
        my_manga = Manga(name=manga_name, url=manga_url)
        my_manga.gen_list()
        chapter_url = my_manga.chapters[int(chapter_number)-1].link
        chapter_number = int(chapter_number)
        my_chapter = Chapter(chapter_number=chapter_number, link=chapter_url)
        my_chapter.gen_images()
        res = {"chapter_number": int(
            chapter_number), "okay": "true", "links": my_chapter.image_links}
        return jsonify(res)
    else:
        res = {"okay": "false", "message": "Chapter Not Found"}
        return jsonify(res)
