from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required

from.index import index_views

from App.controllers import (
    create_user,
    update_user,
    jwt_authenticate, 
    get_all_users,
    get_all_users_json,
    jwt_required
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')

@user_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_all_users()
    return render_template('users.html', users=users)

@user_views.route('/users/update', methods=['PUT'])

def update_user(id, username):

    user = update_user(id, username)
    return render_template('users.html', users=user)

@user_views.route('/api/users', methods=['GET'])
def get_users_action():
    users = get_all_users_json()
    return jsonify(users)

@user_views.route('/api/users', methods=['POST'])
def create_user_endpoint():
    data = request.json
    create_user(data['username'], data['password'])
    return jsonify({'message': f"user {data['username']} created"})

@user_views.route('/users', methods=['POST'])
def create_user_action():
    data = request.form
    flash(f"User {data['username']} created!")
    create_user(data['username'], data['password'])
    return redirect(url_for('user_views.get_user_page'))

@user_views.route('/static/users', methods=['GET'])
def static_user_page():
  return send_from_directory('static', 'static-user.html')



@user_views.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        current_user.change_username(request.form.get('username'))
        current_user.change_password(request.form.get('password'))
        flash('Profile updated successfully!')
        return redirect(url_for('user_views.profile'))

    return render_template('profile.html', username=current_user.username)

@user_views.route('/change_username', methods=['POST'])
@login_required
def change_username():
    new_username = request.form['new_username']
    current_user.change_username(new_username)
    flash('Username changed successfully!')
    return redirect(url_for('user_views.profile'))

@user_views.route('/change_password', methods=['POST'])
@login_required
def change_password():
    new_password = request.form['new_password']
    current_user.change_password(new_password)
    flash('Password changed successfully!')
    return redirect(url_for('user_views.profile'))