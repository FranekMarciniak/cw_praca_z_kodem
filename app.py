from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, WSB!'

if __name__ == '__main__':
    # using 4000 because 5000 is reserved on macos
    app.run(host='0.0.0.0', port=4000)

