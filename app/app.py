from flask import Flask
import redis

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello():
    cache.incr('hits')
    return f"Hello World! This page has been viewed {cache.get('hits').decode('utf-8')} times."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)