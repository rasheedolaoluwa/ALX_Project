from flask import Blueprint, request, jsonify
from flask_login import current_user, login_required
from models.models import db, User

profile = Blueprint('profile', __name__)

@profile.route('/profile', methods=['GET'])
@login_required
def get_profile():
    user = User.query.get(current_user.id)
    if user:
        return jsonify({
            'username': user.username,
            'email': user.email
        })
    return jsonify({'error': 'User not found'}), 404

@profile.route('/profile', methods=['PUT'])
@login_required
def update_profile():
    data = request.get_json()
    user = User.query.get(current_user.id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    if 'username' in data:
        user.username = data['username']
    if 'email' in data:
        user.email = data['email']
    
    db.session.commit()
    return jsonify({'message': 'Profile updated successfully'})