from flask import Flask

from resources import ops_rest

app = Flask(__name__)

app.register_blueprint(ops_rest)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8080,
        threaded=True
    )
