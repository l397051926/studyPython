from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from day03 import config
from day03 import model

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True)