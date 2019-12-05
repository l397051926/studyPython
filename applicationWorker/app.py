from applicationWorker import application
from applicationWorker.model import User
from flask import request, jsonify, json
app = application.app
db = application.db

@app.route('/')
def index():
    return 'hello world'

@app.route('/addUser',methods=['POST'])
def addUser():
    name = request.form['name']
    age = request.form['age']
    email = request.form['email']

    user = User(name,age,email)
    db.session.add(user)
    db.session.commit()
    print('插入成功')
    return jsonify(code=200, status=0, message='ok', data={})


if __name__ == '__main__':
    app.run(debug=True)