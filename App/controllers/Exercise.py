from App.models import Exercise
from App.database import db


def create_Exercise(name):
    NewExercise = Exercise(name=name)
    db.session.add(NewExercise)
    db.session.commit()
    return NewExercise


def get_exercise(id):
    return Exercise.query.get(id)

def get_exercise_by_name():
    return Exercise.query.filter_by(name=name).first()
    
def get_all_exercises():
    return Exercise.query.all()

