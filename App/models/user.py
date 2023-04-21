from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db
from .Exercise import Exercise
from .userExercise import UserExercise

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def add_exercise(self, exercise_id, name, reps, sets):
        exercise = Exercise.query.get(exercise_id)

        if exercise:
            try:
                user_exercise = UserExercise(self.id, exercise_id, name, reps, sets, weight)
                db.session.add(user_exercise)
                db.session.commit()
                return user_exercise
            except Exception:
                db.session.rollback()
                return None

        return None

    def delete_exercise(self, exercise_id):
        exercise = Exercise.query.get(exercise_id)

        if exercise.user == self:
            db.session.delete(exercise)
            db.session.commit()
            return True
        return None

    def edit_exercise(self, exercise_id, name, reps, sets, weight):
        exercise = UserExercise.query.get(exercise_id)

        if exercise.user == self:
            exercise.name = name
            exercise.reps = reps
            exercise.sets = sets
            exercise.weight = weight

            db.session.add(exercise)
            db.session.commit()
            return True
        return None

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