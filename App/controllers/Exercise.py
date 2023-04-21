from App.models import Exercise
from App.database import db


def create_Exercise(name, exercise_type, muscle_group, difficulty):
    NewExercise = Exercise(name=name, exercise_type=exercise_type, muscle_group=muscle_group, difficulty=difficulty)
    db.session.add(NewExercise)
    db.session.commit()
    return NewExercise


def get_exercise(id):
    return Exercise.query.get(id)

def get_exercise_by_type(exerciseType):
    return Exercise.query.filter_by(exercise_type = exerciseType)


def get_exercise_by_muscle_group(muscleGroup):
    return Exercise.query.filter_by(muscle_group = muscleGroup)

def get_exercise_by_difficulty(difficulty):
    return Exercise.query.filter_by(difficulty = difficulty)

def get_exercise_by_name(name):
    return Exercise.query.filter_by(name=name).first()
    
def get_all_exercises():
    return Exercise.query.all()

