from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db


class UserExercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'))
    exercise = db.relationship('Exercise')
    date = db.Column(db.DateTime, nullable=False)
    reps = db.Column(db.Integer, nullable=False)
    sets = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Float)

    def __repr__(self):
      return f'<UserExercise {self.id} : {self.name} User {self.user.username}>'

    def add_exercise(self, exercise_id, name, reps, sets):
        exercise = Exercise.query.get(exercise_id)

        if exercise:
            try:
                user_exercise = UserExercise(self.id, exercise_id, name, reps, sets)
                db.session.add(user_exercise)
                db.session.commit()
                return user_exercise
            except Exception:
                db.session.rollback()
                return None

        return None

    def delete_exercise(self, exercise_id, name, reps, sets):
        exercise = Exercise.query.get(exercise_id)

        if exercise.user == self:
            db.session.delete(exercise)
            db.session.commit()
            return True
        return None

    def edit_exercise(self, exercise_id, name, reps, sets):
        exercise = Exercise.query.get(exercis_id)

        if exercise.user == self:
            exercise.name = name
            execise.reps = reps
            exercise.sets = sets

            db.session.add(exercise)
            db.session.commit()
            return True
        return None




    def get_json(self):
        return{
            'id' : self.id,
            'name' : self.name,
            'user' : self.user.username,
            'date' : self.date,
            'reps' : self.reps,
            'sets' : self.sets,
            'weight' : self.weight
        }




class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    exercise = db.relationship('UserExercise', backref='user')

    def __init__(self, username, password, email):
        self.username = username
        self.email = email
        self.set_password(password)

    def change_email(self, new_email):
        self.email = new_email
        self.save()

    def change_password(self, new_password):
        self.password = new_password
        self.save()

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)



    def __repr__(self):
        return{
            'id' : self.id,
            'name' : self.name
        }





    def get_json(self):
        return{
            'id': self.id,
            'username': self.username
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

