from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_user, logout_user, current_user, login_required
from models.models import db, User
from forms import RegistrationForm, LoginForm
from itsdangerous import URLSafeTimedSerializer
from extensions import mail
from flask_mail import Message

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        # Send confirmation email
        send_confirmation_email(user)

        flash('A confirmation email has been sent to your email address. Please confirm to complete your registration.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            flash('Username does not exist.', 'danger')
            return redirect(url_for('auth.login'))
        if not user.check_password(form.password.data):
            flash('Incorrect password.', 'danger')
            return redirect(url_for('auth.login'))
        if not user.email_verified:
            flash('Email address not verified. Please check your email.', 'warning')
            return redirect(url_for('auth.login'))
        login_user(user)
        return redirect(url_for('profile.life_stage'))
    return render_template('login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/confirm/<token>')
def confirm_email(token):
    try:
        email = confirm_token(token)
    except:
        flash('The confirmation link is invalid or has expired.', 'danger')
        return redirect(url_for('auth.login'))
    
    user = User.query.filter_by(email=email).first_or_404()
    if user.email_verified:
        flash('Account already confirmed. Please login.', 'success')
    else:
        user.email_verified = True
        db.session.add(user)
        db.session.commit()
        flash('You have confirmed your account. Thanks!', 'success')
    return redirect(url_for('auth.login'))

def send_confirmation_email(user):
    token = generate_confirmation_token(user.email)
    confirm_url = url_for('auth.confirm_email', token=token, _external=True)
    html = render_template('activate.html', confirm_url=confirm_url)
    subject = "Please confirm your email"
    send_email(user.email, subject, html)

def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    return serializer.dumps(email, salt=current_app.config['SECURITY_PASSWORD_SALT'])

def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    try:
        email = serializer.loads(token, salt=current_app.config['SECURITY_PASSWORD_SALT'], max_age=expiration)
    except:
        return False
    return email

def send_email(to, subject, template):
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender=current_app.config['MAIL_DEFAULT_SENDER']
    )
    mail.send(msg)