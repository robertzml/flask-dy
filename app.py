from flask import Flask, request, jsonify, g
from logging.config import dictConfig
from personrepository import PersonRepository
import json
import time
import asyncio
#from gevent import monkey
#from gevent.pywsgi import WSGIServer

#monkey.patch_all()

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

    asyncio.sleep(10)
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
        reqstr = request.data.decode()

        js = json.loads(reqstr)
        # app.logger.info(reqstr)

        person_repository = PersonRepository()
        person_repository.ParseJson(js)

    return "ok"

if __name__ == '__main__':
    app.run()
    #http_server = WSGIServer(('', 5000), app)
    #http_server.serve_forever()
