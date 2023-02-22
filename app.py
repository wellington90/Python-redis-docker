import os
from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host=os.environ.get('REDIS_HOST', 'redis'), port=6379, db=0)

@app.route('/')
def index():
    count = r.incr('counter')
    return 'This page has been refreshed {} times.'.format(count)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
