import flask

import mtg

IMAGE_FORMATS = {'png', 'border_crop', 'art_crop', 'large', 'normal', 'small'}
DEFAULT_IMAGE_FORMAT = 'small'

app = flask.Flask(__name__)
search = mtg.Search()

@app.route('/update', methods=['GET'])
def update():
    search.update()
    return '', 200

@app.route('/image', methods=['POST'])
def image():
    j = flask.request.get_json()

    imageFormat = j['format']
    if imageFormat not in IMAGE_FORMATS:
        imageFormat = DEFAULT_IMAGE_FORMAT

    cards = j['cards']

    res = search.image(cards, imageFormat)
    return res
