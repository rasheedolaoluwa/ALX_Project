from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_user, logout_user, login_required, current_user
from models.models import db, User
from forms import RegistrationForm, LoginForm
from flask_mail import Message
from extensions import mail  # Import mail from extensions.py

auth = Blueprint('auth', __name__)

def send_email(to, subject, template, **kwargs):
    print(f"Sending email to {to} with subject {subject}")  # Debugging statement
    msg = Message(subject, recipients=[to], html=render_template(template, **kwargs), sender=current_app.config['MAIL_DEFAULT_SENDER'])
    mail.send(msg)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        print("Form validated successfully")  # Debugging statement
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        print("User added to the database")  # Debugging statement
        token = user.generate_confirmation_token()
        print(f"Token generated: {token}")  # Debugging statement
        send_email(user.email, 'Confirm Your Account', 'auth/confirm_email.html', user=user, token=token)
        print("Confirmation email sent")  # Debugging statement
        flash('A confirmation email has been sent to you by email.', 'success')
        return redirect(url_for('auth.login'))
    print("Rendering register template")  # Debugging statement
    return render_template('register.html', form=form)

@auth.route('/confirm/<token>')
def confirm_email(token):
    user = User.verify_confirmation_token(token)
    if not user:
        flash('The confirmation link is invalid or has expired.', 'danger')
        return redirect(url_for('auth.login'))
    if user.email_verified:
        flash('Account already confirmed. Please login.', 'success')
    else:
        user.email_verified = True
        db.session.add(user)
        db.session.commit()
        flash('You have confirmed your account. Thanks!', 'success')
    return redirect(url_for('auth.login'))

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password', 'danger')
            return redirect(url_for('auth.login'))
        if not user.email_verified:
            flash('Please confirm your email address first.', 'warning')
            return redirect(url_for('auth.login'))
        login_user(user)
        return redirect(url_for('profile.life_stage'))
    return render_template('login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))