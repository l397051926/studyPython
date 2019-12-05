from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from day03 import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


class UserTmp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/')
def index():
    return 'hello world'

#
# admin = UserTmp('ccc', 'ccc')
# user1 = UserTmp('eee', 'eee')
# db.session.add(admin)
# db.session.add(user1)
# db.session.commit()

if __name__ == '__main__':
    users = UserTmp.query.all()
    print(users)
    user = UserTmp.query.filter_by(username='admin').first()
    print(user)
    app.run(debug=True)