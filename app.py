import flask
import controllers

app = flask.Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['GET'])
def get_manga():
    res = controllers.get_manga()
    return res


app.run()
