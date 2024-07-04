@recommendations.route('/recommendations')
@login_required
def get_recommendations():
    allocations = {
        'Conservative': {
            'Fixed Income': 50,
            'Real Estate': 30,
            'Equities': 5,
            'Alternatives': 15
        },
        'Moderate': {
            'Fixed Income': 40,
            'Real Estate': 20,
            'Equities': 15,
            'Alternatives': 25
        },
        'Aggressive': {
            'Fixed Income': 30,
            'Real Estate': 10,
            'Equities': 30,
            'Alternatives': 30
        }
    }

    user_allocations = allocations.get(current_user.risk_category, {})

    return render_template('recommendations.html', allocations=user_allocations)