from applicationWorker import application

db = application.db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    email = db.Column(db.String)

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def __repr__(self):
        return '{ id: %r, name : %r, age : %r, email : %r  }' % (self.id,self.name,self.age,self.email)