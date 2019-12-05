from day03.flaskSql import db
class EmpMaster(db.Model):
    emp_id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer)
    email = db.Column(db.String(50))
    phone_nr = db.Column(db.String(20))
    education = db.Column(db.String(20))
    marital_stat = db.Column(db.String(20))
    nr_of_children = db.Column(db.Integer)

    def __repr__(self):
        return '<emp_master %r>' % 'id:{}'.format(self.emp_id)
