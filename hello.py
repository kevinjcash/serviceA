from flask import Flask
import requests
import sys

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        r = requests.get('http://' + str(sys.argv[1]))
        return "Hello, {}".format(r.text)
    except:
        return "Service B unreachable"

@app.route("/health")
def health():
    r = requests.get('http://' + str(sys.argv[1]))
    return str(r.status_code)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=false)
