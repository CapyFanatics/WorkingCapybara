from App.models import UserExercise
from App.database import db


def create_UserExercise( name, reps, sets):
    newuserexercise = UserExercise(name=name, reps=reps, sets=sets)
    db.session.add(newuserexercise)
    db.session.commit()
    return newuserexercise



def get_userexercise(id):
    return UserExercise.query.filter_by(id=id).first()


def get_all_userexercise():
    return UserExercise.query.all()


def update_userexercise(id, name, reps, sets, weight):
    userexercise = get_userexercise(id)
    if userexercise:
        userexercise.name = name
        userexercise.reps = reps
        userexercise.sets = sets
        userexercise.weight = weight
        db.session.add(userexercise)
        db.session.commit()
        return userexercise
    return None


def delete_userexercise(id):
    userexercise = get_userexercise(id)
    if userexercise:
        db.session.delete(userexercise)
        db.session.commit()
        return True
    return None



