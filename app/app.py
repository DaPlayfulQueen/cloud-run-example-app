from flask import Flask
import time
import os

app = Flask(__name__)

@app.route('/')
def hello():
    print("Hello from the Python script!")
    time.sleep(10)
    return "It works!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))