from flask import Blueprint, render_template
from flask_login import login_required, current_user

recommendations = Blueprint('recommendations', __name__)

@recommendations.route('/')
@login_required
def show_recommendations():
    user_profile = current_user.profile
    risk_category = user_profile.risk_category

    # Define the asset allocations based on risk category
    allocations = {
        'Aggressive': {'Fixed Income': 10, 'Real Estate': 10, 'Equities': 60, 'Alternatives': 20},
        'Moderately Aggressive': {'Fixed Income': 20, 'Real Estate': 15, 'Equities': 50, 'Alternatives': 15},
        'Moderate': {'Fixed Income': 40, 'Real Estate': 20, 'Equities': 25, 'Alternatives': 15},
        'Moderately Conservative': {'Fixed Income': 50, 'Real Estate': 20, 'Equities': 15, 'Alternatives': 15},
        'Conservative': {'Fixed Income': 60, 'Real Estate': 20, 'Equities': 10, 'Alternatives': 10}
    }

    # Get the user's recommended allocation based on their risk category
    user_allocation = allocations.get(risk_category, {})

    return render_template('recommendations.html', allocation=user_allocation, risk_category=risk_category)