import boto
from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        r = requests.get('http://' + str(sys.argv[1]) + ':5000')
        return "Hello, {}".format(r.text)
    except:
        return "Service B unreachable"

@app.route("/health")
def health():
    r = requests.get('http://' + str(sys.argv[1]) + ':5000')
    import pdb; pdb.set_trace()
    return str(r.status_code)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
