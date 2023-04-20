from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required

from.index import index_views

from App.controllers import (
    delete_userexercise,
    update_userexercise,
    get_all_userexercise,
    get_userexercise,
    create_UserExercise
)

userexercise_views = Blueprint('userexercise_views', __name__, template_folder='../templates')

API_URL = 'https://api.api-ninjas.com/v1/exercises'


@userexercise_views.route('/userexercises', methods=['GET'])
def get_userexercise_page():
    userexercises = get_all_userexercise()
    return render_template('equipment.html', userExercise=userexercises)


@userexercise_views.route('/userexercises/<int: id>', methods=['GET'])
def get_userexercise_action(id):
    userexercises = get_userexercise(id)
    return render_template('equipment.html', userExercise=userexercises)


@userexercise_views.route('/userexercises/delete/<int: id>', methods=['DELETE'])
def deleteuserexercise_action(id):
    userexercises = delete_userexercise(id)
    return render_template('equipment.html', userExercise=userexercises)

@userexercise_views.route('/userexercises/update/<int: id>', methods=['PUT'])
def updateuserexercise_action(id):
    userexercise = update_userexercise(id, name, reps, sets, weight)
    return render_template('equipment.html', userExercise=userexercises)