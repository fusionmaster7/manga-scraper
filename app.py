import flask
from flask import request
import controllers

app = flask.Flask(__name__)
app.config['DEBUG'] = True


@app.route('/manga/all', methods=['GET'])
def mangas_response():
    res = controllers.get_all_mangas()
    return res


@app.route('/manga/<manga>', methods=['GET'])
def manga_response(manga):
    res = controllers.get_manga(manga_name=manga)
    return res


@app.route('/manga/<manga>/<chapter>', methods=['GET'])
def chapter_response(manga, chapter):
    res = controllers.get_chapter(manga_name=manga, chapter_number=chapter)
    return res


app.run()
