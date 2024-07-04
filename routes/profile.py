from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from models.models import db, Profile
from forms import LifeStageForm, FinancialResourcesForm, InvestmentExperienceForm, EmotionalRiskToleranceForm

profile = Blueprint('profile', __name__)

@profile.route('/profile/life_stage', methods=['GET', 'POST'])
@login_required
def life_stage():
    form = LifeStageForm()
    if form.validate_on_submit():
        score = sum(int(request.form[field]) for field in form.data if field.startswith('q'))
        user_profile = Profile.query.filter_by(user_id=current_user.id).first()
        if not user_profile:
            user_profile = Profile(user_id=current_user.id)
        user_profile.life_stage_score = score
        db.session.add(user_profile)
        db.session.commit()
        return redirect(url_for('profile.financial_resources'))
    return render_template('life_stage.html', form=form)

@profile.route('/profile/financial_resources', methods=['GET', 'POST'])
@login_required
def financial_resources():
    form = FinancialResourcesForm()
    if form.validate_on_submit():
        score = sum(int(request.form[field]) for field in form.data if field.startswith('q'))
        user_profile = Profile.query.filter_by(user_id=current_user.id).first()
        user_profile.financial_resources_score = score
        db.session.commit()
        return redirect(url_for('profile.investment_experience'))
    return render_template('financial_resources.html', form=form)

@profile.route('/profile/investment_experience', methods=['GET', 'POST'])
@login_required
def investment_experience():
    form = InvestmentExperienceForm()
    if form.validate_on_submit():
        score = sum(int(request.form[field]) for field in form.data if field.startswith('q'))
        user_profile = Profile.query.filter_by(user_id=current_user.id).first()
        user_profile.investment_experience_score = score
        db.session.commit()
        return redirect(url_for('profile.emotional_risk_tolerance'))
    return render_template('investment_experience.html', form=form)

@profile.route('/profile/emotional_risk_tolerance', methods=['GET', 'POST'])
@login_required
def emotional_risk_tolerance():
    form = EmotionalRiskToleranceForm()
    if form.validate_on_submit():
        score = sum(int(request.form[field]) for field in form.data if field.startswith('q'))
        user_profile = Profile.query.filter_by(user_id=current_user.id).first()
        user_profile.emotional_risk_tolerance_score = score
        user_profile.total_score = (
            user_profile.life_stage_score +
            user_profile.financial_resources_score +
            user_profile.investment_experience_score +
            user_profile.emotional_risk_tolerance_score
        )
        risk_data = determine_risk_category(user_profile)
        user_profile.risk_category = risk_data['risk_category']
        user_profile.life_stage_message = risk_data['life_stage_message']
        user_profile.financial_resources_message = risk_data['financial_resources_message']
        user_profile.investment_experience_message = risk_data['investment_experience_message']
        user_profile.emotional_risk_tolerance_message = risk_data['emotional_risk_tolerance_message']
        db.session.commit()
        return redirect(url_for('profile.result'))
    return render_template('emotional_risk_tolerance.html', form=form)

@profile.route('/profile/result')
@login_required
def result():
    user_profile = Profile.query.filter_by(user_id=current_user.id).first()
    return render_template('result.html', profile=user_profile)

def determine_risk_category(profile):
    # Life Stage
    if profile.life_stage_score <= 4:
        life_stage_message = "You have a short-term investment horizon"
    elif 5 <= profile.life_stage_score <= 9:
        life_stage_message = "You have a medium term investment horizon"
    else:
        life_stage_message = "You have a long term investment horizon"

    # Financial Resources
    if profile.financial_resources_score <= 4:
        financial_resources_message = "Based on your level of financial resources you should consider evaluating your investment goals"
    elif 5 <= profile.financial_resources_score <= 9:
        financial_resources_message = "Your level of financial resources are just sufficient to pursue your investment goals"
    elif 10 <= profile.financial_resources_score <= 14:
        financial_resources_message = "You have enough funds to pursue your investment goals"
    else:
        financial_resources_message = "Based on your level of financial resources you can pursue your investment goals comfortably"

    # Investment Experience
    if profile.investment_experience_score <= 5:
        investment_experience_message = "You are quite new to the investment market"
    else:
        investment_experience_message = "You have some understanding of investment market behavior"

    # Emotional Risk Tolerance
    if profile.emotional_risk_tolerance_score <= 9:
        emotional_risk_tolerance_message = "Your priorities are the safeguarding of your investment capital. You are prepared to sacrifice higher returns for peace of mind."
    elif 10 <= profile.emotional_risk_tolerance_score <= 19:
        emotional_risk_tolerance_message = "Your priority remains the preservation of capital over the medium to long term. You cannot afford to take any chances with your capital."
    elif 20 <= profile.emotional_risk_tolerance_score <= 29:
        emotional_risk_tolerance_message = "You do not wish to see all of your capital eroded by tax and inflation and are prepared to take small short term risk in order to gain longer term capital growth."
    elif 30 <= profile.emotional_risk_tolerance_score <= 39:
        emotional_risk_tolerance_message = "You are most interested in maximizing long term capital growth, although you do not wish to make unbalanced investment decisions."
    else:
        emotional_risk_tolerance_message = "You are prepared to sacrifice your investment capital in the short term in pursuit of the highest long term capital growth investment."

    # Risk Category
    if profile.total_score >= 71:
        risk_category = 'Aggressive'
    elif 61 <= profile.total_score < 71:
        risk_category = 'Moderately Aggressive'
    elif 46 <= profile.total_score < 61:
        risk_category = 'Moderate'
    elif 36 <= profile.total_score < 46:
        risk_category = 'Moderately Conservative'
    else:
        risk_category = 'Conservative'

    return {
        'life_stage_message': life_stage_message,
        'financial_resources_message': financial_resources_message,
        'investment_experience_message': investment_experience_message,
        'emotional_risk_tolerance_message': emotional_risk_tolerance_message,
        'risk_category': risk_category
    }

@profile.route('/submit_profile', methods=['POST'])
@login_required
def submit_profile():
    # Calculate total scores for each category
    life_stage_score = sum([int(value) for value in request.form.getlist('life_stage')])
    financial_resources_score = sum([int(value) for value in request.form.getlist('financial_resources')])
    investment_experience_score = sum([int(value) for value in request.form.getlist('investment_experience')])
    emotional_risk_tolerance_score = sum([int(value) for value in request.form.getlist('emotional_risk_tolerance')])
    
    total_score = life_stage_score + financial_resources_score + investment_experience_score + emotional_risk_tolerance_score

    # Determine risk category based on total score
    if total_score >= 71:
        risk_category = 'Aggressive'
    elif total_score >= 46:
        risk_category = 'Moderate'
    else:
        risk_category = 'Conservative'

    # Update user's profile and risk category
    profile = Profile.query.filter_by(user_id=current_user.id).first()
    profile.life_stage_score = life_stage_score
    profile.financial_resources_score = financial_resources_score
    profile.investment_experience_score = investment_experience_score
    profile.emotional_risk_tolerance_score = emotional_risk_tolerance_score
    profile.total_score = total_score

    current_user.risk_category = risk_category

    db.session.commit()

    return redirect(url_for('profile.recommendations'))