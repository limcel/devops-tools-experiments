from flask import Flask

app = Flask(__name__)


@app.route('/')
def start():
    return 'Running Flask!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
