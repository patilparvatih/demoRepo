from dotenv import load_dotenv
from os import getenv
from flask import Flask

PORT = int(getenv("PORT"))
app = Flask(__name__),

@app.get("/")
def home():
    return "<h1>Welcome to Flask server</h1>"

if __name__ == '__main__':
    app.run(debug=True,port=PORT)
