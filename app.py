from dotenv import load_dotenv
from os import getenv
from flask import (
    Flask , render_template
)
load_dotenv()
PORT = int(getenv("PORT"))
app = Flask(__name__,
  template_folder = "templates"
)

@app.get("/")
def home():
    return render_template("/index.html",title="Home")

if __name__ == '__main__':
    app.run(debug=True,port=PORT)
