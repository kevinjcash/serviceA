from flask import Flask
import requests
import sys

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        r = requests.get('http://' + str(sys.argv[1]), timeout=3.0)
        return "Hello, {}".format(r.text)
    except:
        return "Service B unreachable"

@app.route("/health")
def health():
    try:
        r = requests.get('http://' + str(sys.argv[1]), timeout=3.0)
        return str(200)
    except:
        return str(503)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=False)

