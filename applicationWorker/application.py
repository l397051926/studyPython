from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from applicationWorker import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
