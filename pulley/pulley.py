from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world"

@app.route("/pull")
def pull():
    os.system("git pull")
    return "200"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9001, debug=False)