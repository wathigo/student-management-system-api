
from app import db, flask_bcrypt

class Admin(db.Model):
    "Admin model to store all the admins"
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(70), nullable=False)
    last_name = db.Column(db.String(70), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    password_hash = db.Column(db.String(100), nullable=True)

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<Admin '{}'>".format(self.first_name)

class Parent(db.Model):
    __tablename__ = "parent"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(70), nullable=False)
    last_name = db.Column(db.String(70), nullable=False)
    email = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return "<Parent '{}'>".format(self.first_name)

class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    admno = db.Column(db.Integer, nullable=False)
    first_name = db.Column(db.String(70), nullable=False)
    last_name = db.Column(db.String(70), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('parent.id'))

    def __repr__(self):
        return "<Student '{}'>".format(self.first_name)

class Semister(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(70), nullable=False)

    def __repr__(self):
        return "<Semister '{}'>".format(self.first_name)

class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(70), nullable=False)

class Unit(db.Model):
    __tablename__ = "unit"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(70), nullable=False)
    semister_id = db.Column(db.Integer, db.ForeignKey('semister.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))

    def __repr__(self):
        return "<Unit '{}'>".format(self.name)

class Result(db.Model):
    __tablename__ = "result"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    semister_id = db.Column(db.Integer, db.ForeignKey('semister.id'))
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"))
    unit_id = db.Column(db.Integer, db.ForeignKey("unit.id"))
    score = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<Result '{}'>".format(self.id)

class Fee(db.Model):
    __tablename__ = "fee"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"))
    semister_id = db.Column(db.Integer, db.ForeignKey('semister.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    total = db.Column(db.Integer, nullable=False)
    paid = db.Column(db.Integer, nullable=False)
    balance = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<Fee '{}'>".format(self.id)
