from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required

from.index import index_views

from App.controllers import (
    create_Exercise,
    get_exercise,
    get_exercise_by_name,
    get_all_exercises
)

Exercise_views = Blueprint('Exercise_views', name, template_folder='../templates')

@Exercise_views.route('/exercises', methods=['GET'])
def get_Exercise_page():
    exercises = get_all_exercises()
    return render_template('equipment.html', exercise=exercises)


@Exercise_views.route('/exercises/<int:id>', methods=['GET'])
def get_Exercise_Action(id):
    exercises = get_exercise(id)
    return render_template('equipment.html', exercise=exercises)


@Exercise_views.route('/exercises/<string:name>', methods=['GET'])
def get_Exercise_Action(name):
    exercises = get_exercise_by_name(name)
    return render_template('equipment.html', exercise=exercises)