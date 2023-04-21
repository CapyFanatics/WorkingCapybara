from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import login_required, login_user, current_user, logout_user

from App.models.user import User
from App.models.Exercise import Exercise
from App.models.userExercise import UserExercise
from App.database import db

from flask_login import LoginManager

from.index import index_views

from App.controllers import (
    create_user,
    jwt_authenticate,
    login,
    get_exercise_by_type
)

auth_views = Blueprint('auth_views', __name__, template_folder='../templates')

'''
Page/Action Routes
'''

@auth_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_all_users()
    return render_template('users.html', users=users)


@auth_views.route('/identify', methods=['GET'])
@login_required
def identify_page():
    return jsonify({'message': f"username: {current_user.username}, id : {current_user.id}"})




# Page routes


@auth_views.route ("/", methods=['GET'])
def login():
    return render_template("login.html")

@auth_views.route("/signup", methods=['GET'])
def signup_page():
  return render_template('signup.html')

@auth_views.route("/profile", methods=['GET'])
def profile_page():
    return render_template('profile.html')

# @auth_views.route("/app", methods=['GET'])
# @auth_views.route("/app/<int:exercise_id>", methods=['GET'])
# @login_required
# def home_page(exercise_id):
#     exercise = Exercise.query.get(exercise_id)
#     user_Exercises = UserExercise.query.filter_by(exercise_id=current_Exercise.id).all()
#     exercises = Exercise.query.all()

#     return render_template("equipment.html", exercise=exercise, user_Exercises=user_Exercises, exercises=exercises)

#Form Action routes

@auth_views.route("/login", methods=['POST'])
def login_action():
    data = request.form

    user = User.query.filter_by(username=data['username']).first()
    if user and user.check_password(data['password']):
        flash('Logged in successfully')
        login_user(user)
        return redirect('/equipment')
    else:
        flash('Invalid username or password')
    return redirect('/')

@auth_views.route("/signup", methods=['POST'])
def signup_action():
    data = request.form
    new_user = User(username=data['username'], password=data['password'])
    try:
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        flash('Account Created')
        return redirect('/equipment')
    except Exception:
        db.session.rollback()
    return redirect('/signup')

@auth_views.route('/logout', methods=['GET'])
@login_required
def logout_action():
    logout_user()
    return redirect('/')


@auth_views.route('/equipment', methods=['GET'])
def equipment_action():
    return render_template("equipment.html")

'''
API Routes
'''

@auth_views.route('/api/users', methods=['GET'])
def get_users_action():
    users = get_all_users_json()
    return jsonify(users)

@auth_views.route('/api/users', methods=['POST'])
def create_user_endpoint():
    data = request.json
    create_user(data['username'], data['password'])
    return jsonify({'message': f"user {data['username']} created"})

@auth_views.route('/api/login', methods=['POST'])
def user_login_api():
  data = request.json
  token = jwt_authenticate(data['username'], data['password'])
  if not token:
    return jsonify(message='bad username or password given'), 401
  return jsonify(access_token=token)

@auth_views.route('/api/identify', methods=['GET'])
@jwt_required()
def identify_user_action():
    return jsonify({'message': f"username: {jwt_current_user.username}, id : {jwt_current_user.id}"})