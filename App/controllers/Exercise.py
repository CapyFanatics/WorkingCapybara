from App.models import Exercise
from App.database import db

import requests


API_URL = 'https://wger.de/api/v2/exercise/?language=2'
API_KEY = 'db41e887abdeee70f768105f746b93afa2a1e856'

def get_api_data(API_URL, API_KEY):
    response = requests.get(API_URL, headers=({'X-Api-Key': 'API_KEY'}) )
    data = response.json()
    #data = data['results'][1]['name']
    return data



import requests

API_URL = 'https://wger.de/api/v2/exercise/?language=2'
API_KEY = 'db41e887abdeee70f768105f746b93afa2a1e856'

API_IMAGE = 'https://wger.de/api/v2/exerciseimage/'

def create_Exercise(name, uuid):
    NewExercise = Exercise(name=name, uuid=uuid)
    db.session.add(NewExercise)
    db.session.commit()
    return NewExercise

def get_api_data(API_URL, API_KEY):
    response = requests.get(API_URL, headers=({'X-Api-Key': 'API_KEY'}) )
    data = response.json()

    # for item in data['results']:
    #     create_Exercise(item['name'], item['uuid'])
    return data

def get_api_image(API_IMAGE, API_KEY):
    response = requests.get(API_IMAGE, headers=({'X-Api-Key': 'API_KEY'}))
    images = response.json()
    return images



def get_exercise(id):
    return Exercise.query.get(id)

def get_exercise_by_uuid(uuid):
    return Exercise.query.filter_by(uuid=uuid)


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

