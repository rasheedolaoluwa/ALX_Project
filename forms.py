from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField
from wtforms.validators import DataRequired, Email, EqualTo
from questions import life_stage_questions, financial_resources_questions, investment_experience_questions, emotional_risk_tolerance_questions

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

def create_dynamic_form(questions):
    class DynamicForm(FlaskForm):
        pass

    for i, q in enumerate(questions):
        field_name = f'q{i+1}'
        choices = [(str(a["score"]), a["answer"]) for a in q["answers"]]
        setattr(DynamicForm, field_name, RadioField(q["question"], choices=choices, validators=[DataRequired()]))

    setattr(DynamicForm, 'submit', SubmitField('Next'))
    return DynamicForm

LifeStageForm = create_dynamic_form(life_stage_questions)
FinancialResourcesForm = create_dynamic_form(financial_resources_questions)
InvestmentExperienceForm = create_dynamic_form(investment_experience_questions)
EmotionalRiskToleranceForm = create_dynamic_form(emotional_risk_tolerance_questions)