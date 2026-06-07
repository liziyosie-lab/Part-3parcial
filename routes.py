from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import db, bcrypt
from app.models import User

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return redirect(url_for('main.dashboard') if current_user.is_authenticated else url_for('main.login'))

@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        confirm = request.form.get('confirm_password', '')

        if not username or not email or not password:
            flash('Todos los campos son obligatorios.', 'danger')
            return render_template('register.html')

        if password != confirm:
            flash('Las contraseñas no coinciden.', 'danger')
            return render_template('register.html')

        if User.query.filter_by(email=email).first():
            flash('El correo ya está registrado.', 'danger')
            return render_template('register.html')

        if User.query.filter_by(username=username).first():
            flash('El usuario ya existe.', 'danger')
            return render_template('register.html')

        hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(username=username, email=email, password=hashed_pw)
        db.session.add(user)
        db.session.commit()

        flash('¡Cuenta creada exitosamente! Ahora puedes iniciar sesión.', 'success')
        return redirect(url_for('main.login'))

    return render_template('register.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        remember = request.form.get('remember') == 'on'

        user = User.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user, remember=remember)
            flash(f'¡Bienvenido, {user.username}!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page or url_for('main.dashboard'))
        else:
            flash('Correo o contraseña incorrectos.', 'danger')

    return render_template('login.html')

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión correctamente.', 'info')
    return redirect(url_for('main.login'))
