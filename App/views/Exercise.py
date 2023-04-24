from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for, requests
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required

from.index import index_views

from App.controllers import (
    create_Exercise,
    get_exercise,
    get_exercise_by_name,

    get_all_exercises,
    get_exercise_by_type,
    get_exercise_by_muscle_group,
    get_exercise_by_difficulty


)

Exercise_views = Blueprint('Exercise_views', __name__, template_folder='../templates')

API_URL = 'https://api.api-ninjas.com/v1/exercises'

API_KEY = 'ccX+1aQ6Qe3He8aYOCMjaA==2yOIcS8AuOndFrKA'


@Exercise_views.route('/exercises', methods=['GET'])
def get_Exercise_page():
    exercises = get_all_exercises()
    return render_template('equipment.html', exercise=exercises)

@Exercise_views.route('/api/exercises', methods=['GET'])
def get_exercise_action():

    exercises = requests.get(API_URL, headers={'X-Api-Key': f'{API_KEY}'})

    if exercises.ok:
        return render_template('equipment.html', exercise=exercises)




@Exercise_views.route('/exercises/id>', methods=['GET'])

def get_Exercise_Action(id):
    exercises = get_exercise(id)
    #if exercises:
    #    return jsonify(exercises.toJSON())
    #return jsonify({"message": f'Exercise with id {Id} not found'}), 404
    return render_template('equipment.html', exercise=exercises)




@Exercise_views.route('/exercises/<name>', methods=['GET'])
def get_Exercise_by_name_Action(name):

    exercises = get_exercise_by_name(name)
    #if exercises:
     #   return jsonify(exercises.toJSON())
    #return jsonify({"message": f'Exercise with name " {name} " not found'}), 404

    return render_template('equipment.html', exercise=exercises)

@Exercise_views.route('/exercises/type/<exercise_type>', methods=['GET'])
def get_Exercise_by_Type_Action(exercise_type):
    exercises = get_exercise_by_type(exercise_type)
    #if exercises:
        #   return jsonify(exercises.toJSON())
    return render_template('equipment.html', exercise_type = exercise_type)


@Exercise_views.route('/exercises/muscle/<muscle_group>', methods=['GET'])
def get_Exercise_by_Group_Action(muscle_group):
    exercises = get_exercise_by_muscle_group(muscle_group)
    #if exercises:
        #   return jsonify(exercises.toJSON())
    return render_template('equipment.html', muscle_group = muscle_group)



@Exercise_views.route('/exercises/difficulty/<difficulty>', methods=['GET'])
def get_Exercise_by_Difficulty_Action(difficulty):
    exercises = get_exercise_by_difficulty(difficulty)
    #if exercises:
        #   return jsonify(exercises.toJSON())
    return render_template('equipment.html', difficulty = difficulty)

