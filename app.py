from flask import Flask, request, jsonify, g
from logging.config import dictConfig
from personrepository import PersonRepository
import json


dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'flasklog.log',
            'maxBytes': 1048576,
            'formatter': 'default',
            'encoding': 'UTF-8'
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'stream': 'ext://sys.stdout'
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['file', 'console']
    }
})

app = Flask(__name__)

@app.route('/')
def index():
    return 'Home Flask'

@app.route('/hello')
def hello_world():
    # app.logger.info('hello')
    return 'Hello World!'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/js')
def root():
    t = {
        'a': 1,
        'b': 2,
        'c': [3, 4, 5]
    }
    return jsonify(t)

@app.route('/data', methods=['POST'])
def comment():
    if request.method == 'POST':
        req_str = request.data.decode()

        js = json.loads(req_str)
        # app.logger.info(req_str)

        person_repository = PersonRepository()
        person_repository.parse_json(js)

    return "ok"


@app.route('/profile', methods=['POST'])
def profile():
    '''
    上传用户个人信息
    :return:
    '''
    if request.method == 'POST':
        req_str = request.data.decode()

        js = json.loads(req_str)
        app.logger.info(req_str)

    return "ok"


if __name__ == '__main__':
    app.run()

