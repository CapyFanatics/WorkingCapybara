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

    def add_exercise(self, exercise_uuid, name, reps, sets, weight):
        exercise = Exercise.query.filter_by(exercise_uuid).first()

        if exercise:
            try:
                user_exercise = UserExercise(
                    user_id=self.id,
                    exercise_id=exercise_id,
                    name=name,
                    reps=reps,
                    sets=sets,
                    weight=weight,
                    uuid=uuid
                )
                db.session.add(user_exercise)
                db.session.commit()
                return user_exercise
            except Exception as e:
                db.session.rollback()
                print(e)
                return None

        return None


    def delete_exercise(self, exercise_uuid):
        user_exercise = UserExercise.query.filter_by(
            user_id=self.id, exercise_uuid=exercise_uuid
        ).first()

        if user_exercise:
            db.session.delete(user_exercise)
            db.session.commit()
            return True

        return None


    def edit_exercise(self, exercise_uuid, name, reps, sets, weight):
        user_exercise = UserExercise.query.filter_by(
            user_id=self.id, exercise_uuid=exercise_uuid
        ).first()

        if user_exercise:
            user_exercise.name = name
            user_exercise.reps = reps
            user_exercise.sets = sets
            user_exercise.weight = weight
            user_exercise.uuid = uuid

            db.session.add(user_exercise)
            db.session.commit()
            return user_exercise

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