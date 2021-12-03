from flask import Flask
from fake_gcs import get_fake_client

client = get_fake_client()
bucket = client.bucket('demo')
blob = bucket.get_blob('test.txt')
app = Flask("__name__")

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World111!'

@app.route("/test")
def test():
    return "test222"

@app.route("/demo/<service>",methods=["GET"])
def demo(service):
    return service

@app.route("/get")
def get():
    return str(blob)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)